# def plus_one( digits: list[int]) -> list[int]:
#     value = 0
#     for i, digit in enumerate(digits):
#         value += digit * pow(10, len(digits) - i -1)
#     value += 1
#     res = []
#     for number in str(value):
#         res.append(int(number))
#
#     return res

# Brute force
#TC: O(N) Loop one times and loop in result to get data
#SC: O(N) Because create new list to store the digits

def plus_one(digits: list[int]) -> list[int]:
    last_item = digits[-1]
    new_item = last_item + 1
    if new_item > 9:
        l = len(digits) - 1
        while l >= 0 and new_item > 9:
            digits[l] = new_item % 10
            if l - 1 < 0:
                digits.insert(0, 1)
            else:
                new_item = digits[l - 1] + 1
            l -= 1
        if new_item <= 9 and l >= 0:
            digits[l] = new_item
    else:
        digits[len(digits) - 1] = new_item
    return digits

#Optimize for long list
#TC: O(N) Loop in the input digits
#SC: O(N) Because modifying digits list


print(plus_one([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 1]))
print(plus_one([9]))

