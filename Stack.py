from typing import Iterator, Any

class Stack:
    """
    A simple LIFO stack implementation.
    """
    def __init__(self) -> None:
        self.stack = []

    def __repr__(self) -> str:
        return f"Stack({str(self.stack)[1:-1]})"
    
    def __len__(self) -> int:
        return len(self.stack)
    
    def __iter__(self) -> Iterator[Any]:
        """Yields values in reverse order; exhausts the stack of all values."""
        while self.stack:
            yield self.pop()

    def is_empty(self) -> bool:
        return bool(self.stack)

    def push(self, value: Any):
        """Push a value to the top of the stack."""
        self.stack.append(value)

    def pop(self) -> Any:
        """Pop a value off the top of the stack."""
        return self.stack.pop()
    
    def peek(self) -> Any:
        """See what value is at the top of the stack."""
        return self.stack[-1]