# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root):
            if not root:
                return [True,float("-inf"),float("inf")]
            l = isValid(root.left)
            r = isValid(root.right)

            if l[0] and r[0]:
                if (l[1] != float("-inf") and l[1] >= root.val) or (r[2] != float("inf") and r[2] <= root.val):
                    
                    return [False]
                else:
                    return [True,max(root.val, l[1], r[1]), min(root.val,l[2],r[2])]
            else:
                return [False]
        res = isValid(root)
        return res[0]