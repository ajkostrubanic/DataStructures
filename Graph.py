from collections import defaultdict
from typing import Optional, Any, Iterator

class Graph:
    """
    Graph implementation: directed, and can be weighted or unweighted.
    """
    def __init__(self, weighted: Optional[bool] = False) -> None:
        self.connections = {}
        self.size = 0
        self.weighted = weighted
        self.marked = defaultdict(lambda: False)

    def __repr__(self) -> str:
        return f"Graph({str(self.connections)[1:-1]})"
    
    def add_node(self, node: Any) -> None:
        if node not in self.connections:
            self.connections[node] = []

    def add_edge(self, ni: Any, nf: Any) -> None:
        self.add_node(ni)
        self.add_node(nf)
        self.connections[ni].append(nf)

    def add_weighted_edge(self, ni: Any, nf: Any, weight: int) -> None:
        if not self.weighted:
            raise Exception("Unweighted graph being given weighted edges")
        self.add_node(ni)
        self.add_node(nf)
        self.connections[ni].append((weight, nf))

    def get_weight(self, ni: Any, nf: Any) -> int:
        adjacent = self.connections[ni]
        for weight, nk in adjacent:
            if nk == nf:
                return weight
            
    def mark(self, node: Any) -> None:
        self.marked[node] = True

    def is_marked(self, node: Any) -> bool:
        return self.marked[node]
    
    def get_adjacent(self, node: Any) -> Iterator[Any]:
        if self.weighted:
            for weight, ni in self.connections[node]:
                yield ni
        else:
            return iter(self.connections[node])