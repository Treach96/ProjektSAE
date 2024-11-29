class jsonHandler:
    def __init__(self):
        pass


def useFile(filePath, modus):
    modusHandler(modus, filePath)


def modusHandler(modus, filePath):
    match modus:
        case "r":
            print("Read mode activated:")
            read(filePath)
        case "r+":
            print("Read and Write mode activated")
            readAndWrite(filePath, modus)
        case "w+":
            print("Write and Read mode activated, file will be overridden")
            writeAndRead(filePath, modus)

def read(filePath: str):
    file = open(filePath, 'r')
    content = file.read()
    dataArr = createDataArray(content)
    printContentWithLineNumber(dataArr)

def writeToFile(filePath, modus):
    file = open(filePath, modus)
    content = input("Please type in the new content to be added:\n"
                    "> ")
    print(content)
    file.write(content)
    file.close()

def writeAndRead(filePath, modus):
    ...


def getKeysFromLineContent(lineContent):
    ...


def readAndWrite(filePath, modus):
    choice = askUserForChoice()
    if choice == "change":
        file = open(filePath, modus)
        content = file.read()
        dataArray: [] = createDataArray(content)
        printContentWithLineNumber(dataArray)
        lineToAdjust = getLineFromArray(dataArray)
        # print(lineToAdjust)
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
        file = open(filePath, 'a')
        appendToFile(file)
        file.close()


def getLineFromArray(arr: []):
    number = askForLineNumber(arr)
    print(f"You chose line {number} with content:\n{arr[number]}")
    return arr[number]


def appendToFile(file):
    newLine = input("Please enter your content:\n"
                    "> ")
    file.write(newLine + ",")


def printContentWithLineNumber(dataArray: []):
    for index, item in enumerate(dataArray):
        print(f"{index}. {item}")


def createDataArray(content):
    dataArr: [] = content.split('},')
    dataComplete: [] = [item + '}' if i < len(dataArr) - 1 else item for i, item
                        in enumerate(dataArr)]
    return dataComplete


def askForLineNumber(arr: []):
    convertedNumber = int(input("Which line do you want to change?\n"
                                "> "))
    arrLenght = len(arr)
    valid = False
    while not valid:
        if convertedNumber >= 0 | convertedNumber < arrLenght:
            valid = True
        else:
            convertedNumber = int(input("Which line do you want to change?\n"
                                        "> "))
    return convertedNumber


def askForKey(arr: []):
    ...


def getValueFromJsonWithKey(filePath, key):
    with open(filePath, 'r') as file:
        data = file.read()
        json_data = eval(data)
        print(json_data.get(key))


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
