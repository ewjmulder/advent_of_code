import pytest

from src.util.tree import Tree


@pytest.fixture
def test_tree() -> Tree:
    tree = Tree(name="root", data=0)
    child1 = Tree(name="child1", data=1)
    child2 = Tree(name="child2", data=2)
    child3 = Tree(name="child3", data=3)
    tree.add_child(child1)
    tree.add_child(child2)
    tree.add_child(child3)
    child1.add_child(Tree(name="child1_child1", data=11))
    child2.add_child(Tree(name="child2_child1", data=21))
    child2.add_child(Tree(name="child2_child2", data=22))
    child3.add_child(Tree(name="child3_child1", data=31))
    child3.add_child(Tree(name="child3_child2", data=32))
    child3_child3 = Tree(name="child3_child3", data=33)
    child3.add_child(child3_child3)
    child3_child3.add_child(Tree(name="child3_child3_child1", data=331))
    return tree


def test_hash():
    assert hash(Tree(name="test", data=1)) == hash(Tree(name="test", data=1))
    assert hash(Tree(name="test", data=1)) != hash(Tree(name="test", data=2))
    assert hash(Tree(name="test", data=1)) != hash(Tree(name="test2", data=1))


# __eq__ is tested enough in the tests below


def test_is_root(test_tree: Tree):
    assert test_tree.is_root()
    assert not test_tree.find_one_by_name("child1").is_root()
    assert not test_tree.find_one_by_name("child1_child1").is_root()


def test_is_leaf(test_tree: Tree):
    assert not test_tree.is_leaf()
    assert not test_tree.find_one_by_name("child1").is_leaf()
    assert test_tree.find_one_by_name("child1_child1").is_leaf()


def test_add_child(test_tree: Tree):
    test_tree.add_child(Tree(name="child4"))
    assert len(test_tree.children) == 4
    assert test_tree.find_one_by_name("child4") == Tree(name="child4")


def test_depth(test_tree: Tree):
    assert test_tree.depth() == 4
    assert test_tree.find_one_by_name("child1").depth() == 2
    assert test_tree.find_one_by_name("child3").depth() == 3
    assert test_tree.find_one_by_name("child3_child3_child1").depth() == 1


def test_find_one_by_name(test_tree: Tree):
    assert test_tree.find_one_by_name("child2_child1").name == "child2_child1"


def test_find_all_by_name(test_tree: Tree):
    test_tree.add_child(Tree(name="child1"))
    assert len(test_tree.find_all_by_name("child1")) == 2


def test_get_nodes_at_level(test_tree: Tree):
    assert [tree.name for tree in test_tree.get_nodes_at_level(1)] == ["root"]
    assert [tree.name for tree in test_tree.get_nodes_at_level(2)] == ["child1", "child2", "child3"]
    assert [tree.name for tree in test_tree.get_nodes_at_level(4)] == ["child3_child3_child1"]
    assert [tree.name for tree in test_tree.get_nodes_at_level(5)] == []


def test_to_list_prefix(test_tree: Tree):
    assert [tree.name for tree in test_tree.to_list_prefix()] == [
        "root", "child1", "child1_child1", "child2", "child2_child1", "child2_child2",
        "child3", "child3_child1", "child3_child2", "child3_child3", "child3_child3_child1"
    ]


def test_to_list_postfix(test_tree: Tree):
    assert [tree.name for tree in test_tree.to_list_postfix()] == [
        "child1_child1", "child1", "child2_child1", "child2_child2", "child2",
        "child3_child1", "child3_child2", "child3_child3_child1", "child3_child3", "child3", "root"
    ]


def test_flatten(test_tree: Tree):
    assert test_tree.flatten() == test_tree.to_list_prefix()


def test_flatten_name(test_tree: Tree):
    assert test_tree.flatten_name() == [
        "root", "child1", "child1_child1", "child2", "child2_child1", "child2_child2",
        "child3", "child3_child1", "child3_child2", "child3_child3", "child3_child3_child1"
    ]


def test_flatten_data(test_tree: Tree):
    assert test_tree.flatten_data() == [
        0, 1, 11, 2, 21, 22, 3, 31, 32, 33, 331
    ]


def test_recurse(test_tree: Tree):
    assert test_tree.recurse(lambda child: child.data) == [1, 2, 3]


def test_flat_rec(test_tree: Tree):
    assert test_tree.flat_rec(lambda child: [child.data]) == [1, 2, 3]


def test_map_data_to_data(test_tree: Tree):
    assert test_tree.map_data_to_data(lambda data: data + 1000).flatten_data() == [
        1000, 1001, 1011, 1002, 1021, 1022, 1003, 1031, 1032, 1033, 1331
    ]


def test_map_tree_to_data(test_tree: Tree):
    assert test_tree.map_tree_to_data(lambda tree: tree.data + 1000) == \
           test_tree.map_data_to_data(lambda data: data + 1000)


def test_map_tree_to_name_and_data(test_tree: Tree):
    assert test_tree.map_tree_to_name_and_data(lambda tree: (tree.name, tree.data + 1000)) == \
           test_tree.map_data_to_data(lambda data: data + 1000)


def test_map_tree_to_tree(test_tree: Tree):
    assert test_tree.map_tree_to_tree(lambda tree: Tree(name=tree.name, data=tree.data + 1000)) == \
           test_tree.map_data_to_data(lambda data: data + 1000)


def test_to_string_node(test_tree: Tree):
    assert test_tree.to_string_node() == "root(0)"
    assert test_tree.children[1].to_string_node() == "child2(2)"
    assert Tree(name="test").to_string_node() == "test"
    assert Tree(data="123").to_string_node() == "123"
    assert Tree().to_string_node() == "."


def test_to_string_tree(test_tree: Tree):
    assert test_tree.to_string_tree() == "root(0)[child1(1)[child1_child1(11)[]], " \
                                         "child2(2)[child2_child1(21)[], child2_child2(22)[]], " \
                                         "child3(3)[child3_child1(31)[], child3_child2(32)[], " \
                                         "child3_child3(33)[child3_child3_child1(331)[]]]]"


def test__str__(test_tree: Tree):
    assert test_tree.__str__() == test_tree.to_string_tree()
