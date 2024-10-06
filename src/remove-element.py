# def remove_element(nums, val) -> int:
#     r = len(nums) - 1
#     l = 0
#     counter = 0
#     while r >= 0 and nums[r] == val:
#         r -= 1
#         counter += 1
#
#     while l <= r:
#         if nums[l] == val:
#             nums[l], nums[r] = nums[r], nums[l]
#             while nums[r] == val:
#                 r -= 1
#                 counter += 1
#         l += 1
#     return len(nums) - counter

#Two pointer
#TC: O(N) Only iterator through the list of nums
#SC: O(1) Not using any extra space

def remove_element(nums, val) -> int:
    counter = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[counter] = nums[i]
            counter += 1
    return counter

#Brute force
#TC: O(N) Only iterator through the list of nums
#SC: O(1) Counter variable to store data

print(remove_element([3, 2, 2, 3], 3))
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(remove_element([1], 1))
print(remove_element([0, 4, 4, 0, 4, 4, 4, 0, 2], 4))