# Prefix sum
# 560. Subarray Sum Equals K
def subarray_sum(arr: list, k: int) -> int:
    res = 0
    cur_sum = 0
    prefix_sum = {0: 1}
    for i in arr:
        cur_sum += i
        diff = cur_sum - k
        res += prefix_sum.get(diff, 0)
        prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)
    return res


class SubarraySumEqualsK:
    pass


print(f'Result: {subarray_sum([1, 1, 1], 2)}')
print(f'Result: {subarray_sum([1, 2, 3], 3)}')
