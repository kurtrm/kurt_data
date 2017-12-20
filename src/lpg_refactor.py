"""
Refactor of lpg to implement some more advanced class attributes
for simplicity. Particularly:
    Nodes:
        - __getitem__ to return properties
        - Format the repr and str methods.

    Relationships:
        - __getitem__ to return properties
        - I thought briefly about throwing nodes and relationships in the same dict,
          but I'm going to keep these separate for now.

    LPG:
        - Relationship keys will now be a tuple. So lpg['Kurt', 'Melissa'] will return
        the dictionary of relationships between the two nodes.
        - Modify __getitem__ to return either nodes or relationships
        - Implement __iter__
        - Define a property method for size, as well as a setter
        - Make it so that nodes can be added from iterables
        - Make it so relationships can be added from iterables
"""


class Node:
    """Node object that will have a relationship to other nodes."""

    def __init__(self, name):
        """Initialized nodes contain properties and methods to view them."""
        self.name = name
        self._properties = {}
        self.labels = []

    def __getitem__(self, key):
        """Get node properties."""
        return self._properties[key]

    def __setitem__(self, key, item):
        """Change or add node properties."""
        self._properties[key] = item

    def __delitem__(self, key):
        """Remove a property from the node."""
        del self._properties[key]

    def add_label(self, label):
        """Adds a label to the node."""
        if label in self.labels:
            raise ValueError('Label already set on node.')
        self.labels.append(label)

    def remove_label(self, label):
        """Removes a label from a node."""
        self.labels.remove(label)

    @property
    def properties(self):
        """Return the keys in self._properties."""
        return list(self._properties.keys())

    def __repr__(self):
        """Show the properties of the node."""
        props = """
-----------
Name: {}
-----------
Properties (key: value)
""".format(self.name)
        for key, value in self._properties.items():
            props += '\r{}: {}'.format(key, value)
        props += '\r\n\r\n-----------\rLabels: '
        props += ', '.join(self.labels)
        props += '\r\n\r\n'
        return props

    def __str__(self):
        """Return the same thing as repr."""
        return self.__repr__()


class Relationship:
    """Relationship object that will be able to have properties as well."""

    def __init__(self, name):
        """Initialize relationships as to contain properites like nodes."""
        self.name = name
        self._properties = {}
        self.labels = []

    def __getitem__(self, key):
        """Get node properties."""
        return self._properties[key]

    def __setitem__(self, key, item):
        """Change or add node properties."""
        self._properties[key] = item

    def __delitem__(self, key):
        """Remove a property from the node."""
        del self._properties[key]

    def add_label(self, label):
        """Adds a label to the node."""
        if label in self.labels:
            raise ValueError('Label already set on relationship.')
        self.labels.append(label)

    def remove_label(self, label):
        """Removes a label from a node."""
        self.labels.remove(label)

    @property
    def properties(self):
        """Return the keys in self._properties."""
        return list(self._properties.keys())

    def __repr__(self):
        """Show the properties of the node."""
        props = """
-----------
Name: {}
-----------
Properties (key: value)
""".format(self.name)
        for key, value in self._properties.items():
            props += '\r{}: {}'.format(key, value)
        props += '\r\n\r\n-----------\rLabels: '
        props += ', '.join(self.labels)
        props += '\r\n\r\n'
        return props

    def __str__(self):
        """Return the same thing as repr."""
        return self.__repr__()


class LabeledPropertyGraph:
    """Define a labeled property graph as dictionary composition."""

    def __init__(self):
        """Initialize the graph as a dictionary."""
        self._graph = {}
        self._nodes = {}
        self._relationships = {}

    def __getitem__(self, key):
        """Return either node or relationship."""
        if isinstance(key, tuple):
            return self._relationships[key]
        return self._nodes[key]

    def __setitem__(self, key, item):
        """Modify or create new nodes or relationships.
           Warning: passing a tuple into the subscript will
           create new relationship, not node."""
        if isinstance(key, tuple):
            if not isinstance(item, Relationship):
                raise ValueError("Graph relationships must"
                                 "be of type Relationship")
            self._relationships[key] = item
        else:
            if not isinstance(item, Node):
                raise ValueError("Graph nodes must"
                                 "be of type Node")
            self._nodes[key] = item
