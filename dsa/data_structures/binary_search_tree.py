"""Unbalanced binary search tree with no duplicate keys."""


class _Node:
    __slots__ = ("key", "left", "right")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, iterable=()):
        self._root = None
        self._size = 0
        for key in iterable:
            self.insert(key)

    def __len__(self):
        return self._size

    def __contains__(self, key):
        node = self._root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def insert(self, key):
        """Insert key; returns False if it was already present."""
        if self._root is None:
            self._root = _Node(key)
            self._size = 1
            return True
        node = self._root
        while True:
            if key == node.key:
                return False
            side = "left" if key < node.key else "right"
            child = getattr(node, side)
            if child is None:
                setattr(node, side, _Node(key))
                self._size += 1
                return True
            node = child

    def delete(self, key):
        """Delete key; raises KeyError if absent."""
        self._root = self._delete(self._root, key)
        self._size -= 1

    def _delete(self, node, key):
        if node is None:
            raise KeyError(key)
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Replace with in-order successor.
            succ = node.right
            while succ.left:
                succ = succ.left
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)
        return node

    def inorder(self):
        """Yield keys in sorted order (iterative traversal)."""
        stack, node = [], self._root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.key
            node = node.right

    def height(self):
        def h(node):
            return 0 if node is None else 1 + max(h(node.left), h(node.right))

        return h(self._root)

    def min(self):
        if self._root is None:
            raise ValueError("min of empty tree")
        node = self._root
        while node.left:
            node = node.left
        return node.key

    def max(self):
        if self._root is None:
            raise ValueError("max of empty tree")
        node = self._root
        while node.right:
            node = node.right
        return node.key
