# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(root,parent):
            nonlocal ans
            if not root:
                return 0
            left = helper(root.left,root.val)
            right = helper(root.right,root.val)

            ans = max(ans, left + right)
            if root.val != parent:
                return 0
            else:
                return max(left,right)+1
        helper(root,-2000)
        return ans