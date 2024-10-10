def sum_of_unique(nums: list[int]) -> int:
    arr = [0] * 101
    for num in nums:
        arr[num] += 1

    res = 0
    for item in nums:
        if arr[item] == 1:
            res += item

    return res


if __name__ == '__main__':
    print(sum_of_unique([1, 2, 3, 2]))  # 4
    print(sum_of_unique([1, 1, 1, 1, 1]))  # 0
    print(sum_of_unique([1, 2, 3, 4, 5]))  # 15
