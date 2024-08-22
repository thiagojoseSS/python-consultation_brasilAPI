import json
import re


class Node:
    def __init__(self, key, value):
        self.key = int(key)
        self.value = json.dumps(value)  # Serializando o JSON
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def clean_cnpj(self, cnpj_in):
        try:
            result = re.sub(r'\D', '', cnpj_in)
            return int(result)
        except:
            return int(cnpj_in)

    def insert(self, root, key, value):
        key = self.clean_cnpj(key)
        if not root:
            return Node(key, value)
        elif key < root.key:
            root.left = self.insert(root.left, key, value)
        else:
            root.right = self.insert(root.right, key, value)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return json.loads(root.value) if root else None

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

