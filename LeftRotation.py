import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):

    if d > len(a):
        shift = len(a) % d
    elif d < len(a):
        shift = d
    elif d == len(a):
        return a

    tempArray = []
    tempArray = a[shift:len(a)]
    tempArray.extend(a[0:shift])

    return tempArray
if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)

