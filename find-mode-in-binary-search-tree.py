# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root,res):
            if not root:
                return res
            helper(root.left,res)
            helper(root.right,res)
            res.append(root.val)
            return res
        res = helper(root,[])
        counts = Counter(res)
        maxCount = counts.most_common(1)[0][1]
        ans = [value for value, count in counts.most_common() if count == maxCount]
        return ans