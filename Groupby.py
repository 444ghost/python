import itertools

for k, c in itertools.groupby(input()):
    print("(" + str(len(list(c))) + ", " + str(k) + ")", end=" ")
