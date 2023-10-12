from ds.linked_list import LinkedList
from e99.two_pointers.remove_nth_last_node import remove_nth_last_node


def test_remove_nth_last_node_1():
    ll = LinkedList.from_items([1, 2, 3])
    head = remove_nth_last_node(ll.head, 1)

    assert head.to_array() == [1, 2]


def test_remove_nth_last_node_2():
    ll = LinkedList.from_items([1, 2, 3])
    head = remove_nth_last_node(ll.head, 2)

    assert head.to_array() == [1, 3]


def test_remove_nth_last_node_3():
    ll = LinkedList.from_items([1, 2, 3])
    head = remove_nth_last_node(ll.head, 3)

    assert head.to_array() == [2, 3]


def test_remove_nth_last_node_4():
    ll = LinkedList.from_items([23, 28, 10, 5, 67, 39, 70, 28])
    head = remove_nth_last_node(ll.head, 2)

    assert head.to_array() == [23, 28, 10, 5, 67, 39, 28]


def test_remove_nth_last_node_5():
    ll = LinkedList.from_items([69, 8, 49, 106, 116, 112])
    head = remove_nth_last_node(ll.head, 6)

    assert head.to_array() == [8, 49, 106, 116, 112]
