def min_operation_reduce_to_zero(nums: list[int], x: int) -> int:
    target = sum(nums) - x
    cur_sum = 0
    max_windows = -1
    l = 0
    for r in range(len(nums)):
        cur_sum += nums[r]
        while l <= r and cur_sum > target:
            cur_sum -= nums[l]
            l += 1

        if cur_sum == target:
            max_windows = max(max_windows, r - l + 1)

    return -1 if max_windows == -1 else len(nums) - max_windows

print(min_operation_reduce_to_zero([1,1,4,2,3], 5))
print(min_operation_reduce_to_zero([5,6,7,8,9], 4))
print(min_operation_reduce_to_zero([3,2,20,1,1,3], 10))
