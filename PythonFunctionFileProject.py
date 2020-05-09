projectTwitterDataFile = open("files/project_twitter_data.csv", "r")
resultingDataFile = open("files/resulting_data.csv", "w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("files/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(str1):
    str1 = strip_punctuation(str1)
    listStr1 = str1.split()

    count = 0
    for word in listStr1:
        if word in positive_words:
                count += 1
    return count


negative_words = []
with open("files/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(str2):
    str2 = strip_punctuation(str2)
    listStr2 = str2.split()

    count = 0
    for word in listStr2:
        if word in negative_words:
            count += 1
    return count


def strip_punctuation(str):
    for char in punctuation_chars:
        str = str.replace(char, "")
    return str


def writeInDataFile(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    lines = projectTwitterDataFile.readlines()
    headerDontUsed = lines.pop(0)
    for linesTD in lines:
        listTD = linesTD.strip().split(',')
        resultingDataFile.write(
            "{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]),
                                        (get_pos(listTD[0]) - get_neg(listTD[0]))))
        resultingDataFile.write("\n")


writeInDataFile(resultingDataFile)
projectTwitterDataFile.close()
resultingDataFile.close()