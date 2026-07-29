class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bal = {}

        for ind in range(len(nums)):
            diff = target - nums[ind]
            if diff in bal:
                return [bal[diff], ind]
            bal[nums[ind]] = ind                