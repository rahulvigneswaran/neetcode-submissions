# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        resMax = [float("-inf")]
        def helper(node):
            if not node:
                return 0
            
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)

            resMax[0] = max(resMax[0], left + node.val + right)

            return max(left, right) + node.val
        
        helper(root)

        return resMax[0]

        # O(N), O(N)
            
