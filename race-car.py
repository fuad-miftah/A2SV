class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1,0)])  #pos, speed, moves
        
        while queue:
            pos,speed,moves = queue.popleft()
            
            if pos==target:
                return moves
        
            queue.append(( pos + speed, speed * 2 ,moves + 1))   #Acceleration
            
            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0): 
                if speed < 0:
                    queue.append((pos,1,moves + 1))
                else:
                    queue.append((pos,-1,moves + 1))