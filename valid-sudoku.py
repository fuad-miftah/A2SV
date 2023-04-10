class Solution:
    def validateRows(self,board):
        for i in range(len(board)):
            cur = []
            for j in range(len(board[0])):
                if board[i][j] not in cur and board[i][j] != ".":
                    cur.append(board[i][j])
                elif board[i][j] != ".":
                    return False
        return True

    def validateCols(self,board):
        for i in range(len(board[0])):
            cur = []
            for j in range(len(board)):
                if board[j][i] not in cur and board[j][i] != ".":
                    cur.append(board[j][i])
                elif board[j][i] != ".":
                    return False
        return True

    def validateSquare(self,board):
        for i in range(0,len(board),3):
            for j in range(0,len(board[0]),3):
                cur = []
                for r in range(i,i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] not in cur and board[r][c] != ".":
                            cur.append(board[r][c])
                        elif board[r][c] != ".":
                            return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = self.validateRows(board)
        colCheck = self.validateCols(board)
        squareCheck = self.validateSquare(board)

        return rowCheck and colCheck and squareCheck