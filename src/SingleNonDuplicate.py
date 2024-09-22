def single_non_duplicate(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    left = 0
    right = len(nums) - 1
    temp = -1
    while left <= right:
        mid = (left + right) // 2
        count_less_or_equal = 0
        for n in nums:
            if n <= nums[mid]:
                count_less_or_equal += 1

        if count_less_or_equal % 2 != 0:
            temp = mid
            right = mid - 1
        else:
            left = mid + 1

    return nums[temp]


class SingleNonDuplicate:
    pass

solution = SingleNonDuplicate()
print(single_non_duplicate([0, 1, 1]))
print(single_non_duplicate([1, 2, 2, 3, 3]))
print(single_non_duplicate([1, 1, 2, 2, 3]))
print(single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(single_non_duplicate([3, 3, 7, 7, 10, 11, 11]))
print(single_non_duplicate([3, 3, 7, 7, 11, 11, 12]))