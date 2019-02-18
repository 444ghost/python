#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the freqQuery function below.
def freqQuery(queries):
    dictionary = {}
    output = []

    for i in range(len(queries)):

        if queries[i][0] == 1:
            value = dictionary.get(queries[i][1])
            if value:
                dictionary.update({queries[i][1]: value + 1})
            else:
                dictionary.update({queries[i][1]: 1})
        elif queries[i][0] == 2:
            value = dictionary.get(queries[i][1])
            if value:
                dictionary.update({queries[i][1]: value - 1})
        elif queries[i][0] == 3:
            values = dictionary.values()
            if queries[i][1] in values:
                output.append("1")
            else:
                output.append("0")

    for i in output:
        print(i)

if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

