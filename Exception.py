# Write your code here
class Calculator(object):
    def __init__(self):
        self.object = object

    def power(self, a, b):
        self.a = a
        self.b = b

        if self.a >= 0 and self.b >= 0:
            return (a ** b)
        else:
            e = "n and p should be non-negative"
        return e


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)   