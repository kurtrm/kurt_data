"""Test labeled property graph comprehensively."""

import pytest


@pytest.fixture
def labeled_property_graph():
    """Fixture of lpg for testing."""
    from labeled_property_graph import LabeledPropertyGraph
    lpg = LabeledPropertyGraph()
    return lpg

# ==================== Nodes ======================


def test_empty_lpg_nodes(labeled_property_graph):
    """Ensure it returns none if no nodes in lpg."""
    assert labeled_property_graph.nodes() == []


def test_empty_lpg_relationships(labeled_property_graph):
    """Ensure it returns none if no relationships."""
    assert labeled_property_graph.nodes() == []


def test_adding_node(labeled_property_graph):
    """Ensure we can successfully add nodes to lpg."""
    labeled_property_graph.add_node('Kurt')
    labeled_property_graph.nodes() == ['Kurt']


def test_adding_node_error(labeled_property_graph):
    """Ensure error raised if node already exists."""
    labeled_property_graph.add_node('Kurt')
    with pytest.raises(KeyError):
        labeled_property_graph.add_node('Kurt')


# def test_removing_node_from_empty(labeled_property_graph):
#     """Ensure we get error when removing from empty lpg."""
#     with pytest.raises(ValueError):
#         labeled_property_graph.remove_node('Kurt')

# ================== Relationsihps ================


def test_adding_rel_to_empty_lpg(labeled_property_graph):
    """Ensure we can't add relationships between nonexistent nodes."""
    with pytest.raises(KeyError):
        labeled_property_graph.add_relationship('durka', 'Will', 'Bill')


def test_adding_rel_one_node_dne(labeled_property_graph):
    """Ensure we can add relationships between existent and non-existent."""
    labeled_property_graph.add_node('Kurt')
    with pytest.raises(KeyError):
        labeled_property_graph.add_relationship('durka', 'Kurt', 'Bill')


def test_adding_rel_other_dne(labeled_property_graph):
    """Ensure second parameter works as well."""
    labeled_property_graph.add_node('Billy')
    with pytest.raises(KeyError):
        labeled_property_graph.add_relationship('durka', 'Kurt', 'Billy')


def test_adding_rel_success(labeled_property_graph):
    """Ensure successful of adding a relationship."""
    labeled_property_graph.add_node('Kurt')
    labeled_property_graph.add_node('Meliss')
    labeled_property_graph.add_relationship('rel', 'Kurt', 'Meliss')
    assert labeled_property_graph.unique_relationships() == ['rel']


def test_adding_rel_success_view(labeled_property_graph):
    """Ensure we can see the relationship as a key in the dict."""
    labeled_property_graph.add_node('Kurt')
    labeled_property_graph.add_node('Meliss')
    labeled_property_graph.add_relationship('rel', 'Kurt', 'Meliss')
    assert labeled_property_graph._graph['Kurt'] == {'rel': 'Meliss'}
