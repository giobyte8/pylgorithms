"""Check whether or not a linked list contains a cycle. If a cycle exists, \
    return TRUE. Otherwise, return FALSE. The cycle means that at least one \
    node can be reached again by traversing the next pointer.
"""

from ds.linked_list import LinkedListNode


def has_cycle(head: LinkedListNode) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
