from e99.binary_search.b_search import binary_search

def test_case_1():
    idx = binary_search([1,6,8,10], 1)
    assert idx == 0


def test_case_2():
    idx = binary_search([11,22,33,44,55,66,77], 33)
    assert idx == 2


def test_case_3():
    idx = binary_search([-3,-1,0,11,15], 0)
    assert idx == 2


def test_case_4():
    idx = binary_search([-30,-27,-8,-6,-1], -1)
    assert idx == 4


def test_case_5():
    idx = binary_search([0], 0)
    assert idx == 0
