# Data Structures & Algorithms in Python

Clean, tested implementations of core data structures and algorithms. Pure Python 3, standard library only.

## Layout

```
dsa/
├── data_structures/
│   ├── linked_list.py         # singly linked list: reverse, middle (slow/fast pointers)
│   ├── stack.py               # LIFO stack
│   ├── queue.py               # FIFO queue built from two stacks
│   ├── min_heap.py            # binary heap with O(n) heapify
│   ├── binary_search_tree.py  # insert / delete / iterative in-order traversal
│   ├── trie.py                # prefix tree with prefix search
│   ├── lru_cache.py           # O(1) LRU cache (hash map + doubly linked list)
│   └── union_find.py          # disjoint set, path compression + union by rank
├── algorithms/
│   ├── sorting.py             # bubble, insertion, merge, quick, heap, counting
│   ├── searching.py           # binary search, lower/upper bound, rotated array
│   ├── graphs.py              # BFS, DFS, shortest path, Dijkstra, topo sort,
│   │                          # cycle detection, Kruskal MST, number of islands
│   └── dynamic_programming.py # fibonacci, coin change, LCS, edit distance,
│                              # 0/1 knapsack, LIS, Kadane
└── tests/
```

## Complexity cheat sheet

| Algorithm / Structure | Time | Space |
|---|---|---|
| Merge sort | O(n log n) | O(n) |
| Quick sort (avg) | O(n log n) | O(log n) |
| Heap sort | O(n log n) | O(1) |
| Counting sort | O(n + k) | O(k) |
| Binary search | O(log n) | O(1) |
| Heap push / pop | O(log n) | — |
| BST ops (balanced / worst) | O(log n) / O(n) | — |
| Trie insert / lookup | O(L) | O(total chars) |
| LRU get / put | O(1) | O(capacity) |
| Union-Find | ~O(α(n)) | O(n) |
| BFS / DFS | O(V + E) | O(V) |
| Dijkstra (binary heap) | O((V + E) log V) | O(V) |
| Kruskal MST | O(E log E) | O(V) |
| Edit distance | O(mn) | O(min(m, n)) |
| LIS (patience) | O(n log n) | O(n) |

## Usage

```python
from dsa.data_structures import LRUCache, Trie
from dsa.algorithms.graphs import dijkstra

cache = LRUCache(2)
cache.put("a", 1)

trie = Trie(["car", "care", "cart"])
trie.words_with_prefix("car")   # ['car', 'care', 'cart']

dijkstra({"A": [("B", 4), ("C", 1)], "C": [("B", 2)], "B": []}, "A")
# {'A': 0, 'C': 1, 'B': 3}
```

## Running the tests

From the repository root:

```bash
python3 -m unittest discover -s dsa/tests -t . -v
```
