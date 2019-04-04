import os

for x in "test", "train":

    inputFile = open(x + "/" + "feats.scp", "r+")
    outputFile = open(x + "/" + "feats2.scp", "w+")

    inputFileLines = inputFile.read().split("\n")

    for i in inputFileLines:
        if len(i) != 0:
            line = i
            if line.count("plp"):
                outputFile.write(line.replace("plp", "mfcc+plp") + "\n")
            else:
                outputFile.write(line.replace("mfcc", "mfcc+plp") + "\n")

    inputFile.close()
    outputFile.close()
    os.rename(x + "/feats.scp", x + "/" + "feats_backup.scp")
    os.rename(x + "/feats2.scp", x + "/" + "feats.scp")
#
# for x in "test/split2", "test/split10", "train/split2", "train/split4":
#     for i in range(int(x.split("split")[1])):
#         inputFile = open(x + "/" + str(i + 1) + "/" + "feats.scp", "r")
#         outputFile = open(x + "/" + str(i + 1) + "/" + "feats2.scp", "w")
#
#         inputFileLines = inputFile.read().split("\n")
#
#         for j in inputFileLines:
#             if len(j) != 0:
#                 line = j
#                 if line.count("plp"):
#                     outputFile.write(line.replace("plp", "mfcc+plp") + "\n")
#                 else:
#                     outputFile.write(line.replace("mfcc", "mfcc+plp") + "\n")
#
#         inputFile.close()
#         outputFile.close()
#         os.rename(x + "/" + str(i + 1) + "/" + "feats.scp", x + "/" + str(i + 1) + "/" + "feats_backup.scp")
#         os.rename(x + "/" + str(i + 1) + "/" + "feats2.scp", x + "/" + str(i + 1) + "/" + "feats.scp")
