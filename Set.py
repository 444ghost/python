# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
list1 = set(map(int, input().split(" ")))
m = input()
list2 = set(map(int, input().split(" ")))
list3 = sorted([*list1.difference(list2).union(list2.difference(list1))], key=int)
print(*list3, sep="\n")
