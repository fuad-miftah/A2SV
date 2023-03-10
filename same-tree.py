# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            if not p and not q:
                return True
            elif not p:
                return False
            elif not q:
                return False
            if p.val != q.val:
                return False
            else:
                return isSame(p.left,q.left) and isSame(p.right,q.right)
            
        return isSame(p,q)