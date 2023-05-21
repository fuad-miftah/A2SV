class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        newMat = []
        leftToright = True
        for i in range(len(board)-1,-1,-1):
            if leftToright:
                for j in range(len(board[0])):
                    num = board[i][j]
                    if num == -1:
                        newMat.append(num)
                    else:
                        newMat.append(num-1)
                leftToright = False
            else:
                for j in range(len(board[0]) - 1, -1, -1):
                    num = board[i][j]
                    if num == -1:
                        newMat.append(num)
                    else:
                        newMat.append(num-1)
                leftToright = True

        queue = deque()
        queue.append((0,0))
        visited = set()
        visited.add(0)
        while queue:
            curr,move = queue.popleft()
            for i in range(1,7):
                nextMove = curr + i
                inbound = 0 < nextMove <= len(newMat) - 1
                if inbound and nextMove not in visited:
                    visited.add(nextMove)
                    if newMat[nextMove] != -1:
                        nextMove = newMat[nextMove]
                    if nextMove == len(newMat) - 1:
                        return move + 1
                    queue.append((nextMove,move + 1))
                    
        return -1