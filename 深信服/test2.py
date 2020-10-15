#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def max_number(self, arry):
        # write code here
        # return ''.join(map(str, arry))
        if not arry:
            return ''
        numsum = sum(arry)
        if numsum % 3 != 0:
            return ''
        else:
            arry.sort(reverse=True)
            numlistnew = [str(i) for i in arry]
            return ''.join(numlistnew)

if __name__ == '__main__':
    solution = Solution()
    print(solution.max_number([]))
