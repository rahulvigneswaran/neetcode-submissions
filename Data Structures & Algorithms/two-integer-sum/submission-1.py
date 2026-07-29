class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bal = {}

        for ind in range(len(nums)):
            diff = target - nums[ind]
            if diff not in bal:
                bal[nums[ind]] = ind 
            else:
                return [bal[diff], ind]
                           