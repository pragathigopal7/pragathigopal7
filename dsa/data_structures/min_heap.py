"""Binary min-heap stored in an array."""


class MinHeap:
    def __init__(self, iterable=()):
        self._data = list(iterable)
        # Heapify bottom-up in O(n).
        for i in reversed(range(len(self._data) // 2)):
            self._sift_down(i)

    def __len__(self):
        return len(self._data)

    def push(self, item):
        """O(log n)"""
        self._data.append(item)
        self._sift_up(len(self._data) - 1)

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def pop(self):
        """Remove and return the smallest item. O(log n)"""
        if not self._data:
            raise IndexError("pop from empty heap")
        last = self._data.pop()
        if not self._data:
            return last
        top, self._data[0] = self._data[0], last
        self._sift_down(0)
        return top

    def _sift_up(self, i):
        data = self._data
        while i > 0:
            parent = (i - 1) // 2
            if data[i] < data[parent]:
                data[i], data[parent] = data[parent], data[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        data, n = self._data, len(self._data)
        while True:
            smallest, left, right = i, 2 * i + 1, 2 * i + 2
            if left < n and data[left] < data[smallest]:
                smallest = left
            if right < n and data[right] < data[smallest]:
                smallest = right
            if smallest == i:
                return
            data[i], data[smallest] = data[smallest], data[i]
            i = smallest
