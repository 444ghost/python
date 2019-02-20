import itertools

mList, n = input().strip().split(" ")

combinationList = list(itertools.combinations(sorted(mList), int(n)))

for i in combinationList:
    print(''.join(i))