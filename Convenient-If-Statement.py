# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split(" "))

array = list(map(int, input().split(" ")))

setA = set(map(int, input().split(" ")))
setB = set(map(int, input().split(" ")))

count = 0

for i in range(len(array)):
    if array[i] in setA:
        count += 1
    if array[i] in setB:
        count -= 1
print(count)
