#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
4 2 2 4
3 3
4 2 2 4
1 1
4 2 2 4
5 5
4 2 4 2
2 4
2 2 2 4
3 3
3 2 2 4
3 3
2 2 2 4
4 2

YES
NO
NO
YES
NO
NO
YES

n, m, a, b
m1, m2
"""
if __name__ == '__main__':
    while True:
        try:
            input_data = map(int, input().strip().split())
            data = list(map(int, input().strip().split()))

            # print(n, m, a, b)
            # test_data = [a, b]
            # if not test_data or not data:
            #     print('NO')

            if n == m:
                if set(data) == set(test_data):
                    print('YES')
                else:
                    print('NO')
            elif n == (m + 1):
                if max(data) <= max(test_data) and min(data) >= min(test_data):
                    if test_data[0] in data or test_data[1] in data:
                        print('YES')
                    else:
                        print('NO')
                else:
                    print('NO')
            elif (n - m) >= 2:
                if max(data) <= max(test_data) and min(data) >= min(test_data):
                    print('YES')
                else:
                    print('NO')
            else:
                print('NO')
        except:
            print('NO')




