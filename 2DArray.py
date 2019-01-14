import math
import os
import random
import re
import sys

def hourglassSum(arr):

    maxHourGlassSum = arr[0][0] + arr[0][1] + arr[0][2] + arr[1][1] + arr[2][0] + arr[2][1] + arr[2][2]
    for i in range(4):
        for j in range(4):
            local = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if(local > maxHourGlassSum):
                maxHourGlassSum = local # hey
    return maxHourGlassSum

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(hourglassSum(arr))