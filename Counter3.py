import collections

n = int(input())
lines = []

for i in range(n):
    lines.append(input().strip())

# print(lines)

counter = collections.Counter(lines)

# print(counter)

print(len(counter))
for i in counter:
    print(counter.get(i), end=" ")