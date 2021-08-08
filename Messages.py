import os
from config import PROJECT_NAME

m_start = '⚡️ SELAMAT DATANG DI {PROJECT_NAME} ⚡️\n\n🇮🇩 Semoga Dapat teman atau jodoh\n\n🇳🇿 I hope you can make a friend or a partner\n\n💬 untuk mencari teman obrolan gunakan button New Chat'

m_is_not_free_users = '❗️ Maaf Anda tidak berada dalam obrolan\n❗️ Sorry you are not in chat'
         
m_is_connect = '✅ Anda sudah berada di dalam obrolan, silahkan kirim chat anda\n✅ You are already in the chat, please send your chat'

m_play_again = 'Apakah Anda Ingin mengobrol dengan orang lain?\nDo you want to chat with other people?'

m_is_not_user_name = '❌ Maaf, bot kami hanya dapat berkomunikasi jika Anda memiliki nama pengguna\n❌ Sorry, our bot can only communicate if you have a username'

m_good_bye = '❌ Maaf lawan bicara anda meninggalkan obrolan\n❌ Sorry your interlocutor left the chat'

m_disconnect_user = 'Maaf sambungan telah terputus!\nSorry, the connection was lost!'

m_failed = '❌ Terjadi kesalahan!\n❌ Loss happened'

m_like = '✅ Pilihan yang bagus!\n✅ Great choice'

m_dislike_user = 'Obrolan Telah Berakhir\nChat Has Ended'

m_dislike_user_to = 'Lawan tidak menyukai Anda, Maaf\nThe opponent doesnt like you sorry'

m_send_some_messages = 'Bot tidak bisa meneruskan pesan dari bot\nThe bot could not continue the pan from the bot'

m_has_not_dialog = 'Anda tidak sedang dalam obrolan\nYou are not in chat'

dislike_str = '\U0001F44E Tidak Suka'

like_str = '\U0001F44D Suka'


def m_all_like (x):
    return 'Teman bicara menyukai Anda\n + Nama pengguna: + str (x) \nSemoga berhasil dengan komunikasi Anda!\nTerima kasih telah bersama kami!\nThe interlocutor likes you\n + Username: + str (x)\nGood luck with your communication!\nThanks for being with us!'
