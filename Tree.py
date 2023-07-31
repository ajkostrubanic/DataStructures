from typing import Optional

class Node:
    def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node(value={self.value}, left={self.left}, right={self.right})"

    def _insert(self, value: int):
        if self.value > value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left._insert(value)
        if self.value <= value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right._insert(value)

    def _height(self) -> int:
        l,r = 0,0
        if self.left is not None:
            l += self.left._height()
        if self.right is not None:
            r += self.right._height()
        return max(l, r) + 1
    
    def _size(self) -> int:
        l,r = 0,0
        if self.left is not None:
            l += self.left._size()
        if self.right is not None:
            r += self.right._size()
        return l + r + 1

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: 'Node' = None

    def __repr__(self) -> str:
        return f"BinarySearchTree(root={self.root})"

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self.root._insert(value)

    def __len__(self) -> int:
        return self.root._size()
    
    def height(self) -> int:
        return self.root._height()