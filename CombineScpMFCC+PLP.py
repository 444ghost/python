import os

directories = ["test", "train"]

for x in directories:

    for j in range(1):

        inputFile = open("../mfcc/raw_mfcc_" + str(x) + "." + str(j + 1) + ".scp", "r")
        outputFile = open("raw_mfcc+plp_" + str(x) + "." + str(j + 1) + ".scp", "w")
        inputFileLines = inputFile.read().split("\n")

        for i in inputFileLines:
            if len(i) != 0:
                lineElements = i.split("/")
                lineElements[len(lineElements) - 2] = "mfcc+plp"
                tempElements = lineElements[len(lineElements) - 1].split(".")
                tempElements[0] = "raw_mfcc+plp_" + str(x)
                lineElements[len(lineElements) - 1] = ".".join(tempElements)
                print(lineElements[0] + "/" + "/".join(lineElements[1:]))
                outputFile.write(lineElements[0] + "/" + "/".join(lineElements[1:]) + "\n")

        inputFile.close()
        outputFile.close()

