from collections import Counter

logo = input()
logoChars = list(sorted(logo))
logoCounter = Counter(logoChars)
#
# print(logoCounter.most_common(3))

for i in logoCounter.most_common(3):
    print(str(i[0]) + " " + str(i[1]))

# for i in logoCounter.keys():
#     print(i)
#
# for i in logoCounter.values():
#     print(i)
#
# for i in range(3):

