def plus_one( digits: list[int]) -> list[int]:
    value = 0
    for i, digit in enumerate(digits):
        value += digit * pow(10, len(digits) - i -1)
    value += 1
    res = []
    for number in str(value):
        res.append(int(number))

    return res

print(plus_one([1,2,3,4,5,6,7,8,9]))
print(plus_one([1,2,3]))
print(plus_one([4,3,2,1]))
print(plus_one([9]))
