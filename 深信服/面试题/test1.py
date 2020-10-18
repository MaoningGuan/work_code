#!/usr/bin/env python
# -*- coding: utf-8 -*-
def quicksort(arr, left, right):
    if left < right:
        parrIndex = parrtition(arr, left, right)
        quicksort(arr, left, parrIndex - 1)
        quicksort(arr, parrIndex + 1, rigth)
    return arr


def parrIndex(arr, left, right):
    prior = left
    index = prior + 1
    i = index

    while i < right:
        if arr[i] < arr[prior]:
            swap(arr, i, index)
            index += 1
        i += 1

    swap(arr, prior, index - 1)
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    l = [1, 4, 5, 8, 2, 4, 5]
    print(quicksort(l, 0, len(l) - 1))
#     print('test')
