#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
2,5,7
"""
l = [2, 5, 7]


class Solution:
    def is_product(self, N):
        while True:
            a1, b1 = divmod(N, l[0])
            a2, b2 = divmod(N, l[1])
            a3, b3 = divmod(N, l[2])
            if b1 == 0:
                N = a1
            elif b2 == 0:
                N = a2
            elif b3 == 0:
                N = a3
            else:
                return 0

            if N == 1:
                return 1

# write code here
if __name__ == '__main__':
    N = 89

    solution = Solution()
    print(solution.is_product(N))