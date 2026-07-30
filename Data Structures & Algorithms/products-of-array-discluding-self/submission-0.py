class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        cum = 1
        for ind in range(len(nums)):
            res[ind] *= cum
            cum *= nums[ind]
        
        cum = 1
        for ind in range(len(nums)-1, -1, -1):
            res[ind] *= cum
            cum *= nums[ind]
        
        return res
        