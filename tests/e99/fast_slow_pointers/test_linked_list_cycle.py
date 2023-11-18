from ds.linked_list import LinkedList
from e99.fast_slow_pointers.linked_list_cycle import has_cycle


def test_has_cycle_1():
    llist = LinkedList.from_items([1, 2, 3, 4, 5])

    # No cycle at this point
    assert not has_cycle(llist.head)

    # Create cycle and assert its existence
    third = llist.head.next.next
    llist.tail.next = third
    assert has_cycle(llist.head)


def test_has_cycle_case_1():
    llist = LinkedList.from_items([2,4,6,8,10])
    llist.tail.next = llist.head.next.next

    assert has_cycle(llist.head)


def test_has_cycle_case_2():
    llist = LinkedList.from_items([1,3,5,7,9])
    assert not has_cycle(llist.head)


def test_has_cycle_case_3():
    llist = LinkedList.from_items([1,2,3,4,5])
    llist.tail.next = llist.head.next.next.next

    assert has_cycle(llist.head)


def test_has_cycle_case_4():
    llist = LinkedList.from_items([0,2,3,5,6])
    assert not has_cycle(llist.head)


def test_has_cycle_case_5():
    llist = LinkedList.from_items([3,6,9,10,11])
    llist.tail.next = llist.head

    assert has_cycle(llist.head)
