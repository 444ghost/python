import itertools

mList, n = input().strip().split(" ")

combination_with_replacementList = list(itertools.combinations_with_replacement(sorted(mList), int(n)))

for i in combination_with_replacementList:
    print(''.join(i))
