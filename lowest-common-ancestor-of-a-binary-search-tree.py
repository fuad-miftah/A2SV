# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = TreeNode()
        found = False
        def lca(root):
            nonlocal res
            nonlocal found
            if not root:
                return [False,False]
            l = lca(root.left)
            r = lca(root.right)
            if root.val == p.val and (l[1] or r[1]):
                if found == False:
                    res = p
                found = True
                return [True,True]
            elif root.val == q.val and (l[0] or r[0]):
                if found == False:
                    res = q
                found = True
                return [True,True]
            elif (l[0] or r[0]) and (l[1] or r[1]):
                if found == False:
                    res.val = root.val
                found = True
                return [True,True]
            else:
                if root.val == p.val:
                    return [True,False]
                elif root.val == q.val:
                    return [False,True]
                else:
                    if l[0] or r[0]:
                        return [True,False]
                    elif l[1] or r[1]:
                        return [False,True]
                    else:
                        return [False,False]
        lca(root)
        
        return res