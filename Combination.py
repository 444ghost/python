import itertools

mList, n = input().strip().split(" ")

# combinationList = list(itertools.combinations(sorted(mList), int(n)))
# print(combinationList)
for i in range(int(n)):
    mTuple = list(itertools.combinations(sorted(mList), i + 1))
    for j in mTuple:
        print("".join(j))