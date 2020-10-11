#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
And millionaires will hold 46% of 4000 total 2020 wealth by 2019, the report says. This ratio is likely to increase in 2020.
"""
import re

if __name__ == '__main__':
    while True:
        try:
            strs = input()
            if strs != '':
                pattern = '[1-3]{1}[0-9]{1}[0-9]{1}[0-9]*'

                res = re.findall(pattern, strs)
                hashset = set()
                years = []

                # print(res)

                for year in res:
                    # year = ''.join(res[i: i + 4])
                    if len(year) > 4:
                        continue
                    if year not in hashset:
                        hashset.add(year)
                        years.append(year)
                    # print(year, end=' ')
                # print(''.join(res[i: i + 4])
                # years.append(''.join(res[i: i + 4]))
                # print(years)
                # print(res)
                for year in years:
                    print(year, end=' ')

        except:
            break
