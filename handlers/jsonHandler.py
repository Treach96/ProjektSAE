from importlib.util import source_hash


class jsonHandler:
    def __init__(self):
        pass


def useFile(filePath, modus):
    modusHandler(modus, filePath)


def modusHandler(modus, filePath):
    match modus:
        case "r+":
            print("Read and Write mode activated")
            readAndWrite(filePath, modus)
        case "w+":
            print("Write and Read mode activated, file will be overridden")
            writeAndRead(filePath, modus)


def writeToFile(filePath, modus):
    file = open(filePath, modus)
    content = input("Please type in the new content to be added:\n"
                    "> ")
    print(content)
    file.write(content)
    file.close()


def writeAndRead(filePath, modus):
    file = open(filePath, modus)
    printFileWithLineNumbers(file)


def getKeysFromLineContent(lineContent):
    pass


def readAndWrite(filePath, modus):
    choice = askUserForChoice()
    if choice == "change":
        file = open(filePath)
        content: [] = file.readlines()

        printFileWithLineNumbers(content)
    #  lineContent = askForLine(file)
    #      keys, values = getKeysFromLineContent(lineContent)
    #    print(f" Key: {keys}, value: {values}")
    # File in verschiedene Zeilen aufsplitten
    # Zeilen in Array packen?
    # Anschließend Zeile auswählen
    # Dann dict aus Zeile erstellen und key auswählen
    # Value des Keys anpassen
    #       lineNr = askForLine(filePath)
    if choice == "append":
        printFileWithLineNumbers(filePath)
        file = open(filePath, 'a')
        appendToFile(file)
        file.close()
        printFile(filePath)


def appendToFile(file):
    newLine = input("Please enter your content:\n"
                    "> ")
    file.write('\n' + newLine)


def printFileWithLineNumbers(content):
    # first json File needs to be split on , so we can create an array of json stings
    # after that each element of the array should be printed as new line with new index number
    accessIndexOfList(content)

def printFile(filePath):
    file = open(filePath)
    for line in file:
        print(line)
    file.close()


def accessIndexOfList(content):
    split_data = content[0].split('},')
    print(split_data)

def lineToNumber():
    convertedNumber = int(input("Which line do you want to change?\n"
                                "> "))
    return convertedNumber


def askForLine(file):
    valid = False
    while not valid:
        lineNumber = lineToNumber()
        valid = checkLineNumber(lineNumber, file)
        file.seek(0)
        lineContent = file.readlines()
        print(
            f"You selected line: {lineNumber} and the content is: \n{lineContent[lineNumber]}")
    return lineContent[lineNumber]


def checkLineNumber(lineNumber, file):
    numberToCheck = lineNumber
    lineCounter = int(countLinesFromFile(file))
    if numberToCheck in range(lineCounter):
        return True
    else:
        return False


def countLinesFromFile(file):
    counter = 0
    file.seek(0)
    for line in enumerate(file):
        counter += 1
    return counter


def askForKey(filePath):
    key = input("Which key do want to change the value of?\n"
                "> ")
    value = getValueFromJsonWithKey(filePath, key)
    print(value)


def getValueFromJsonWithKey(filePath, key):
    with open(filePath, 'r') as file:
        data = file.read()
        json_data = eval(data)
        print(json_data.get(key))


def convertFileToDict(filePath):
    pass


def askUserForChoice():
    userInput = input(
        "\nWhat do you want to do here? Select number to choose:\n"
        "1. change value of key\n"
        "2. append new entry\n"
        "> ")
    match userInput:
        case "1":
            return "change"
        case "2":
            return "append"
