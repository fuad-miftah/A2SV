# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        def helper(root,father,gf):
            nonlocal res
            if root:
                if gf % 2 == 0:
                    res += root.val
                helper(root.left,root.val,father)
                helper(root.right,root.val,father)
            
        helper(root,1,1)
        return res