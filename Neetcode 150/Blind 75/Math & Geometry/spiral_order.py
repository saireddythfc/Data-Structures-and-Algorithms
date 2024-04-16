"""

Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = []

        for i in range(m):
            visited.append([False] * n)

        move = {0: 1, 1: 2, 2: 3, 3: 0}
        ans = []
        dire = 0
        r, c = 0, 0
        seen = m * n
        while seen > 0:
            if dire == 0:
                while c < n:
                    # print(r,c, dire)
                    if not visited[r][c]:
                        ans.append(matrix[r][c])
                        visited[r][c] = True
                        c += 1
                        seen -= 1
                    else:
                        c -= 1
                        r += 1
                        break
                else:
                    c -= 1
                    r += 1

            elif dire == 1:
                while r < m:
                    # print(r,c, dire)
                    if not visited[r][c]:
                        ans.append(matrix[r][c])
                        visited[r][c] = True
                        r += 1
                        seen -= 1
                    else:
                        r -= 1
                        c -= 1
                        break
                else:
                    r -= 1
                    c -= 1

            elif dire == 2:
                while c >= 0:
                    # print(r,c, dire)
                    if not visited[r][c]:
                        ans.append(matrix[r][c])
                        visited[r][c] = True
                        c -= 1
                        seen -= 1
                    else:
                        c += 1
                        r -= 1
                        break
                else:
                    c += 1
                    r -= 1

            elif dire == 3:
                while r >= 0:
                    # print(r,c, dire)
                    if not visited[r][c]:
                        ans.append(matrix[r][c])
                        visited[r][c] = True
                        r -= 1
                        seen -= 1
                    else:
                        r += 1
                        c += 1
                        break
                else:
                    r += 1
                    c += 1
            dire = move[dire]

        return ans


# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         res = []
#         top, bottom = 0, len(matrix)
#         left, right  = 0, len(matrix[0])
#         while left<right and top < bottom:
#             for i in range(left, right):
#                 res.append(matrix[top][i])
#             top += 1
#             for i in range(top, bottom):
#                 res.append(matrix[i][right-1])
#             right -= 1
#             if not (left<right and top<bottom):
#                 break
#             for i in range(right-1, left-1,-1):
#                 res.append(matrix[bottom -1][i])
#             bottom -= 1
#             for i in range(bottom -1, top -1, -1):
#                 res.append(matrix[i][left])
#             left += 1
#         return res
