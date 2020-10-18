#!/usr/bin/env python
# -*- coding: utf-8 -*-
def factor(n):
    if n == 1:
        return 1
    else:
        return n * factor(n - 1)


if __name__ == '__main__':
    N = int(input().strip())
    if 1 <= N <= 200:
        res = factor(N)
        print(res)
    else:
        print('Error')
