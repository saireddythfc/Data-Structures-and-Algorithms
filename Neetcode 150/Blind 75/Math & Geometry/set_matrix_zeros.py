"""

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]


Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        rows, cols = [], []

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for i in rows:
            for j in range(col):
                matrix[i][j] = 0

        for j in cols:
            for i in range(row):
                matrix[i][j] = 0


# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n, m = len(matrix), len(matrix[0])
#         row = [0] * n
#         col = [0] * m
#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 0:
#                     row[i] = 1
#                     col[j] = 1

#         for i in range(n):
#             for j in range(m):
#                 if row[i] or col[j]:
#                     matrix[i][j] = 0
