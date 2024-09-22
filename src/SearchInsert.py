def search_insert(nums: list, target: int) -> int:
    start = 0
    end = len(nums) - 1
    mid = 0
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
    else:
        start = mid + 1

    return start


class SearchInsert:
    pass


sl = SearchInsert()
# Tc1 - 2
data1 = [1, 3, 5, 6]
print('Result: ${sl.searchInsert(data1, 5) == 2}')

# Tc2 - 1
data2 = [1, 3, 5, 6]
print('Result: ${sl.searchInsert(data2, 2) == 1}')

# Tc3 == 4
data3 = [1, 3, 5, 6]
print('Result: ${sl.searchInsert(data3, 7)==4}')

# Tc4 - 1
data4 = [1, 3]
print('Result: ${sl.searchInsert(data4, 2) == 1}')

# Tc5
data5 = [3]
print('Result: ${sl.searchInsert(data5, 3) == 0}')

# Tc6
data6 = [1, 3]
print('Result: ${sl.searchInsert(data6, 3)}')

# Tc7
data7 = [1, 3, 5]
print('Result: ${sl.searchInsert(data7, 4)}')

# Tc8
data8 = [1, 3, 5, 6]
print('Result: ${sl.searchInsert(data8, 2)}')

# Tc9 - 2
data9 = [1, 4, 6, 7, 8, 9]
print('Result: ${sl.searchInsert(data9, 6)}')

# Tc10 - 1
data10 = [1, 2, 3, 4, 5, 10]
print('Result: ${sl.searchInsert(data10, 2) == 1}')

# Tc10 - 1
data11 = [3, 6, 7, 8, 10]
print('Result: ${sl.searchInsert(data11, 5) == 1}')
