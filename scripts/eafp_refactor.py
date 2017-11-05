def add_relationship(self, name, node_a, node_b):
    """Refactored add_relatinship for EAFP."""
    nodes = self.nodes()
    try:
        self._graph[node_a][node_b].append(name)
    except AttributeError:
        curr_rel = self._graph[node_a][node_b]
        self._graph[node_a][node_b] = [curr_rel, name]
    except KeyError as node:
        if node_a == node:
            raise KeyError('{} not present in graph'.format(node))
