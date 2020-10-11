#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from utils import ListNode


def main(s):
    hashset = set()
    res = ''
    for c in s:
        if c not in hashset:
            hashset.add(c)
            res += c
    return res


if __name__ == '__main__':
    s = '12ere25555'
    print(main(s))