from typing import Any, Callable, List

class Queue:
    """
    Max Priority Queue implementation.
    """
    def __init__(self, f: Callable[[Any], Any] = None) -> None:
        self.heap = []
        if f is None:
            self.f = lambda x: x
        else:
            self.f = f

    def __repr__(self) -> str:
        return f"MaxQueue({str(self.heap)[1:-1]})"

    def __getitem__(self, i: int) -> Any:
        return self.heap[i]
    
    def __setitem__(self, i: int, value: Any) -> None:
        print("index ", i)
        self.heap[i] = value

    def __delitem__(self, value) -> None:
        del self.heap[value]

    def __len__(self) -> int:
        return len(self.heap)

    def _heapify(self, i: int) -> None:
        size = len(self)
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < size and self.f(self[i]) < self.f(self[l]):
            largest = l
        if r < size and self.f(self[largest]) < self.f(self[r]):
            largest = r
        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self._heapify(largest)

    def insert(self, value: Any) -> None:
        size = len(self)
        self.heap.append(value)
        for i in range((size // 2), -1, -1):
            print("heapify", i)
            self._heapify(i)

    def delete(self, value: Any) -> None:
        size = len(self)
        i = self.heap.index(value)
        self[i], self[size - 1] = self[size - 1], self[i]
        del self.heap[size - 1]

        for i in range((size // 2) - 1, -1, -1):
            self._heapify(i)
            
    def pop(self) -> Any:
        result = self.heap[0]
        self.delete(result)
        return result