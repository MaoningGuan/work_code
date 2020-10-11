#!/usr/bin/env python
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    while True:
        try:
            n = int(input().strip())

            if n == 0:
                print(0)

            num = 0  # 瓶盖数
            count = 0   # 金钱
            numbers = 0  # 牛奶数
            while True:
                if num < 2:
                    count += 5
                    num += 1
                    numbers += 1
                else:
                    num -= 1
                    count += 1
                    numbers += 1
                if numbers == n:
                    break
            print(count)
        except:
            break