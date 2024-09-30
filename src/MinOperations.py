import math


def min_operations( n: int) -> int:
    if n == pow(2, int(math.log2(n))):
        return 1

    low = pow(2, int(math.log2(n)))
    height = pow(2, int(math.log2(n)) + 1)
    d1 = n - low
    d2 = height - n

    return 1 + min(min_operations(d1), min_operations(d2))

print(min_operations( 39))
print(min_operations(54))
print(min_operations(70))
