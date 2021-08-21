from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from BinaryTree import BinaryTree
from models import Base, Contact, User

free_users = BinaryTree()
communications = {}

in_users = 0
out_users = 0

engine = create_engine("sqlite:///Data.db")
Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)


def add_users(chat=None, user_chat_id=None, username=None):
    """
    This function add new user in Data Base.
    Information about user_chat_id and username you can take from chat, but Data Base save only
    user_chat_id and username, so for interactions with DB, function use additional arguments:
    user_chat_id and username

    :param chat: It structure call.message.chat from telebot
    :param user_chat_id: Chat id with user
    :param username:
    :return:
    """
    global free_users
    global out_users
    global in_users

    if chat is not None:
        user_id = chat.id
        user_name = chat.username
    else:
        user_id = user_chat_id
        user_name = username

    if user_id in free_users:
        return

    if in_users >= out_users:
        free_users[user_id] = {"state": 0, "ID": user_id, "UserName": user_name}
        out_users = out_users + 1
    elif in_users < out_users:
        free_users[user_id] = {"state": 1, "ID": user_id, "UserName": user_name}
        in_users = in_users + 1

    s = session()
    if len(s.query(User).filter(User.id == user_id).all()) > 0:
        s.query(User).filter(User.id == user_id).update({"status": 0})

        s.commit()
        s.close()
        return

    if user_name is None:
        user_name = "anon"

    s.add(User(id=user_id, username=user_name, like=False, status=0))

    s.commit()
    s.close()


def delete_info(user_id):
    """
    Reset information about user in Data Base
    :param user_id: Chat id with user
    :return:
    """
    global communications

    tmp_id = communications[user_id]["UserTo"]

    communications.pop(user_id)
    communications.pop(tmp_id)

    s = session()

    if len(s.query(Contact).filter(Contact.userID == user_id).all()) > 0:
        s.query(Contact).filter(Contact.userID == user_id).delete()
    else:
        s.query(Contact).filter(Contact.userID == tmp_id).delete()
    s.commit()

    s.query(User).filter(User.id == user_id).update({"status": 3, "like": False})
    s.query(User).filter(User.id == tmp_id).update({"status": 3, "like": False})

    s.commit()
    s.close()


def add_communications(user_id, user_to_id):
    """
    Add dialog in Data Base
    :param user_id: Chat id with first user
    :param user_to_id: Chat id with second user
    :return:
    """
    global free_users

    communications[user_id] = {
        "UserTo": user_to_id,
        "UserName": free_users[user_to_id]["UserName"],
        "like": False,
    }
    communications[user_to_id] = {
        "UserTo": user_id,
        "UserName": free_users[user_id]["UserName"],
        "like": False,
    }

    print(communications[user_id], " ", communications[user_to_id])

    free_users.delete(user_id)
    free_users.delete(user_to_id)

    s = session()

    s.query(User).filter(User.id == user_id).update({"status": 1})
    s.query(User).filter(User.id == user_to_id).update({"status": 1})

    s.add(Contact(userID=user_id, userToID=user_to_id))

    s.commit()
    s.close()


def recovery_data():
    """
    This function recovers data from Data Base, if server was temporarily disabled
    :return:
    """
    global communications

    s = session()

    for i in s.query(Contact).all():
        first = s.query(User).filter(User.id == i.userID).first()
        second = s.query(User).filter(User.id == i.userToID).first()

        communications[i.userID] = {
            "UserTo": second.id,
            "UserName": second.username,
            "like": second.like,
        }
        communications[i.userToID] = {
            "UserTo": first.id,
            "UserName": first.username,
            "like": first.like,
        }

    for i in s.query(User).filter(User.status == 0).all():
        add_users(user_chat_id=i.id, username=i.username)

    s.close()


def update_user_like(user_id):
    """
    Update status about user like in Data Base
    :param user_id: Chat id with user
    :return:
    """
    communications[user_id]["like"] = True

    s = session()

    s.query(User).filter(User.id == user_id).update({"like": True})

    s.commit()
    s.close()


def delete_user_from_db(user_id):
    """
    Delete information about user from Data Base
    :param user_id: Chat id with user
    :return:
    """
    if user_id in free_users:
        free_users.delete(user_id)

    s = session()

    s.query(User).filter(User.id == user_id).delete()

    s.commit()
    s.close()
