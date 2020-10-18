#!/usr/bin/env python
# -*- coding: utf-8 -*-
def factor(N):
    N2 = N
    a = list(range(1, N+1))
    while N2 > 1:
        N1 = N2%2
