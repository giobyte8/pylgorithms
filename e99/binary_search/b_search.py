
def binary_search(nums: list[int], target: int) -> int:
    if not nums:
        return -1

    start = 0
    end = len(nums) - 1

    while start <= end:
        pivot = (start + end) // 2

        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            start = pivot + 1
        else:
            end = pivot - 1

    return -1
