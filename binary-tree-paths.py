# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def helper(root,rootVal):
            if not root.left and not root.right:
                rootVal.append(str(root.val))
                res.append(rootVal)
                return 
            if not root.left:
                rootVal.append(str(root.val))
                helper(root.right,rootVal)
                return
            elif not root.right:
                rootVal.append(str(root.val))
                helper(root.left,rootVal)
                return
            rootVal.append(str(root.val))
            helper(root.left,rootVal.copy())
            helper(root.right,rootVal.copy())
            return
        helper(root,[])
        for i in range(len(res)):
            res[i] = "->".join(res[i])
        return res