#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    a, b = line.split(' ')
    print(int(a) + int(b))
