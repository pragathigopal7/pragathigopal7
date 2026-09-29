"""Singly linked list."""


class _Node:
    __slots__ = ("value", "next")

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, iterable=()):
        self._head = None
        self._size = 0
        for item in iterable:
            self.append(item)

    def __len__(self):
        return self._size

    def __iter__(self):
        node = self._head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return f"LinkedList({list(self)})"

    def prepend(self, value):
        """O(1)"""
        self._head = _Node(value, self._head)
        self._size += 1

    def append(self, value):
        """O(n)"""
        if self._head is None:
            self._head = _Node(value)
        else:
            node = self._head
            while node.next:
                node = node.next
            node.next = _Node(value)
        self._size += 1

    def remove(self, value):
        """Remove the first occurrence of value. O(n). Raises ValueError if absent."""
        prev, node = None, self._head
        while node:
            if node.value == value:
                if prev:
                    prev.next = node.next
                else:
                    self._head = node.next
                self._size -= 1
                return
            prev, node = node, node.next
        raise ValueError(f"{value!r} not in list")

    def reverse(self):
        """Reverse in place. O(n) time, O(1) space."""
        prev, node = None, self._head
        while node:
            node.next, prev, node = prev, node, node.next
        self._head = prev

    def middle(self):
        """Return the middle value using slow/fast pointers."""
        if self._head is None:
            raise IndexError("middle of empty list")
        slow = fast = self._head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        return slow.value
