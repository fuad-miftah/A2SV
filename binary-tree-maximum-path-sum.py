# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root):
        if not root:
            return 0
            
        l = max(self.dfs(root.left), 0)
        r = max(self.dfs(root.right), 0)

        self.maxSum = max(self.maxSum, (root.val + l + r))

        return root.val + max(l, r)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxSum = float("-inf")
        self.dfs(root)
        return self.maxSum