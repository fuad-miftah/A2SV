# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        left_most = float("inf")
        right_most = float("-inf")
        def traverse(root,col,row):
            nonlocal left_most,right_most
            if root:
                left_most = min(left_most, col)
                right_most = max(right_most, col)
                dic[col].append((row,root.val))
                traverse(root.left,col-1,row+1)
                traverse(root.right,col+1,row+1)

        traverse(root,0,0)
        res = []
        for i in range(left_most,right_most+1):
            temp = [val for row,val in sorted(dic[i])]
            res.append(temp)
        return res