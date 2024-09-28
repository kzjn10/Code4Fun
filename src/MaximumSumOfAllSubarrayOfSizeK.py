# https://www.geeksforgeeks.org/window-sliding-technique/
def maximum_sum_of_all_sub_arrays_of_size_k(nums: list[int], k: int) -> int:
    if len(nums) <= k:
        return -1

    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(len(nums) - k):
        current_sum = current_sum - nums[i] + nums[i + k]
        max_sum = max(current_sum, max_sum)

    return max_sum


class SubarrayLessThanK:
    pass


print(f'Result: {maximum_sum_of_all_sub_arrays_of_size_k([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)}')
print(f'Result: {maximum_sum_of_all_sub_arrays_of_size_k([2, 3], 3)}')
