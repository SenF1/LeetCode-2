class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row Validation
        for row in board:
            tempRow = []
            for col in row:
                if col == ".":
                    continue
                elif col not in tempRow and int(col) <= 9 and int(col) >= 1:
                    tempRow.append(col)
                else:
                    return False

        # Col Validation
        for col in range(len(board)):
            tempCol = []
            for row in range(len(board)):
                if board[row][col] == ".":
                    continue
                elif board[row][col] not in tempCol and int(board[row][col]) <= 9 and int(board[row][col]) >= 1:
                    tempCol.append(board[row][col])
                else:
                    return False

        # Square Validation
        centerCells = [[1,1],[4,1],[7,1],[1,4],[4,4],[4,7],[1,7],[7,4],[7,7]]
        for row, col in centerCells:
            tempSquare = []
            if board[row][col] != ".":
                tempSquare.append(board[row][col])
            for dirRow, dirCol in [[-1,-1],[0,1],[1,0],[-1,0],[0,-1],[1,1],[1,-1],[-1,1]]:
                if board[row+dirRow][col+dirCol] == ".":
                    continue
                elif board[row+dirRow][col+dirCol] not in tempSquare and int(board[row+dirRow][col+dirCol]) <= 9 and int(board[row+dirRow][col+dirCol]) >= 1:
                    tempSquare.append(board[row+dirRow][col+dirCol])
                else:
                    return False
        return True
        