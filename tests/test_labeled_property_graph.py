"""Test labeled property graph comprehensively."""

from faker import Faker
import pytest


@pytest.fixture
def lpg():
    """Fixture of labeled property graph(lpg) for testing."""
    from kurt_data.scripts.labeled_property_graph import LabeledPropertyGraph
    lpg = LabeledPropertyGraph()
    return lpg


@pytest.fixture
def loaded_lpg():
    """Fixture of a loaded lpg."""
    from kurt_data.scripts.labeled_property_graph import LabeledPropertyGraph
    lpg = LabeledPropertyGraph()
    lpg.add_node('Charlie')
    lpg.add_node('Unicorn')
    lpg.add_node('Pegasus')
    lpg.add_relationship('buddies', 'Charlie', 'Unicorn', both_ways=True)
    lpg.add_relationship('cousins', 'Charlie', 'Unicorn')

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
    assert lpg.nodes() == ['Kurt']


def test_adding_lots_of_nodes(lpg):
    """Ensure we can put a lot of nodes in the graph."""
    names = [Faker().name() for _ in range(20)]
    names.append(3451)
    names.append(3.21)
    names.append(None)
    for name in names:
        lpg.add_node(name)
    for name in names:
        assert name in lpg.nodes()


def test_adding_lots_of_nodes_2(lpg):
    """Ensure we can put a lot of nodes in the graph."""
    names = [Faker().name() for _ in range(20)]
    names.append(3451)
    names.append(3.21)
    names.append(None)
    for name in names:
        lpg.add_node(name)
    for name in lpg.nodes():
        assert name in names


def test_adding_node_error(lpg):
    """Ensure error raised if node already exists."""
    lpg.add_node('Kurt')
    with pytest.raises(KeyError):
        lpg.add_node('Kurt')


def test_removing_node_from_empty(lpg):
    """Ensure we get error when removing from empty lpg."""
    with pytest.raises(KeyError):
        lpg.remove_node('Kurt')


def test_removing_nodes_with_many_connections(loaded_lpg):
    """Ensure relationships to deleted node are cleared."""
    loaded_lpg.add_node('Wendy')
    for node in ['Charlie', 'Unicorn', 'Pegasus']:
        loaded_lpg.add_relationship('friends', 'Wendy', node)
    for rel, node in zip(['boss', 'parent', 'administrator'], ['Charlie', 'Unicorn', 'Pegasus']):
        loaded_lpg.add_relationship(rel, node, 'Wendy')
    loaded_lpg.remove_node('Wendy')
    for rel in loaded_lpg._relationships:
        assert 'Wendy' not in loaded_lpg._relationships[rel]


# def test_removing_nodes_with_additional_conns(loaded_lpg):
#     """Ensure the relationship dict is changed appropriately."""
#     loaded_lpg.add_node('Wendy')
#     for node in ['Charlie', 'Unicorn', 'Pegasus']:
#         loaded_lpg.add_relationship('friends', 'Wendy', node)
#     for rel, node in zip(['boss', 'parent', 'administrator'], ['Charlie', 'Unicorn', 'Pegasus']):
#         loaded_lpg.add_relationship(rel, node, 'Wendy')
#     loaded_lpg.remove_node('Wendy')
    

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


def test_adding_rel_success_view(lpg):
    """Ensure we can see the relationship as a key in the dict."""
    lpg.add_node('Kurt')
    lpg.add_node('Meliss')
    lpg.add_relationship('rel', 'Kurt', 'Meliss')
    assert (lpg._graph['Kurt'],
            lpg._relationships['rel']['Kurt']['Meliss'].name) == ({'Meliss': 'rel'}, 'rel')


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


def test_adding_existent_rel(lpg):
    """Ensure we get the proper key erro."""
    lpg.add_node('Charlie')
    lpg.add_node('Unicorn')
    lpg.add_relationship('buddies', 'Charlie', 'Unicorn')
    with pytest.raises(ValueError):
        lpg.add_relationship('buddies', 'Charlie', 'Unicorn')


def test_adding_existent_rel_both_ways(lpg):
    """Ensure we get the proper key erro."""
    lpg.add_node('Charlie')
    lpg.add_node('Unicorn')
    lpg.add_relationship('buddies', 'Charlie', 'Unicorn')
    with pytest.raises(ValueError):
        lpg.add_relationship('buddies', 'Charlie', 'Unicorn', both_ways=True)


def test_adding_both_ways_success_graph(lpg):
    """Ensure successful both ways relationship add."""
    lpg.add_node('Charlie')
    lpg.add_node('Unicorn')
    lpg.add_relationship('buddies', 'Charlie', 'Unicorn', both_ways=True)
    assert lpg._graph['Charlie']['Unicorn'] == lpg._graph['Unicorn']['Charlie']


def test_adding_both_ways_success_rels(lpg):
    """Ensure successful both ways relationship add."""
    lpg.add_node('Charlie')
    lpg.add_node('Unicorn')
    lpg.add_relationship('buddies', 'Charlie', 'Unicorn', both_ways=True)
    assert lpg._relationships['buddies']['Charlie']['Unicorn'].name == lpg._relationships['buddies']['Unicorn']['Charlie'].name


def test_coniditionals_in_add_rels(lpg):
    """Ensure we successfully add rels b/w nodes."""
    lpg.add_node('Charlie')
    lpg.add_node('Unicorn')
    lpg.add_node('Pegasus')
    lpg.add_relationship('buddies', 'Charlie', 'Unicorn', both_ways=True)
    lpg.add_relationship('buddies', 'Charlie', 'Pegasus')
    assert lpg._graph['Charlie']['Pegasus'] == lpg._relationships['buddies']['Charlie']['Pegasus'].name


def test_adding_another_rel_between_nodes(lpg):
    """Ensure we except attribute error."""
    lpg.add_node('Charlie')
    lpg.add_node('Unicorn')
    lpg.add_node('Pegasus')
    lpg.add_relationship('buddies', 'Charlie', 'Unicorn', both_ways=True)
    lpg.add_relationship('cousins', 'Charlie', 'Unicorn')
    assert lpg._graph['Charlie']['Unicorn'][1] == lpg._relationships['cousins']['Charlie']['Unicorn'].name


def test_removing_rel(loaded_lpg):
    """Ensure relationships can be removed."""
    loaded_lpg.remove_relationship('cousins', 'Charlie', 'Unicorn')
    assert loaded_lpg._graph['Charlie']['Unicorn'] == 'buddies'


def test_removing_rel_single(loaded_lpg):
    """Ensure relationships can be removed."""
    loaded_lpg.remove_relationship('cousins', 'Charlie', 'Unicorn')
    loaded_lpg.remove_relationship('buddies', 'Charlie', 'Unicorn')
    with pytest.raises(KeyError):
        loaded_lpg._graph['Charlie']['Unicorn'] == []




