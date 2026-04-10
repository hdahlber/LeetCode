class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
       
        n = len(matrix) # n of rows
        m = len(matrix[0]) # n columns
        self.prefix = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if j-1 != -1:
                    self.prefix[i][j] = (matrix[i][j] + self.prefix[i][j-1])
                else:
                    self.prefix[i][j] = matrix[i][j]
                
                #print(self.prefix[i][j], j, matrix[i][j], self.prefix[i][j-1])





    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_sum = 0
        for r in range(row1, row2 + 1):
            if col1 > 0:
                total_sum += self.prefix[r][col2] - self.prefix[r][col1 - 1]
            else:
                total_sum += self.prefix[r][col2]
                
        return total_sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)