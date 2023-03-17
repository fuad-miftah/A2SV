# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(root,level,res):
            if not root:
                return res
            if len(res) <= level:
                res.append([root.val])
            else:
                res[level].append(root.val)
            helper(root.left,level+1,res)
            helper(root.right,level+1,res)
            return res
        res = helper(root,0,[])
        ans = []
        for i in range(len(res)):
            ans.append(res[i][-1])
        return ans