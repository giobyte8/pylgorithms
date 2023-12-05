
class API:

    def __init__(self, versions: int, first_bad: int) -> None:
        self.versions = versions
        self.first_bad = first_bad

    def is_bad(self, version: int):
        return version >= self.first_bad


def first_bad_version(api: API):
    n = api.versions

    first_bad = -1
    api_calls = 0

    start = 1
    end = n

    while start <= end:
        pivot = (start + end) // 2

        api_calls += 1
        if api.is_bad(pivot):
            first_bad = pivot
            end = pivot - 1

        else:
            start = pivot + 1

    return first_bad, api_calls


