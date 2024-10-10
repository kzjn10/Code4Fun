class NumArray:

    def __init__(self, nums: list[int]):
        self.P = [0]
        for num in nums:
            self.P.append(self.P[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.P[right+1] - self.P[left]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
