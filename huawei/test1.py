#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
uvwxyz
"""
strs = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
        'v','w','x','y','z']
if __name__ == '__main__':
    while True:
        try:
            n = int(input().strip())
            if n == 0:
                break

            for _ in range(n):
                res = []
                s = input().strip()
                if not s:
                    print('')
                    continue
                a = 0
                b = 1
                for c in s:
                    d = a + b
                    offset = b
                    a, b = b, d
                    ind = strs.index(c)
                    index = ind + offset
                    index = index % 26
                    res.append(strs[index])
                print(''.join(res))
        except:
            break

