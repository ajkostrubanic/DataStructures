from typing import Any

class Queue:
    def __init__(self) -> None:
        self.elements = []

    def __repr__(self) -> str:
        return f"Queue({str(self.elements)[1:-1]})"
    
    def __len__(self) -> int:
        return len(self.elements)
    
    def is_empty(self) -> bool:
        return bool(self.elements)

    def enqueue(self, value: Any) -> None:
        self.elements.append(value)

    def dequeue(self) -> Any:
        result = self.elements[0]
        del self.elements[0]
        return result