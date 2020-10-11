#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
11
A 2 3 3 4 3 2 2 3 4 A
"""
import collections

if __name__ == '__main__':
    while True:
        n = int(input().strip())
        data = list(input().strip().split())
        # print(n, data)
        queue = []
        queue.append(data[0])

        max_num = 0
        i = 1
        while queue:
            queue.append(data[i])
            j = i - 1
            while j >= 0:
                if data[i] == data[j]:
                    max_num = max(max_num, i - j + 1)
                    for index in range(j, i + 1):
                        queue.pop(index)
                else:
                    j -= 1
            i = i + 1
            if i >= len(data):
                break
        print(max_num)