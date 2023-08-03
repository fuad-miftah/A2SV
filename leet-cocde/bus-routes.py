class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        queue = deque()
        visited = set()
        graph = defaultdict(list)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                    graph[routes[i][j]].append(i)
        
        for indx in graph[source]:
            for route in routes[indx]:
                queue.append(route)
            visited.add(indx)
        level = 1
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node == target:
                    return level

                for indx in graph[node]:
                    if indx not in visited:
                        for route in routes[indx]:
                            queue.append(route)
                        visited.add(indx)
            level += 1

        return -1