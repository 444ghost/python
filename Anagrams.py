#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    dictionary = {}

    for i in range(len(s)):
        for j in range(i, len(s)):
            dictionary.setdefault(len(s[i:j + 1]), []).append(str(s[i:j + 1]))

    # print(dictionary)
    count = 0

    for i in range(len(dictionary)):
        for j in range(len(dictionary.get(i + 1))):
            for k in range(j, len(dictionary.get(i + 1))):


                # setA = set(dictionary.get(i + 1)[j])
                # setB = set(dictionary.get(i + 1)[k])
                #
                # if setA == setB and j != k:
                if sorted(dictionary.get(i + 1)[j]) == sorted(dictionary.get(i + 1)[k]) and j != k:
                    count += 1
                    # print(dictionary.get(i + 1)[j], end="")
                    # print(dictionary.get(i + 1)[k], end=" ")
                # print(dictionary.get(i + 1)[j], end="")
                # print(dictionary.get(i + 1)[k], end=" ")
    print(count)
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

