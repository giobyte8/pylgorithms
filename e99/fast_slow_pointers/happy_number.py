
def is_happy_number(n: int) -> bool:
    """We use the following process to check if a given number is a \
        happy number: \

        1. Starting with the given number 'n', replace the number with \
           the sum of the squares of its digits. \
        2. Repeat the process until: \
             a) The number equals 1, which will depict that the given number \
                is a happy number.
             b) It enters a cycle, which will depict that the given number
                is not a happy number.

    Args:
        n (int): Number to evaluate

    Returns:
        bool: True if given number is a 'happy number'
    """
    slow = n
    fast = sum_squared_digits(n)

    while slow != fast:
        slow = sum_squared_digits(slow)
        fast = sum_squared_digits(sum_squared_digits(fast))

        if fast == 1:
            return True

    return fast == 1


def sum_squared_digits(n: int) -> int:
    """Sums the squares of the digits of a given number

    Args:
        n (int): Number to evaluate

    Returns:
        int: Sum of the squares of the digits of a given number
    """

    # Convert n into a list of its digits
    digits = [int(d) for d in str(n)]

    # Square and sum each digit
    return sum(x**2 for x in digits)
