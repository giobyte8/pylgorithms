from ds.linked_list import LinkedListNode

def remove_nth_last_node(head: LinkedListNode, n: int) -> LinkedListNode:
    """Given a singly linked list, remove the nth node from the end of the \
        list and return its head.

    Args:
        head (LinkedListNode): Head of singly linked list
        n (int): Nth node to remove (Assume: 1 <= n <= len(list))

    Returns:
        LinkedListNode: Head of altered linked list
    """
    if head is None: return None

    # Set left and right pointers at start of list
    left  = head
    right = head

    # Advance 'right' nth positions
    for i in range(0, n):
        if right is None:
            break

        right = right.next

    # Removing list head?
    if right is None:
        tmp = left.next
        left.next = None
        left = head = tmp
    else:
        # Move both pointers until reach end of list
        while right.next is not None:
            left  = left.next
            right = right.next

        # Remove nth element
        tmp = left.next.next
        left.next.next = None
        left.next = tmp

    return head
