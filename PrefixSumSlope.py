#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # base = [0] * n

    # for i in range(len(queries)):

    #     for j in range(queries[i][0] - 1, queries[i][1]):

    #         base[j] = base[j] + queries[i][2]
    # return max(base)

    list = [0] * (n + 1)
    for i in range(len(queries)):
        x = queries[i][0]
        y = queries[i][1]
        incr = queries[i][2]
        list[x - 1] += incr
        if ((y) <= len(list)): list[y] -= incr
        # print(list)
    maximum = x = 0
    print(list)
    for i in list:
        x = x + i
        if (maximum < x): maximum = x
    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
