# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(LB, UB, node):
            if not node:
                return True
            
            if LB < node.val < UB:
                return helper(LB, node.val, node.left) and helper(node.val, UB, node.right)
            
            return False

        return helper(float("-inf"), float("inf"), root)