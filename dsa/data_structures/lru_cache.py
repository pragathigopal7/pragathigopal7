"""Least-recently-used cache: hash map + doubly linked list, O(1) get/put."""


class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._map = {}
        # Sentinels: head.next is most recent, tail.prev is least recent.
        self._head, self._tail = _Node(), _Node()
        self._head.next, self._tail.prev = self._tail, self._head

    def __len__(self):
        return len(self._map)

    def _unlink(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _push_front(self, node):
        node.prev, node.next = self._head, self._head.next
        self._head.next.prev = node
        self._head.next = node

    def get(self, key, default=None):
        node = self._map.get(key)
        if node is None:
            return default
        self._unlink(node)
        self._push_front(node)
        return node.value

    def put(self, key, value):
        node = self._map.get(key)
        if node:
            node.value = value
            self._unlink(node)
        else:
            if len(self._map) == self.capacity:
                lru = self._tail.prev
                self._unlink(lru)
                del self._map[lru.key]
            node = _Node(key, value)
            self._map[key] = node
        self._push_front(node)
