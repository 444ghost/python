n = int(input())
dictionary = {}

for i in range(n):
    line = list(input().strip().split(" "))
    dictionary.setdefault(line[0], line[1])
    print(line)

for i in range(n):
    key = input()
    value = dictionary.get(key, -1)
    if  value != -1:
        print(key + "=" + value)
    else:
        print("Not found")