from e99.two_pointers.sort_colors import sort_colors


def test_sort_colors_1():
    colors = [0, 1, 2, 0, 1, 2]
    colors = sort_colors(colors)

    assert colors == [0, 0, 1, 1, 2, 2]


def test_sort_colors_2():
    colors = [1, 1, 0]
    colors = sort_colors(colors)

    assert colors == [0, 1, 1]


def test_sort_colors_3():
    colors = [0,1,0]
    colors = sort_colors(colors)

    assert colors == [0, 0, 1]


def test_sort_colors_4():
    colors = [1]
    colors = sort_colors(colors)

    assert colors == [1]


def test_sort_colors_5():
    colors = [2, 2]
    colors = sort_colors(colors)

    assert colors == [2, 2]


def test_sort_colors_6():
    colors = [2, 1, 1, 0, 0]
    colors = sort_colors(colors)

    assert colors == [0, 0, 1, 1, 2]
