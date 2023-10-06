# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0

        def dfs(node):
            nonlocal result
            if not node:
                return []
            l = dfs(node.left)
            r = dfs(node.right)
            res = [node.val]
            if node.val == targetSum:
                result += 1
            for i in l:
                if i + node.val == targetSum:
                    result += 1
                res.append(i + node.val)
            for i in r:
                if i + node.val == targetSum:
                    result += 1
                res.append(i + node.val)
            return res

        dfs(root)
        return result