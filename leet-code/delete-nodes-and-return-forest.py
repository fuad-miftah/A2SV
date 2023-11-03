# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        
        def dfs(node, pval):
            if not node: 
                return 
            if node.val in to_delete: 
                node.left = dfs(node.left, None)
                node.right = dfs(node.right, None)
                return 
            else: 
                if not pval: 
                    ans.append(node)
                node.left = dfs(node.left, node.val)
                node.right = dfs(node.right, node.val)
                return node 
        
        ans = []
        dfs(root, None)
        return ans 
        