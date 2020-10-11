#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
1
4
3 -2 4 -1
"""
if __name__ == '__main__':
    while True:
        n = int(input().strip())
        for _ in range(n):
            m = int(input().strip())
            data = list(map(int, input().strip().split()))
            data2 = data[:-1]
            nums = data + data2
            max_data = 0
            for index in range(len(nums)):
                nums2 = nums[:]
                max_num = nums2[index]
                num = 0
                for i in range(index + 1, len(nums2)):
                    if nums2[i - 1] > 0:
                        nums2[i] += nums2[i - 1]
                        num += 2
                    else:
                        num += 1
                    if num > m:
                        break
                    max_num = max(max_num, nums2[i])
                max_data = max(max_data, max_num)
            print(max_data)