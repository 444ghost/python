#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(chaoticQueue):
    count = 0
    n = len(chaoticQueue)

    for i in range(n - 1, 0, -1):
        if chaoticQueue[i] != (i + 1):
            if (i - 1) >= 0 and chaoticQueue[i - 1] == (i + 1):
                count = count + 1
                temp = chaoticQueue[i]
                chaoticQueue[i] = chaoticQueue[i - 1]
                chaoticQueue[i - 1] = temp
            elif (i - 2) >= 0 and chaoticQueue[i - 2] == (i + 1):
                count = count + 2
                chaoticQueue[i - 2] = chaoticQueue[i - 1]
                chaoticQueue[i - 1] = chaoticQueue[i]
                chaoticQueue[i] = i + 1
            else:
                print("Too chaotic")
                return

    # for i in range(len(chaoticQueue)):
    #     if (chaoticQueue[i] - (i + 1)) >= 3:
    #         print("Too chaotic")
    #         return
    #
    # for i in range(len(chaoticQueue)):
    #     if (i + 1) != chaoticQueue[i] and i != len(chaoticQueue) - 1:
    #         index = chaoticQueue.index(i + 1)
    #         temp = chaoticQueue[i]
    #         chaoticQueue[i] = chaoticQueue[index]
    #         chaoticQueue.pop(index)
    #         chaoticQueue.insert(i + 1, temp)
    #         count = count + (index - i)

    print(count)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
