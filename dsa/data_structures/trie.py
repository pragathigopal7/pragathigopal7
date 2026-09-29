"""Prefix tree for string keys."""


class _Node:
    __slots__ = ("children", "is_word")

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self, words=()):
        self._root = _Node()
        for word in words:
            self.insert(word)

    def insert(self, word):
        node = self._root
        for ch in word:
            node = node.children.setdefault(ch, _Node())
        node.is_word = True

    def _find(self, prefix):
        node = self._root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def contains(self, word):
        node = self._find(word)
        return node is not None and node.is_word

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def words_with_prefix(self, prefix):
        """Return all stored words beginning with prefix, sorted."""
        node = self._find(prefix)
        if node is None:
            return []
        result = []

        def dfs(n, path):
            if n.is_word:
                result.append(path)
            for ch in sorted(n.children):
                dfs(n.children[ch], path + ch)

        dfs(node, prefix)
        return result
