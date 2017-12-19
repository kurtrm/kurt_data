"""
Refactor of lpg to implement some more advanced class attributes
for simplicity. Particularly:
    Nodes:
        - __getitem__ to return properties
        - Format the repr and str methods.

    Relationships:
        - __getitem__ to return properties
        - Keys will now be a tuple. So lpg['Kurt', 'Melissa'] will return
        the dictionary of relationships between the two nodes.
        - I thought briefly about throwing nodes and relationships in the same dict,
          but I'm going to keep these separate for now.

    LPG:
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
        self.properties = {}
        self.labels = []

    def __getitem__(self, key):
        """Get node properties."""
        return self.properties[key]

    def __setitem__(self, key, item):
        """Change or add node properties."""
        self.properties[key] = item


    def add_property(self, property_, value):
        """Method to add a property to a node."""
        if property_ in self.properties:
            raise KeyError("Property already exists, use change_property()"
                           "to alter property value")
        self.properties[property_] = value

    def change_property(self, property_, value):
        """Method to alter a value on a property."""
        if property_ not in self.properties:
            raise AttributeError("Property does not exist, use add_property()"
                                 "to add a property")
        self.properties[property_] = value

    def remove_property(self, property_):
        """Method to remove a property from a node."""
        if property_ not in self.properties:
            raise AttributeError("Node does not contain that property")
        del self.properties[property_]

    def add_label(self, label):
        """Adds a label to the node."""
        if label in self.labels:
            raise ValueError('Label already set on node.')
        self.labels.append(label)

    def remove_label(self, label):
        """Removes a label from a node."""
        self.labels.remove(label)

    def __repr__(self):
        """Show the properties of the node."""
        props = "Name: {}\nProperties:".format(self.name)
        for key, value in self.properties.items():
            props += '\r{}: {}'.format(key, value)
        return props

