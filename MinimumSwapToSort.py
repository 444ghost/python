#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    print(arr)

    chaoticArr = []
    count = 0

    for i in range(len(arr)):

        chaoticArr.append([i + 1, arr[i]])

    print("chaoticArr = ", end="")
    print(chaoticArr)

    for i in range(len(chaoticArr)):

        if chaoticArr[i][0] != chaoticArr[i][1] and chaoticArr[i][0] != -1:

            index = chaoticArr[i][0]
            data = chaoticArr[i][1]

            while index != chaoticArr[data - 1][1]:

                count += 1
                chaoticArr[data - 1][0] = -1
                data = chaoticArr[data - 1][1]

            count += 1
            chaoticArr[data - 1][0] = -1

    print("count = ", end="")
    print(count)

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
