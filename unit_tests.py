import pytest
from Stack import Stack
from PriorityQueue import PriorityQueue
from LinkedList import LinkedList
from Graph import Graph
from Tree import BinarySearchTree

class TestStack:
    def test_pushing(self):
        stack = Stack()
        stack.push(3)
        stack.push(5)

    def test_len(self):
        stack = Stack()
        stack.push(4)
        stack.push(5)
        assert len(stack) == 2
        stack.pop()
        assert len(stack) == 1
        stack.pop()
        assert len(stack) == 0
        assert stack.is_empty()

    def test_popping(self):
        stack = Stack()
        stack.push(3)
        stack.push(5)
        stack.push(8)
        assert stack.pop() == 8
        assert stack.pop() == 5
        assert stack.pop() == 3
        

class TestPriorityQueue:
    def test_insertion(self):
        q = PriorityQueue()
        q.insert(4)
        q.insert(3)
        q.insert(7)
        assert q.pop() == 7
        assert q.pop() == 4
        assert q.pop() == 3

    def test_function(self):
        q = PriorityQueue(f=lambda x: -x)
        q.insert(4)
        q.insert(3)
        q.insert(7)
        assert q.pop() == 3
        assert q.pop() == 4
        assert q.pop() == 7

    def test_len(self):
        q = PriorityQueue(f=lambda x: -x)
        q.insert(4)
        q.insert(3)
        q.insert(7)
        assert len(q) == 3
        q.pop()
        assert len(q) == 2
        q.pop()
        q.pop()
        assert len(q) == 0
        assert q.is_empty()

class TestLinkedList:
    def test_insertion(self):
        a = LinkedList()
        a.add(4)
        a.add(3)
        a.add(2)
        assert a.pop() == 2
        assert a.pop() == 3
        assert a.pop() == 4

    def test_len(self):
        a = LinkedList()
        a.add(4)
        a.add(3)
        a.add(2)
        assert len(a) == 3
        a.pop(); a.pop()
        assert len(a) == 1
        a.pop()
        assert len(a) == 0
        assert a.is_empty()

class TestGraph:
    def test_node_insertion(self):
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        assert "A" in g.connections
        assert "B" in g.connections

    def test_edge_insertion(self):
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("B", "A")
        assert g.connections["A"] == ["B"]
        assert g.connections["B"] == ["A"]

    def test_weighted_edge_insertion(self):
        g = Graph(weighted=True)
        g.add_weighted_edge("A", "B", 4.0)
        g.add_weighted_edge("B", "A", 5.0)
        assert g.connections["A"] == [(4.0, "B")]
        assert g.connections["B"] == [(5.0, "A")]

    def test_mark(self):
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("B", "A")
        g.mark("B")
        assert g.is_marked("B")

    def test_len(self):
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("B", "A")
        g.add_edge("B", "C")
        assert len(g) == 3

    def test_tuples(self):
        g = Graph()
        g.add_edge(("A", 1), ("B", 2))
        g.add_edge(("B", 2), ("A", 1))
        g.add_edge(("C", 3), ("B", 2))
        assert g.connections[("A", 1)] == [("B", 2)]
        assert g.connections[("B", 2)] == [("A", 1)]
        assert g.connections[("C", 3)] == [("B", 2)]

class TestBinarySearchTree:
    def test_height(self):
        t = BinarySearchTree()
        t.insert(3)
        t.insert(4)
        t.insert(2)
        t.insert(1)
        assert t.height() == 3

    def test_len(self):
        t = BinarySearchTree()
        t.insert(1)
        t.insert(4)
        t.insert(9)
        t.insert(1)
        assert len(t) == 4

    def test_pop(self):
        t = BinarySearchTree()
        t.insert(1)
        t.insert(4)
        t.insert(9)
        print(t.root.right)
        assert t.pop() == 9
        assert t.pop() == 4
        assert len(t) == 2

    def test_insert(self):
        t = BinarySearchTree()
        t.insert(4)
        t.insert