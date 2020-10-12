#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
5 4
MMMM
MMFF
FMMM
MMMM
MFMM
"""
class Solution:
    def maxSquare(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 'M':
                    maxSide = max(maxSide, 1)
                    currentMaxSide = min(rows-i, columns-j)
                    for k in range(1, currentMaxSide):
                        flag = True
                        if matrix[i+k][j+k] == 'F':
                            break
                        for m in range(k):
                            if matrix[i+k][j+m] == 'F' or matrix[i+m][j+k] == 'F':
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k+1)
                        else:
                            break

        maxSquare = maxSide * maxSide
        return maxSquare



if __name__ == '__main__':
    solution = Solution()
    while True:
        m, n = map(int, input().strip().split())
        matrix = list()
        for _ in range(m):
            matrix.append(list(input().strip()))

        # print(matrix)
        print(solution.maxSquare(matrix))
