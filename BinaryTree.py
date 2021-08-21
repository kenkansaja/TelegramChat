class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def has_left_child(self):
        return self.leftChild

    def has_right_child(self):
        return self.rightChild

    def is_left_child(self):
        return self.parent and self.parent.leftChild == self

    def is_right_child(self):
        return self.parent and self.parent.rightChild == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.leftChild or self.rightChild)

    def has_any_children(self):
        return self.leftChild or self.rightChild

    def has_all_children(self):
        return self.leftChild and self.rightChild

    def replace_data(self, key, val, lc, rc):
        self.key = key
        self.val = val
        self.leftChild = lc
        self.rightChild = rc
        if self.has_left_child():
            self.leftChild.parent = self
        if self.has_right_child():
            self.rightChild.parent = self

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.leftChild:
                    if elem is not None:
                        yield elem
            yield self.val
            if self.has_right_child():
                for elem in self.rightChild:
                    if elem is not None:
                        yield elem


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.leftChild)
            else:
                current_node.leftChild = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.rightChild)
            else:
                current_node.rightChild = TreeNode(key, val, parent=current_node)

    def put(self, key, val):
        if self.root is None:
            self.root = TreeNode(key, val)
        else:
            self._put(key, val, self.root)
        self.size = self.size + 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.leftChild)
        else:
            return self._get(key, current_node.rightChild)

    def get(self, key):
        if self.root is None:
            return None
        else:
            res = self._get(key, self.root)
            if res is None:
                return None
            else:
                return res.val

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root) is None:
            return False
        else:
            return True

    def find_successor(self):
        successor = None
        if self.hasRightChild():
            successor = self.rightChild.find_min()
        else:
            if self.parent:
                if self.isLeftChild():
                    successor = self.parent
                else:
                    self.parent.rightChild = None
                    successor = self.parent.find_c()
                    self.parent.rightChild = self
        return successor

    def find_min(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def splice_out(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def remove(self, current_node):
        if current_node.is_leaf():
            if current_node == current_node.parent.leftChild:
                current_node.parent.leftChild = None
            else:
                current_node.parent.rightChild = None
        elif current_node.hasBothChildren():  # interior
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.payload = successor.payload
        else:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.leftChild.parent = current_node.parent
                    current_node.parent.leftChild = current_node.leftChild
                elif current_node.is_right_child():
                    current_node.leftChild.parent = current_node.parent
                    current_node.parent.rightChild = current_node.leftChild
                else:
                    current_node.replaceNodeData(
                        current_node.leftChild.key,
                        current_node.leftChild.payload,
                        current_node.leftChild.leftChild,
                        current_node.leftChild.rightChild,
                    )
            else:
                if current_node.is_left_child():
                    current_node.rightChild.parent = current_node.parent
                    current_node.parent.leftChild = current_node.rightChild
                elif current_node.is_right_child():
                    current_node.rightChild.parent = current_node.parent
                    current_node.parent.rightChild = current_node.rightChild
                else:
                    current_node.replaceNodeData(
                        current_node.rightChild.key,
                        current_node.rightChild.payload,
                        current_node.rightChild.leftChild,
                        current_node.rightChild.rightChild,
                    )

    def delete(self, key):
        if self.size > 1:
            node_for_remove = self._get(key, self.root)
            if node_for_remove:
                self.remove(node_for_remove)
                self.size = self.size - 1
            else:
                raise KeyError("Error, node with key is not found")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError("Error, node with key is not found")

    def __delitem__(self, key):
        self.delete(key)

    def __iter__(self):
        for i in self.root:
            yield i
