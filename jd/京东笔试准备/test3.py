#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 0,1,2,3,4,3,2,1,5,6,5,7,8,9,8,7,5,1,0
success_path = [str(c) for c in [0,1,2,3,4,3,2,1,5,6,5,7,8,9,8,7,5,1,0]]
bad_path = ['A', 'B', 'C', 'D', 'E', 'F']


def main(path):
    i = 0
    for j in range(len(path)):
        if path[j] in bad_path:
            return 'Collision'
        elif path[j] == '-1':
            return 'Out of path'
        elif path[j] == success_path[i]:
            if j > 0 and path[j] == path[j - 1]:
                pass
            else:
                i += 1
        else:
            return 'Bad path'
    return 'Success' if i == len(success_path) else 'Bad path'


if __name__ == '__main__':
    for line in sys.stdin:
        path = line.strip().split(',')
        print(path)
        print(main(path))
    # print(main(success_path))