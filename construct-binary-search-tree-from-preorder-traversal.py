# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def traverse(l,r):
            if l >= r:
                if l < len(preorder) and l == r:
                    return TreeNode(preorder[l])
                else:
                    return None
            j = l+1
            while j <= r and preorder[j] < preorder[l]:
                j+=1
            left = traverse(l+1,j-1)
            right = traverse(j,r)

            return TreeNode(preorder[l],left,right)
        return traverse(0,len(preorder)-1)