from e99.utils import swap

def test_swap():
    arr = [1, 2, 3, 4]
    swap(arr, 1, 2)

    assert arr == [1, 3, 2, 4]
