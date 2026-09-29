import unittest

from dsa.data_structures import (
    BinarySearchTree,
    LinkedList,
    LRUCache,
    MinHeap,
    Queue,
    Stack,
    Trie,
    UnionFind,
)


class TestLinkedList(unittest.TestCase):
    def test_append_prepend_remove(self):
        ll = LinkedList([2, 3])
        ll.prepend(1)
        ll.append(4)
        self.assertEqual(list(ll), [1, 2, 3, 4])
        ll.remove(1)
        ll.remove(3)
        self.assertEqual(list(ll), [2, 4])
        self.assertEqual(len(ll), 2)
        with self.assertRaises(ValueError):
            ll.remove(99)

    def test_reverse_and_middle(self):
        ll = LinkedList(range(5))
        self.assertEqual(ll.middle(), 2)
        ll.reverse()
        self.assertEqual(list(ll), [4, 3, 2, 1, 0])
        with self.assertRaises(IndexError):
            LinkedList().middle()


class TestStackQueue(unittest.TestCase):
    def test_stack(self):
        s = Stack()
        for i in range(3):
            s.push(i)
        self.assertEqual(s.peek(), 2)
        self.assertEqual([s.pop(), s.pop(), s.pop()], [2, 1, 0])
        self.assertTrue(s.is_empty())
        with self.assertRaises(IndexError):
            s.pop()

    def test_queue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(3)
        self.assertEqual(q.peek(), 2)
        self.assertEqual([q.dequeue(), q.dequeue()], [2, 3])
        with self.assertRaises(IndexError):
            q.dequeue()


class TestMinHeap(unittest.TestCase):
    def test_heap_order(self):
        data = [5, 3, 8, 1, 9, 2, 7]
        h = MinHeap(data)
        h.push(0)
        self.assertEqual(h.peek(), 0)
        self.assertEqual([h.pop() for _ in range(len(h))], sorted(data + [0]))
        with self.assertRaises(IndexError):
            h.pop()


class TestBST(unittest.TestCase):
    def test_insert_contains_delete(self):
        t = BinarySearchTree([50, 30, 70, 20, 40, 60, 80])
        self.assertFalse(t.insert(50))
        self.assertIn(40, t)
        self.assertEqual(list(t.inorder()), [20, 30, 40, 50, 60, 70, 80])
        self.assertEqual((t.min(), t.max(), t.height()), (20, 80, 3))
        t.delete(50)  # two children
        t.delete(20)  # leaf
        self.assertEqual(list(t.inorder()), [30, 40, 60, 70, 80])
        self.assertEqual(len(t), 5)
        with self.assertRaises(KeyError):
            t.delete(999)
        self.assertEqual(len(t), 5)


class TestTrie(unittest.TestCase):
    def test_trie(self):
        t = Trie(["car", "cart", "care", "dog"])
        self.assertTrue(t.contains("car"))
        self.assertFalse(t.contains("ca"))
        self.assertTrue(t.starts_with("ca"))
        self.assertEqual(t.words_with_prefix("car"), ["car", "care", "cart"])
        self.assertEqual(t.words_with_prefix("x"), [])


class TestLRUCache(unittest.TestCase):
    def test_eviction(self):
        c = LRUCache(2)
        c.put("a", 1)
        c.put("b", 2)
        self.assertEqual(c.get("a"), 1)  # a is now most recent
        c.put("c", 3)  # evicts b
        self.assertIsNone(c.get("b"))
        self.assertEqual(c.get("c"), 3)
        c.put("a", 10)
        self.assertEqual(c.get("a"), 10)
        self.assertEqual(len(c), 2)


class TestUnionFind(unittest.TestCase):
    def test_union_find(self):
        uf = UnionFind(5)
        self.assertTrue(uf.union(0, 1))
        self.assertTrue(uf.union(3, 4))
        self.assertFalse(uf.union(1, 0))
        self.assertTrue(uf.connected(0, 1))
        self.assertFalse(uf.connected(1, 3))
        self.assertEqual(uf.components, 3)


if __name__ == "__main__":
    unittest.main()
