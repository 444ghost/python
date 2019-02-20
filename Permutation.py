import itertools

mList, n = input().strip().split(" ")

permutationList = list(itertools.permutations(sorted(mList), int(n)))

for i in permutationList:
    print(''.join(i))
