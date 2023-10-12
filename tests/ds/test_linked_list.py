from ds.linked_list import LinkedList


class TestLinkedList:

    def test_to_array_empty(self):
        ll = LinkedList()
        assert ll.to_array() == []

    def test_to_array(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)

        assert ll.to_array() == [1, 2]

    def test_from_items_empty(self):
        ll = LinkedList.from_items([])
        assert ll.to_array() == []

    def test_from_items(self):
        ll = LinkedList.from_items([6, 5, 4])
        assert ll.to_array() == [6, 5, 4]
