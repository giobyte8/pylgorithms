from e99.utils import swap


def sort_colors(colors: list[int]) -> list:
    """Given an array, colors, which contains a combination of the following \
        three elements: \
            - 0 (representing red)   \
            - 1 (representing white) \
            - 2 (representing blue)  \
        Sort the array in place so that the elements of the same color are \
        adjacent, with the colors in the order of red, white, and blue.

    Args:
        colors (list[int]): Array of colors to be sorted

    Returns:
        list: Same array with elements sorted in place
    """
    if len(colors) <= 1:
        return colors

    red = 0
    white = 0
    blue = len(colors) - 1

    while white <= blue:
        if colors[white] == 0:
            swap(colors, white, red)
            white += 1
            red += 1

        elif colors[white] == 1:
            white += 1

        else:
            swap(colors, white, blue)
            blue -= 1

    return colors
