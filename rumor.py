from collections import defaultdict
from collections import deque
n,m = map(int, input().split())
friends = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
 
res = 0
visited = set()
 
def bfs(q):
    while q:
        node = queue.popleft()
        for friend in graph[node]:
            if friend not in visited:
                visited.add(friend)
                q.append(friend)
                path.append(friends[friend-1])
 
for i in range(n):
    if i + 1 not in visited:
        path = []
        queue = deque()
        queue.append(i+1)
        path.append(friends[i])
        bfs(queue)
        res += min(path)
print(res)