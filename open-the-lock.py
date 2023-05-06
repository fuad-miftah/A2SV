class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        if "0000" in deadends: return -1      
        if target == "0000": return 0
        
        queue = deque()
        visited = set()
        queue.append(["0000", 0])
        
        while len(queue) > 0:   
            cur, level = queue.popleft()            
            nnum = []       
            
            for i in range(4):
                nnum.append(cur[:i] + str((int(cur[i]) + 1) % 10) + cur[i+1:])                
                nnum.append(cur[:i] + str((int(cur[i]) - 1) % 10) + cur[i+1:])
            
            for num in nnum:
                if num in visited or num in deadends:
                    continue
                visited.add(num)               
                if num == target:
                    return level + 1
                queue.append([num, level + 1])                
        return -1