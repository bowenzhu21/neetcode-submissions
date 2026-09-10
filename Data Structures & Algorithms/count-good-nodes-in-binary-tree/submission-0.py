# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        self.good = 0

        def dfs(node, high):
            if node.val >= high:
                self.good += 1
                high = node.val
            if node.left:
                dfs(node.left, high)
            if node.right:
                dfs(node.right, high)

        dfs(root, root.val)
        return self.good