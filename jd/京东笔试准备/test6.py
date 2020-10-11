#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    line = sys.stdin.readline().strip().split()

    if line[0] == line[1]:
        print(line[0])
    else:
        print(0)
    # for line in sys.stdin:
    #     path = line.strip().split(',')
    #     # print(path)
    #     print(main(path))
    # print(0)