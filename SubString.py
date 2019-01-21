def count_substring(string, sub_string):

    globalCount = 0
    for i in range(len(string) - len(sub_string) + 1):
        print(string[i:len(sub_string) + i])
        if string[i:len(sub_string) + i] == sub_string:
            globalCount = globalCount + 1

    return globalCount


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)

    print(count)