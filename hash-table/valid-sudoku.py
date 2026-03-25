class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for c, row_vals in enumerate(board):
            l = [j for j in row_vals if j.isnumeric()]
            if len(l) != len(set(l)):
                return False
            
            col =[board[r][c] for r in range(9) if board[r][c].isnumeric()]
            if len(col) != len(set(col)):
                return False
        for row in range(3):
            for col in range(3):
                box = []

                for r in range(row * 3, row * 3 + 3):
                    for c in range(col * 3, col * 3 + 3):
                        val = board[r][c]
                        if val.isnumeric():
                            box.append(val)
                if len(box) != len(set(box)):
                    return False
        return True


