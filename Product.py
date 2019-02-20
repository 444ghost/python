import itertools

mList, n = input().strip().split(" ")

productList = list(itertools.product(sorted(mList), repeat=int(n)))

for i in productList:
    print(''.join(i))