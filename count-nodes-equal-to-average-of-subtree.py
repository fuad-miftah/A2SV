# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root):
            nonlocal res
            if not root:
                return [0,0]

            l = helper(root.left)
            r = helper(root.right)
            
            sums = l[1] + r[1] + root.val
            count = l[0] + r[0] + 1
            if sums // count == root.val:
                res+=1

            return [count,sums]
        helper(root)
        return res