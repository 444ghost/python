from collections import OrderedDict

n = int(input())
dictionary = OrderedDict()

for i in range(n):
    line = input().strip().split()
    key = line[:len(line) - 1]
    value = int(line[len(line) - 1])
    keyString = " ".join(key)
    dictionary.update({" ".join(key): int(dictionary.get(keyString, 0)) + value}) # same as "".join(key) == *key

for i in dictionary.keys():
    print(i + " " + str(dictionary.get(i)))