#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"112" 1
"112" 2
"""


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param content string字符串 需要执行消除的内容
# @param bomb char字符型 炸弹字符
# @return string字符串
#
import collections

class Solution:
    def make_cancellation(self, content, bomb):
        if not content:
            return ''

        queue = collections.deque(list(content))
        target = queue.popleft()
        res = []
        while queue:
            c = queue.popleft()
            if target != c:
                res.append(target)
                target = c
                if not queue:
                    res.append(target)
            else:
                if target == bomb:
                    if queue:
                        queue.popleft()
                    else:
                        break
                    if queue:
                        target = queue.popleft()
                        if not queue:
                            res.append(target)
                            break
                    else:
                        break
                else:
                    if queue:
                        target = queue.popleft()
                        if not queue:
                            res.append(target)
                            break
                    else:
                        break
        return ''.join(res)



if __name__ == '__main__':
    solution = Solution()
    content = ''
    bomb = '1'

    print(solution.make_cancellation(content, bomb))
