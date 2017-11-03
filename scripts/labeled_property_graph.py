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
        if name not in self.nodes():
            node = Node(name)
            self._graph[name] = {}
            self._nodes[name] = node
        else:
            raise KeyError('Node already exists in graph')

    def add_relationship(self, name, node_a, node_b):
        """Add a relationship between two nodes."""
        nodes = self.nodes()
        if node_a in nodes and node_b in nodes:
            relationship = Relationship(name)
            if self._graph[node_a].get(name):
                if isinstance(self._graph[node_a][name], list):
                    self._graph[node_a][name].append(node_b)
                else:
                    current_relationship = self._graph[node_a][name]
                    self._graph[node_a][name] = [current_relationship, node_b]
            else:
                self._graph[node_a][name] = node_b
            if self._relationships.get(name):
                if self._relationships[name].get(node_a):
                    if self._relationship[name][node_a].get(node_b):
                        raise ValueError('Relationship already exists'
                                         'between nodes')
                    else:
                        self._relationship[name][node_a][node_b] = relationship
                else:
                    self._relationship[name][node_a] = {node_b: relationship}
            else:
                self._relationships[name] = {node_a: {node_b: relationship}}
        else:
            raise KeyError('Node not in graph')  # More description

    def remove_relationship(self, name, node_a, node_b):
        """Remove a relationship between two nodes."""
        pass

    def remove_node(self, name):
        """Remove a node and all of its relationships."""
        pass

    def get_relationships(self, node_a, node_b):
        """Return all relationships between two nodes."""
        pass

    def nodes_with_relationship(self, name):
        """Return all nodes with a given relationship."""
        pass

    def get_relationship_properties(self, name, node_a, node_b):
        """Return properties of a relationship between two nodes."""
        pass

    def get_node_properties(self, name):
        """Return properties of a node."""
        pass

# Traversals
# 