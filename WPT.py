
def WPT_low(signal, output, j):

    if j == 0:
        output.extend(signal)
        return

    buffer = []
    avgList = []
    diffList= []

    for i in signal:

        buffer.append(i)
        if len(buffer) == 2:
            avgList.append((buffer[0] + buffer[1]) / 2)
            diffList.append((buffer[0] - buffer[1]) / 2)
            buffer.clear()

    print(avgList)
    print(diffList)
    output.extend(diffList)
    j -= 1
    WPT_low(avgList, output, j)

    return

signal = list(range(1, 17))
signal2 = [1, 2]
signal2 = signal2 * 8
output = []
j = 3

print(signal)
WPT_low(signal, output, 3)
print(output)

