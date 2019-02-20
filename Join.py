
n = int(input())

for i in range(n):

        arr = []
        for j in range(i + 1):
            arr.append(j + 1)
        a = "".join(str(x) for x in arr)
        b = "".join(str(x) for x in arr[::-1])
        print(a + b[1:])
