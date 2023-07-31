from typing import Any

class LinkedListNode:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return f"Node({self.value})"
    
    def get_next(self) -> 'LinkedListNode':
        return self.next
    
    def get_previous(self) -> 'LinkedListNode':
        return self.prev
    
    def _assign_next(self, node: 'LinkedListNode'):
        self.next = node

    def _assign_prev(self, node: 'LinkedListNode'):
        self.prev = node
    
class LinkedList:
    """
    Two-way linked list implementation.
    """
    def __init__(self) -> None:
        self.head = None
        self.rear = None
        self.size = 0

    def __repr__(self) -> str:
        return f"LinkedList(head={self.head}, rear={self.rear})"

    def add(self, value: Any):
        if self.head is None:
            self.head = LinkedListNode(value)
            self.rear = self.head
        else:
            node = LinkedListNode(value)
            self.rear._assign_next(node)
            node._assign_prev(self.rear)
            self.rear = node

    def get_head(self) -> LinkedListNode:
        return self.head
    
    def get_rear(self) -> LinkedListNode:
        return self.rear
    
    def pop(self) -> LinkedListNode:
        """Pop the last node off the linked list."""
        if self.rear is self.head:
            node = self.head
            self.rear = None
            self.head = None
            return node.value
        
        node = self.rear
        rear_p = self.rear.get_previous()
        rear_p._assign_next(None)
        self.rear = rear_p
        return node.value