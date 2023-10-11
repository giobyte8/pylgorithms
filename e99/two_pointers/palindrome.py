
def is_palindrome(s: str):
    if len(s) in [0, 1]:
        return True

    p1 = 0
    p2 = len(s) - 1
    while p1 < p2:
        if s[p1] != s[p2]:
            return False

        p1 += 1
        p2 -= 1

    return True
