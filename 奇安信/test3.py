#!/usr/bin/env python
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    N = int(input().strip())
    if 1 <= N <= 200:
        res = 1
        for i in range(2, N + 1):
            res *= i
        print(res)
    else:
        print('Error')
