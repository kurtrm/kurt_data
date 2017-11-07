"""Test labeled property graph comprehensively."""

import pytest


@pytest.fixture
def lpg():
    """Fixture of labeled property graph(lpg) for testing."""
    from kurt_data.scripts.labeled_property_graph import LabeledPropertyGraph
    lpg = LabeledPropertyGraph()
    return lpg

# ==================== Nodes ======================


def test_empty_lpg_nodes(lpg):
    """Ensure it returns none if no nodes in lpg."""
    assert lpg.nodes() == []


def test_empty_lpg_relationships(lpg):
    """Ensure it returns none if no relationships."""
    assert lpg.nodes() == []


def test_adding_node(lpg):
    """Ensure we can successfully add nodes to lpg."""
    lpg.add_node('Kurt')
    lpg.nodes() == ['Kurt']


def test_adding_node_error(lpg):
    """Ensure error raised if node already exists."""
    lpg.add_node('Kurt')
    with pytest.raises(KeyError):
        lpg.add_node('Kurt')


# def test_removing_node_from_empty(lpg):
#     """Ensure we get error when removing from empty lpg."""
#     with pytest.raises(ValueError):
#         lpg.remove_node('Kurt')

# ================== Relationsihps ================


def test_adding_rel_to_empty_lpg(lpg):
    """Ensure we can't add relationships between nonexistent nodes."""
    with pytest.raises(KeyError):
        lpg.add_relationship('durka', 'Will', 'Bill')


def test_adding_rel_one_node_dne(lpg):
    """Ensure we can add relationships between existent and non-existent."""
    lpg.add_node('Kurt')
    with pytest.raises(KeyError):
        lpg.add_relationship('durka', 'Kurt', 'Bill')


def test_adding_rel_other_dne(lpg):
    """Ensure second parameter works as well."""
    lpg.add_node('Billy')
    with pytest.raises(KeyError):
        lpg.add_relationship('durka', 'Kurt', 'Billy')


def test_adding_rel_success(lpg):
    """Ensure successful of adding a relationship."""
    lpg.add_node('Kurt')
    lpg.add_node('Meliss')
    lpg.add_relationship('rel', 'Kurt', 'Meliss')
    assert lpg.unique_relationships() == ['rel']


# def test_adding_rel_success_view(lpg):
#     """Ensure we can see the relationship as a key in the dict."""
#     lpg.add_node('Kurt')
#     lpg.add_node('Meliss')
#     lpg.add_relationship('rel', 'Kurt', 'Meliss')
#     assert (lpg._graph['Kurt'],
#             lpg._relationships['rel']['Kurt']['Meliss'].name) == ({'rel': 'Meliss'}, 'rel')

def test_adding_rel_success_view(lpg):
    """Ensure we can see the relationship as a key in the dict."""
    lpg.add_node('Kurt')
    lpg.add_node('Meliss')
    lpg.add_relationship('rel', 'Kurt', 'Meliss')
    assert (lpg._graph['Kurt'],
            lpg._relationships['rel']['Kurt']['Meliss'].name) == ({'Meliss': 'rel'}, 'rel')


# def test_adding_rel_with_other_rels(lpg):
#     """Ensure we can add to a list of rels in _graph."""
#     lpg.add_node('Kurt')
#     lpg.add_node('Meliss')
#     lpg.add_node('Mom')
#     lpg.add_relationship('rel', 'Kurt', 'Meliss')
#     lpg.add_relationship('rel', 'Kurt', 'Mom')
#     graph_key = lpg._graph['Kurt']
#     rel_node = lpg._relationships['rel']['Kurt']['Meliss']
#     assert (graph_key,
#             rel_node.name) == ({'rel': ['Meliss', 'Mom']}, 'rel')


def test_adding_rel_with_other_rels(lpg):
    """Ensure we can add to a list of rels in _graph."""
    lpg.add_node('Kurt')
    lpg.add_node('Meliss')
    lpg.add_node('Mom')
    lpg.add_relationship('rel', 'Kurt', 'Meliss')
    lpg.add_relationship('rel', 'Kurt', 'Mom')
    graph_key = lpg._graph['Kurt']
    rel_node = lpg._relationships['rel']['Kurt']['Meliss']
    assert (graph_key,
            rel_node.name) == ({'Meliss': 'rel', 'Mom': 'rel'}, 'rel')
