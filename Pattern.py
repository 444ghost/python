def print_rangoli(size):
    # your code goes here

    pattern = ""

    if size == 1:
        print("a")
        return

    for i in range(size - 1, -1, -1):
        pattern = "-" + chr(ord('a') + i) + pattern
        printPattern = (pattern[::-1][:len(pattern)] + pattern[3:]).center(((size * 2) - 1) + ((size * 2) - 2), "-")
        print(printPattern)
    for i in range(size - 1):
        pattern = printPattern[0:len(printPattern) // 2]
        printPattern = pattern + pattern[::-1][3:]
        print(printPattern.center(((size * 2) - 1) + ((size * 2) - 2), "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)