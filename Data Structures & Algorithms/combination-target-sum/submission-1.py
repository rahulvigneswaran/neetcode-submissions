class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(ind, total, subset):
            if total == target:
                res.append(subset.copy())
                return
            
            if ind >= len(nums) or total > target:
                return 
            
            # include
            subset.append(nums[ind])
            helper(ind, total+nums[ind], subset)
            subset.pop()

            # exclude
            helper(ind + 1, total, subset)

        helper(0, 0, [])

        return res            

        # O(2^(T/M)), O(T/M)