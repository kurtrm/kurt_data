"""
Implementation of a labeled property graph.

Note that classes are fine to be keys in a dictionary, so the
graph itself is going to be a dictionary with Node class objects
as keys.
"""


class Node:
    """Node object that will have a relationship to other nodes."""

    def __init__(self, name):
        """Initialized nodes contain properties and methods to view them."""
        self.name = name
        self.properties = {}

    def add_property(self, property_, value):
        """Method to add a property to a node."""
        if property_ in self.properties:
            raise KeyError("Property already exists, use change_property()"
                           "to alter property value")
        self.properties[property_] = value

    def change_property(self, property_, value):
        """Method to alter a value on a property."""
        if property_ not in self.properties:
            raise KeyError("Property does not exist, use add_property()"
                           "to add a property")
        self.properties[property_] = value

    def remove_property(self, property_):
        """Method to remove a property from a node."""
        if property_ not in self.properties:
            raise KeyError("Node does not contain that property")
        del self.properties[property_]


class Relationship:
    """Relationship object that will be able to have properties as well."""

    def __init__(self, name):
        """Initialize relationships as to contain properites like nodes."""
        self.name = name
        self.properties = {}

    def add_property(self, property_, value):
        """Method to add a property to a node."""
        if property_ in self.properties:
            raise KeyError("Property already exists, use change_property()"
                           "to alter property value")
        self.properties[property_] = value

    def change_property(self, property_, value):
        """Method to alter a value on a property."""
        if property_ not in self.properties:
            raise KeyError("Property does not exist, use add_property()"
                           "to add a property")
        self.properties[property_] = value

    def remove_property(self, property_):
        """Method to remove a property from a node."""
        if property_ not in self.properties:
            raise KeyError("Node does not contain that property")
        del self.properties[property_]


class LabeledPropertyGraph:
    """Define a labeled property graph as dictionary composition."""

    def __init__(self):
        """Initialize the graph as a dictionary."""
        self._graph = {}
        self._nodes = {}
        self._relationships = {}

    def nodes(self):
        """Return a list of nodes in the graph."""
        return [node for node in self._nodes.keys()]

    def unique_relationships(self):
        """Return list of unique relationships."""
        #  This will likely not return what I'm looking for.
        return [relationship for relationship in self._relationships.keys()]

    def add_node(self, name):
        """Add a node and pass the name to the node.name."""
        if name in self.nodes():
            raise KeyError('Node already exists in graph')
        node = Node(name)
        self._graph[name] = {}
        self._nodes[name] = node

    def add_relationship(self, name, node_a, node_b, both_ways=False):
        """Refactored add_relationship for EAFP."""
        nodes = self.nodes()
        if node_a not in nodes or node_b not in nodes:
            raise KeyError('A node is not present in this graph')

        def add(rel, a, b):
            """Local function to perform operation."""
            try:
                if self._relationships[rel][a].get(b):
                    raise ValueError('{} -> {} relationship'
                                     'already exists'.format(a, b))
                self._relationships[rel][a][b] = Relationship(rel)
            except KeyError as key_errors:
                key = key_errors.args[0]
                if key == rel:
                    self._relationships[rel] = {
                        a: {
                            b: Relationship(rel)
                        }
                    }
                elif key == a:
                    self._relationships[rel][a] = {
                        b: Relationship(rel)
                    }
            try:
                self._graph[a][b].append(rel)
            except AttributeError:
                curr_rel = self._graph[a][b]
                self._graph[a][b] = [curr_rel, rel]
            except KeyError:
                self._graph[a][b] = rel

        add(name, node_a, node_b)
        if both_ways:
            add(name, node_b, node_a)

    def remove_relationship(self, name, node_a, node_b):
        """Remove a relationship between two nodes."""
        del self._relationships[name][node_a][node_b]
        try:
            self._graph[node_a][node_b].remove(name)
        except AttributeError:
            del self._graph[node_a][node_b]

    def remove_node(self, name):
        """Remove a node and all of its relationships."""
        for relationship in self._relationships:
            try:
                del self._relationships[relationship][name]
            except KeyError:
                continue
            for node_a in relationship:
                del self._relationship[node_a][name]
        del self._graph[name]
        #  The following needs to be refactored, as it would be computationally
        #  expensive to iterate over all of the nodes in a possibly huge graph.
        for node in self._graph:
            try:
                del self._graph[node][name]
            except KeyError:
                continue

    def get_relationships(self, node_a, node_b):
        """Return all relationships between two nodes."""
        return self._graph[node_a][node_b]

    def nodes_with_relationship(self, name):
        """Return all nodes with a given relationship."""
        return list(self._relationships[name].keys())

    def get_neighbors(self, node):
        """Return all nodes node has relationships with."""
        return list(self._graph[node].keys())

    def get_relationship_properties(self, name, node_a, node_b):
        """Return properties of a relationship between two nodes."""
        return self._relationship[name][node_a][node_b].properties()

    def get_node_properties(self, name):
        """Return properties of a node."""
        return list(self._nodes[name].properties.keys())

    def has_neighbor(self, node_a, node_b):
        """Return boolean whether a node has a certain neighbor."""
        try:
            return node_b in self._graph[node_a]
        except KeyError:
            raise KeyError('{} not in graph'.format(node_a))

    def has_relationship(self, node_a, node_b, relationship, both_ways=False):
        """Return whether node_a has a given rel to node_b or vice_versa."""
        if both_ways:
            return relationship in self._graph[node_a][node_b] \
                and relationship in self._graph[node_b][node_a]
        return relationship in self._graph[node_a][node_b]

    def change_node_property(self, property_, node):
        """Change the property of a node."""
        pass

    def change_relationship_property(self, property_, node):
        """Change the property of a relationship."""
        pass


# TODO: Traversals
# TODO: Add an option make a relationship bi-directional betwen two nodes
