def add_relationship(self, name, node_a, node_b):
    """Refactored add_relatinship for EAFP."""
    nodes = self.nodes()
    if self._relationship[name][node_a].get(node_b):
        raise ValueError('Relationship already exists between nodes')
    elif node_a in nodes or node_b in nodes:
        raise KeyError('A node is not present in this graph')
    try:
        self._relationship[name][node_a][node_b] = Relationship(name)
    except KeyError as key:
        if key == name:
            self._relationships[name] = {node_a: {node_b: Relationship(name)}}
        elif key == node_a:
            self._relationship[name][node_a] = {node_b: Relationship(name)}
        else:
            self._relationship[name][node_a][node_b] = Relationship(name)
    try:
        self._graph[node_a][node_b].append(name)
    except AttributeError:
        curr_rel = self._graph[node_a][node_b]
        self._graph[node_a][node_b] = [curr_rel, name]
    except KeyError:
        self._graph[node_a][node_b] = name
