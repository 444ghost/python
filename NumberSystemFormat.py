def print_formatted(number):
    # your code goes here

    n = len(format(number, 'b')) + 1
    for i in range(1, number + 1):
        print(str(i).rjust(n - 1, " ") + format(i, 'o').rjust(n, " ") + format(i, 'x').rjust(n, " ").upper() + format(i, 'b').rjust(n, " "))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)