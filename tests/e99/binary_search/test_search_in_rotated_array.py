from e99.binary_search.search_in_rotated_array import binary_search_rotated


def test_case_1():
    nums = [6,7,1,2,3,4,5]
    target = 3

    assert 4 == binary_search_rotated(nums, target)


def test_case_2():
    nums = [6,7,1,2,3,4,5]
    target = 6

    assert 0 == binary_search_rotated(nums, target)


def test_case_3():
    nums = [4,5,6,1,2,3]
    target = 3

    assert 5 == binary_search_rotated(nums, target)


def test_case_4():
    nums = [4,5,6,1,2,3]
    target = 6

    assert 2 == binary_search_rotated(nums, target)


def test_case_5():
    nums = [4]
    target = 1

    assert -1 == binary_search_rotated(nums, target)

