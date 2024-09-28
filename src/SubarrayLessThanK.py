# Sliding window
# 713. Subarray Product less than K
def num_subarray_less_than_k(nums: list[int], k: int) -> int:
    res = 0
    l = 0
    product = 1
    for r in range(len(nums)):
        product *= nums[r]
        while l <= r and product >= k:
            product = product // nums[l]
            l += 1
        res += r - l + 1
    return res


class SubarrayLessThanK:
    pass

print(f'Result: {num_subarray_less_than_k([10, 5, 2, 6], 100)}')
print(f'Result: {num_subarray_less_than_k([1, 2, 3], 0)}')
