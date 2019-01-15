# import math
# import os
# import random
# import re
# import sys
#
# if __name__ == '__main__':
#     nameArr = []
#     scoreArr = []
#     for i in range(int(input())):
#         nameArr.append(input())
#         scoreArr.append(float(input()))
#
#     # print(nameArr)
#     # print(scoreArr)
#
#     minScore = min(scoreArr)
#
#     for i in range(scoreArr.count(minScore)):
#         nameArr.pop(scoreArr.index(minScore))
#         scoreArr.pop(scoreArr.index(minScore))
#
#     # print(nameArr)
#     # print(scoreArr)
#
#     minScore = min(scoreArr)
#     secondLowArr = []
#     for i in range(scoreArr.count(minScore)):
#         secondLowArr.append(nameArr[(scoreArr.index(minScore))])
#         nameArr.pop(scoreArr.index(minScore))
#
#     secondLowArr.sort()
#
#     for i in range(len(secondLowArr)):
#         print(secondLowArr[i])

if __name__ == '__main__':
    nestedList = []

    for _ in range(int(input())):
        nestedList.append([input(), float(input())])

    nestedList.sort(key=lambda x: x[1]) # sort by the first element
    #minScore = min(nestedList, key=lambda x: x[1])
    minCount = [i[1] for i in nestedList].count(nestedList[0][1])
    for i in range(minCount):
        nestedList.pop(0)

    #minScore = min(nestedList, key=lambda x: x[1])
    minCount = [i[1] for i in nestedList].count(nestedList[0][1])
    badStduents = []
    for i in range(minCount):
        #print(nestedList, end="\n")
        badStduents.append(nestedList[i][0])

    badStduents.sort(key=lambda x: x[0])
    for i in range(len(badStduents)):
        print(badStduents[i])