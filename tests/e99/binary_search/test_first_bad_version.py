from e99.binary_search.first_bad_version import API, first_bad_version


def test_case_1():
    api = API(10, 6)
    assert (6, 3) == first_bad_version(api)


def test_case_2():
    api = API(versions=6, first_bad=3)
    assert (3, 3) == first_bad_version(api)


def test_case_3():
    api = API(5, 4)
    assert (4, 2) == first_bad_version(api)
