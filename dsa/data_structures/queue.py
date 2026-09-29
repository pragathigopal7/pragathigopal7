"""FIFO queue implemented with two stacks (amortized O(1) operations)."""


class Queue:
    def __init__(self):
        self._in = []
        self._out = []

    def __len__(self):
        return len(self._in) + len(self._out)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, item):
        self._in.append(item)

    def _shift(self):
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def dequeue(self):
        self._shift()
        if not self._out:
            raise IndexError("dequeue from empty queue")
        return self._out.pop()

    def peek(self):
        self._shift()
        if not self._out:
            raise IndexError("peek from empty queue")
        return self._out[-1]
