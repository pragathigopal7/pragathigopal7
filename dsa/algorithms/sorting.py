"""Classic sorting algorithms. Each returns a new sorted list."""


def bubble_sort(items):
    """O(n^2); stops early once a pass makes no swaps."""
    a = list(items)
    for end in range(len(a) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break
    return a


def insertion_sort(items):
    """O(n^2) worst case, O(n) on nearly sorted input. Stable."""
    a = list(items)
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(items):
    """O(n log n). Stable."""
    a = list(items)
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(items):
    """O(n log n) average. In-place Lomuto partition with median-of-three pivot."""
    a = list(items)

    def partition(lo, hi):
        mid = (lo + hi) // 2
        # Move the median of a[lo], a[mid], a[hi] to a[hi].
        if a[mid] < a[lo]:
            a[mid], a[lo] = a[lo], a[mid]
        if a[hi] < a[lo]:
            a[hi], a[lo] = a[lo], a[hi]
        if a[mid] < a[hi]:
            a[mid], a[hi] = a[hi], a[mid]
        pivot, i = a[hi], lo
        for j in range(lo, hi):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        return i

    # Recurse on the smaller side to bound stack depth at O(log n).
    def sort(lo, hi):
        while lo < hi:
            p = partition(lo, hi)
            if p - lo < hi - p:
                sort(lo, p - 1)
                lo = p + 1
            else:
                sort(p + 1, hi)
                hi = p - 1

    sort(0, len(a) - 1)
    return a


def heap_sort(items):
    """O(n log n), in place on the copy."""
    a = list(items)
    n = len(a)

    def sift_down(i, size):
        while True:
            largest, l, r = i, 2 * i + 1, 2 * i + 2
            if l < size and a[l] > a[largest]:
                largest = l
            if r < size and a[r] > a[largest]:
                largest = r
            if largest == i:
                return
            a[i], a[largest] = a[largest], a[i]
            i = largest

    for i in reversed(range(n // 2)):
        sift_down(i, n)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(0, end)
    return a


def counting_sort(items):
    """O(n + k) for integers in range of size k."""
    a = list(items)
    if not a:
        return a
    lo, hi = min(a), max(a)
    counts = [0] * (hi - lo + 1)
    for x in a:
        counts[x - lo] += 1
    result = []
    for offset, c in enumerate(counts):
        result.extend([offset + lo] * c)
    return result
