import itertools

n, M = map(int, input().strip().split(" "))

inputList = []

for i in range(n):
    inputList.append(list(map(int, input().strip().split(" ")))[1:])

#print(inputList)

combinationList = list(itertools.product(*inputList))
numList = []

for i in combinationList:
    numList.append(sum(x * x for x in i) % M)

print(max(numList))

#input:
# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10
