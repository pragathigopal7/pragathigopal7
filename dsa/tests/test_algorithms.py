import random
import unittest

from dsa.algorithms import dynamic_programming as dp
from dsa.algorithms import graphs, searching, sorting


class TestSorting(unittest.TestCase):
    SORTS = [
        sorting.bubble_sort,
        sorting.insertion_sort,
        sorting.merge_sort,
        sorting.quick_sort,
        sorting.heap_sort,
        sorting.counting_sort,
    ]

    def test_all_sorts(self):
        rng = random.Random(42)
        cases = [[], [1], [2, 1], [3, 3, 3], list(range(20)), list(range(20, 0, -1))]
        cases += [[rng.randint(-50, 50) for _ in range(rng.randint(0, 60))] for _ in range(25)]
        for sort in self.SORTS:
            for case in cases:
                with self.subTest(sort=sort.__name__, case=case):
                    original = list(case)
                    self.assertEqual(sort(case), sorted(case))
                    self.assertEqual(case, original)  # input untouched


class TestSearching(unittest.TestCase):
    def test_binary_search(self):
        arr = [1, 3, 5, 7, 9]
        for i, x in enumerate(arr):
            self.assertEqual(searching.binary_search(arr, x), i)
        self.assertEqual(searching.binary_search(arr, 4), -1)
        self.assertEqual(searching.binary_search([], 1), -1)

    def test_bounds(self):
        arr = [1, 2, 2, 2, 5]
        self.assertEqual(searching.lower_bound(arr, 2), 1)
        self.assertEqual(searching.upper_bound(arr, 2), 4)
        self.assertEqual(searching.lower_bound(arr, 6), 5)

    def test_rotated(self):
        arr = [4, 5, 6, 7, 0, 1, 2]
        for i, x in enumerate(arr):
            self.assertEqual(searching.search_rotated(arr, x), i)
        self.assertEqual(searching.search_rotated(arr, 3), -1)


class TestGraphs(unittest.TestCase):
    GRAPH = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": ["F"], "E": ["F"], "F": []}

    def test_traversals(self):
        self.assertEqual(graphs.bfs(self.GRAPH, "A"), ["A", "B", "C", "D", "E", "F"])
        self.assertEqual(graphs.dfs(self.GRAPH, "A"), ["A", "B", "D", "F", "C", "E"])

    def test_shortest_path(self):
        self.assertEqual(graphs.shortest_path_unweighted(self.GRAPH, "A", "F"), ["A", "B", "D", "F"])
        self.assertIsNone(graphs.shortest_path_unweighted(self.GRAPH, "F", "A"))

    def test_dijkstra(self):
        g = {"A": [("B", 4), ("C", 1)], "C": [("B", 2), ("D", 5)], "B": [("D", 1)], "D": []}
        self.assertEqual(graphs.dijkstra(g, "A"), {"A": 0, "B": 3, "C": 1, "D": 4})

    def test_topological_sort_and_cycles(self):
        order = graphs.topological_sort(self.GRAPH)
        pos = {n: i for i, n in enumerate(order)}
        for u, vs in self.GRAPH.items():
            for v in vs:
                self.assertLess(pos[u], pos[v])
        cyclic = {"x": ["y"], "y": ["z"], "z": ["x"]}
        self.assertTrue(graphs.has_cycle_directed(cyclic))
        self.assertFalse(graphs.has_cycle_directed(self.GRAPH))
        with self.assertRaises(ValueError):
            graphs.topological_sort(cyclic)

    def test_kruskal(self):
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        total, chosen = graphs.kruskal_mst(4, edges)
        self.assertEqual(total, 19)
        self.assertEqual(len(chosen), 3)

    def test_islands(self):
        grid = ["11000", "11000", "00100", "00011"]
        self.assertEqual(graphs.count_islands(grid), 3)
        self.assertEqual(graphs.count_islands([]), 0)


class TestDynamicProgramming(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual([dp.fibonacci(i) for i in range(10)], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(dp.climb_stairs(5), 8)

    def test_coin_change(self):
        self.assertEqual(dp.coin_change([1, 2, 5], 11), 3)
        self.assertEqual(dp.coin_change([2], 3), -1)
        self.assertEqual(dp.coin_change([1], 0), 0)

    def test_lcs(self):
        self.assertEqual(dp.longest_common_subsequence("abcde", "ace"), "ace")
        self.assertEqual(dp.longest_common_subsequence("abc", "def"), "")

    def test_edit_distance(self):
        self.assertEqual(dp.edit_distance("kitten", "sitting"), 3)
        self.assertEqual(dp.edit_distance("", "abc"), 3)

    def test_knapsack(self):
        self.assertEqual(dp.knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7), 9)

    def test_lis_and_kadane(self):
        self.assertEqual(dp.longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(dp.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(dp.max_subarray([-3, -1, -2]), -1)


if __name__ == "__main__":
    unittest.main()
