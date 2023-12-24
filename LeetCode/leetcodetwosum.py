class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for index, value in enumerate(nums):
            x = target - value
            if x in d:
                return [d[x], index]
            else:
                d[value] = index
