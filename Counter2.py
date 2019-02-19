from collections import Counter

n = int(input())
s = list(map(int, input().strip().split(" ")))

rooms = Counter(s)

# print(rooms)

for i in rooms:
    # print(i)
    # print(rooms[i])

    if rooms[i] != n:
        print(i)
        break