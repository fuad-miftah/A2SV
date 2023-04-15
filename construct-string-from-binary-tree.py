# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root):
        if not root.left and not root.right:
            return str(root.val)
        elif not root.left:
            return str(root.val) + "()" + "(" + self.traverse(root.right) + ")"
        elif not root.right:
            return str(root.val) + "(" + self.traverse(root.left) + ")"
        else:
            left = self.traverse(root.left)
            right = self.traverse(root.right)
            
            return str(root.val) + "(" + left + ")" + "(" + right + ")"
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.traverse(root)