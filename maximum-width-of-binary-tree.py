# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(list)
        def traverse(root,row,num):
            if root:
                traverse(root.left,row+1,(2*num))
                traverse(root.right,row+1,(2*num)+1)
                if row in dic:
                    dic[row][0] = min(dic[row][0], num)
                    dic[row][1] = max(dic[row][1], num)
                else:
                    dic[row] = [num,num]
        traverse(root,0,0)
        
        res = 0
        for key in dic:
            width = dic[key][1] - dic[key][0] + 1
            res = max(res,width)
        return res