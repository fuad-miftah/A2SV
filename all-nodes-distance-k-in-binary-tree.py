# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph=defaultdict(list)  
        stack=[root]
        while stack:
            node=stack.pop()
            if node == target:
                tval = node.val
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)
        
        q=deque([(tval,0)])
        visited=set([tval])
        
        res=[]
        while q:
            node, level = q.popleft()
            if level == k: 
                res.append(node)
            if level > k: 
                break 

            for neighbour in graph[node]:
                if neighbour not in visited:
                    q.append((neighbour,level+1))
                    visited.add(neighbour)
        return res