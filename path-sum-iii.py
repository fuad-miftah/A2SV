# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        res = 0
        def traverse(root,curSum):
            nonlocal res
            if root:
                curSum+=root.val
                if curSum - targetSum in dic:
                    res+=dic[curSum - targetSum]
                dic[curSum] += 1
                l = traverse(root.left,curSum)
                r = traverse(root.right,curSum)
                dic[curSum] -= 1
            return
        traverse(root,0)
        return res