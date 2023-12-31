from __future__ import annotations


class LinkedListNode:

    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def to_array(self) -> list:
        n = self
        arr = []
        while n is not None:
            arr.append(n.data)
            n = n.next

        return arr


class LinkedList:

    def __init__(self) -> None:
        self.size = 0
        self.tail = None
        self.head = None

    def add(self, data: any) -> None:
        node = LinkedListNode(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def to_array(self) -> list:
        arr = []
        n = self.head
        while n is not None:
            arr.append(n.data)
            n = n.next

        return arr

    @staticmethod
    def from_items(items: list) -> LinkedList:
        ll = LinkedList()
        for it in items:
            ll.add(it)

        return ll
