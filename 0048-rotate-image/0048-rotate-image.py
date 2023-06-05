class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                
                if (i, j) not in visited:
                    temp_i, temp_j = i, j
                    temp = matrix[i][j]
                    visited.add((i, j))
                    for _ in range(3):
                        matrix[temp_i][temp_j] = matrix[len(matrix) - temp_j-1][temp_i]
                        temp_i, temp_j = len(matrix) - temp_j - 1, temp_i
                        visited.add((temp_i, temp_j))
                    matrix[temp_i][temp_j] = temp
        