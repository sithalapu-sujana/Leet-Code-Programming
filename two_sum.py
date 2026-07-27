class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]     #o(n**2)

class Solution:
    def twoSum(self, nums, target):
        d = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in d:
                return [d[need], i]

            d[nums[i]] = i #o(n) best
