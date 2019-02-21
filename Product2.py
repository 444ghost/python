import itertools

productList = list(itertools.product("AB", "ab"))

for i in productList:
    print(''.join(i))