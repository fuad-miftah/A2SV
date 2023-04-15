# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def helper(root,res,s):
            if not root.right and not root.left:
                s+=str(root.val)
                res.append(s)
                return res
            if not root.left:
                s+=str(root.val)
                helper(root.right,res,s)
                return res
            elif not root.right:
                s+=str(root.val)
                helper(root.left,res,s)
                return res
            s+=str(root.val)
            helper(root.left,res,s)
            helper(root.right,res,s)
            return res
        res = helper(root,[],"")
        res = list(map(int,res))
    
        return sum(res)