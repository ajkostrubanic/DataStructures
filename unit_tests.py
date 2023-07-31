import pytest
from Stack import Stack
from PriorityQueue import PriorityQueue
from LinkedList import LinkedList
from Graph import Graph

class TestStack:
    def test_pushing(self):
        stack = Stack()
        stack.push(3)
        stack.push(5)

    def test_popping(self):
        stack = Stack()
        stack.push(3)
        stack.push(5)
        stack.push(8)
        assert stack.pop() == 8
        assert stack.pop() == 5
        assert stack.pop() == 3

    def test_is_empty(self):
        stack = Stack()
        assert stack.is_empty()
        stack.push(5)
        stack.pop()
        assert stack.is_empty()

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

class TestLinkedList:
    def test_insertion(self):
        a = LinkedList()
        a.add(4)
        a.add(3)
        a.add(2)
        assert a.pop() == 2
        assert a.pop() == 3
        assert a.pop() == 4
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