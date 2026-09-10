# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low = float("-inf")
        high = float("inf")

        def check(node, l, h):
            if not node:
                return True
            if node.val <= l or node.val >= h:
                return False
            return check(node.right, max(node.val, l), h) and check(node.left, l, min(node.val, h))
        
        return check(root, low, high)