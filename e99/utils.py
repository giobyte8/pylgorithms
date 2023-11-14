
def swap(arr: list, i: int, j: int) -> None:
    """Swaps elements at given positions in given list

    Args:
        arr (list): List containing elements to swap
        i (int): First element to swap
        j (int): Second element to swap
    """
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
