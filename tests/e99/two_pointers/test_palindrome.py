from e99.two_pointers.palindrome import is_palindrome


def test_is_palindrome_empty():
    assert is_palindrome('')


def test_is_palindrome_single_char():
    assert is_palindrome('G')


def test_is_palindrome():
    assert is_palindrome('abba')
    assert is_palindrome('kayak')
    assert is_palindrome('racecar')


def test_is_palindrome_negative():
    assert not is_palindrome('hello')
    assert not is_palindrome('raceacar')
    assert not is_palindrome('ABCDABCD')
