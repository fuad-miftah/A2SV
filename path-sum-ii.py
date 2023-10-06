# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node,arr,s):
            if not root:
                return 
            if not node.left and not node.right:
                s += node.val
                arr.append(node.val)
                if s == targetSum:
                    result.append(arr)
                return
            if node.left:
                dfs(node.left,arr+[node.val],s + node.val)
            if node.right:
                dfs(node.right,arr+[node.val],s + node.val)
        dfs(root,[],0)
        return result