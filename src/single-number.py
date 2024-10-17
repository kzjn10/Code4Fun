def single_number(nums: list[int]) -> int:
    store = {}
    for num in nums:
        store[num] = 1 + store.get(num, 0)

    for key, value in store.items():
        if value == 1:
            return key
    return -1


if __name__ == '__main__':
    print(single_number([2, 2, 1]))  # 1
