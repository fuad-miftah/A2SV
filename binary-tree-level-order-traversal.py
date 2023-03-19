# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def levelTraversal(root,res,level):
            if not root:
                return res
            if len(res) <= level:
                res.append([root.val])
            else:
                res[level].append(root.val)
            levelTraversal(root.left,res,level+1)
            levelTraversal(root.right,res,level+1)
            return res
        return levelTraversal(root,[],0)