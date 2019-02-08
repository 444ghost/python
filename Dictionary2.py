#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    magazineSet = set(magazine)
    flag = True

    # print(magazineDic)

    for i in range(len(note)):

        if note[i] not in magazineSet:
            print("No")
            flag = False
            break
        else:

            try:
                index = magazine.index(note[i])
                magazine.pop(index)
            except ValueError:
                print("No")
                flag = False
                break

    if flag:
        print("Yes")
    # magazineDic = {}
    # magazineSet = set(magazine)
    # flag = True

    # for i in magazineSet:
    #     magazineDic.setdefault(i, magazine.count(i))

    # # print(magazineDic)

    # for i in range(len(note)):

    #     if note[i] not in magazineSet:
    #         print("No")
    #         flag = False
    #         break
    #     else:

    #         if magazineDic[note[i]] == 0:
    #             print("No")
    #             flag = False
    #             break
    #         magazineDic[note[i]] -= 1

    # if flag:
    #     print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

