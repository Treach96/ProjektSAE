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


def readAndWrite(filePath, modus):
    choice = askUserForChoice()
    if choice == "change":
        print("change")
        file = open(filePath, modus)
        printFileWithLineNumbers(filePath)
        line = askForLine(file)
        # todo: read keys from file
        key = askForKey(filePath)
    if choice == "append":
        printFileWithLineNumbers(filePath)
        file = open(filePath, 'a')
        appendToFile(file)
        file.close()
        printFile(filePath)
    file.close()


def appendToFile(file):
    newLine = input("Please enter your content:\n"
                    "> ")
    file.write(newLine + '\n')


def printFileWithLineNumbers(filePath):
    file = open(filePath)
    for index, line in enumerate(file):
        print(index, line)
    file.close()


def printFile(filePath):
    file = open(filePath)
    for line in file:
        print(line)
    file.close()


def lineToNumber():
    convertedNumber = int(input("Which line do you want to change?\n"
                                "> "))
    return convertedNumber


def askForLine(file):
    valid = False
    while not valid:
        lineNumber = lineToNumber()
        valid = checkLineNumber(lineNumber, file)
    return lineNumber


def checkLineNumber(lineNumber, file):
    numberToCheck = lineNumber
    lineCounter = int(countLinesFromFile(file))
    if numberToCheck in range(lineCounter):
        return True
    else:
        return False


def countLinesFromFile(file):
    counter = 0
    for index, line in enumerate(file):
        counter += index
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
    # todo: convert file to dict so key of json can be used
    file = open(filePath)
    data = file.read()
    dict = eval(data)

    # Remove surrounding brackets and split file
    items = data.strip()[1:-1].split('},{')
    result = []
    for item in items:
        # Add cury brackets back to each item
        item = '{' + item + '}'
        # Convert the string representation of a dict in and actuallz dict
        item_dict = eval(item)
        result.append(item_dict)
    return result



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
