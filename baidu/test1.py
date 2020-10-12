#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Five Little Monkeys Jumping on the Bed. It was bedtime. So five little monkeys took a bath. Five little Monkeys put on their pajamas.
Five 3
"""
if __name__ == '__main__':
    while True:
        try:
            sentence = input().strip()
            if not sentence:
                continue
            for c in sentence:
                if c.lower() not in 'abcdefghijklmnopqrstuvwxyz ':
                    sentence = sentence.replace(c, '')

            # sentence = sentence.replace('.', '')
            # print(sentence)
            words = sentence.split()

            # print(words)
            d = dict()
            for word in words:
                if word.lower() in d:
                    d[word.lower()][1] += 1
                else:
                    d[word.lower()] = [word, 1]

            items = list(d.values())
            items.sort(key=lambda x: x[1], reverse=True)
            max_value = items[0][1]
            # print(items)
            # max_value = max(d.values())

            # print(d)
            # print(max_value)
            res = list()
            for item in items:
                if item[1] == max_value:
                    res.append(item)

            # print(res)
            if len(res) == 1:
                target = res[0]
                print(target[0], target[1])
            else:
                # print('ok')
                index = 'z'
                for word in res:

                    if word[0][0].lower() <= index:
                        index = word[0][0].lower()
                        target = word
                print(target[0], target[1])
        except:
            break

