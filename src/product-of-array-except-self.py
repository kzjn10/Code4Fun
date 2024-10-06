# Brute force - Time Limit Exceeded
# def product_except_self(nums: list[int]) -> list[int]:
#     result = [0] * len(nums)
#     for i in range(len(nums)):
#         temp = 1
#         for j in range(len(nums)):
#             if i != j:
#                 temp *= nums[j]
#
#         result[i] = temp
#     return result
#TC: O(N^2) - Nested loops
#SC: O(N) - Create temp array to store result

def product_except_self(nums: list[int]) -> list[int]:
    zero_counter = 0
    product = 1
    result = [0] * len(nums)

    # Count zero in list
    for num in nums:
        if num == 0:
            zero_counter += 1
            if zero_counter > 1:
                break
        else:
            product *= num

    # Check count if `zero_counter` more then 1
    if zero_counter > 1:
        # Set index at zero = product value
        return result
    elif zero_counter == 1:
        # Set index at zero = product value
        zero_index = nums.index(0)
        result[zero_index] = product
    else:
        for i in range(len(nums)):
            result[i] = product // nums[i]

    return result


#TC: O(N) - Iterate through the list once to calculate the product of all element
#SC: O(N) -  Create temp array to store result
#Ref: https://www.geeksforgeeks.org/a-product-array-puzzle/


print(product_except_self([1, 2, 3, 4]))  # Output: [24,12,8,6]
print(product_except_self([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
