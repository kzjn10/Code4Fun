#Prefix sum + hashmap
def check_subarray_sum(self, nums: list[int], k: int) -> bool:
    seen = {0: -1}
    remain_sum_so_far = 0
    for i, num in enumerate(nums):
        remain_sum_so_far = (remain_sum_so_far + num) % k
        if remain_sum_so_far in seen and i - seen[remain_sum_so_far] >= 2:
            return True

        if remain_sum_so_far not in seen:
            seen[remain_sum_so_far] = i
    return False


class CheckSubarraySum:
    pass


print(f'Result: {check_subarray_sum(CheckSubarraySum, [23, 2, 4, 6, 7], 6)}')
