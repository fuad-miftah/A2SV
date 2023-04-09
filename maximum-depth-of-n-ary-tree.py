"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def traverse(self,root,depth,cur):
        if root:
            for i in range(len(root.children)):
                
                self.traverse(root.children[i],depth,cur+1)
                self.dep = max(self.dep, cur + 1)
            return cur+1
    def maxDepth(self, root: 'Node') -> int:
        self.dep = 0
        self.traverse(root,0,0)
        return self.dep + 1 if root != None else 0