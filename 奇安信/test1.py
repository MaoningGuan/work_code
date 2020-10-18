#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
[ [2,3,1], [2,5,3], [4,2,1] ]
"""


# if __name__ == '__main__':
#     s = input().strip().split(', ')
#     print(s)

class Solution:
    def maxValue(self, matrix):
        # write code here
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    matrix[i][j] = matrix[i][j - 1] + matrix[i][j]
                elif j == 0:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j]
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1]) + matrix[i][j]
        return matrix[-1][-1]


if __name__ == '__main__':
    matrix = [[2, 3, 1], [2, 5, 3], [4, 2, 1]]

    solution = Solution()
    print(solution.maxValue(matrix))
