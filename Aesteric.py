if __name__ == '__main__':
    n = int(input())
    student_marks = {} # dictionary
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    avg = 0;
    for i in range(len(student_marks[query_name])):
        avg = avg + student_marks[query_name][i]
    avg = avg/len(student_marks[query_name])

    print("%.2f" % avg)

