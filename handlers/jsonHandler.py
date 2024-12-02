from typing import SupportsIndex, TextIO


class jsonHandler:
    def __init__(self):
        pass


def useFile(filePath: str, modus: str):
    modusHandler(modus, filePath)


def modusHandler(modus: str, filePath: str):
    match modus:
        case "r":
            print("Read mode activated:")
            read(filePath)
        case "r+":
            print("Read and Write mode activated")
            readAndWrite(filePath, modus)
        case "w+":
            print("Write and Read mode activated, file will be overridden")
            writeToFile(filePath, modus)


def read(filePath: str):
    file = open(filePath, 'r')
    content = file.read()
    formattedContent = formatContent(content)
    dataArr = createDataArray(formattedContent)
    printContentWithLineNumber(dataArr)
    file.close()


def writeToFile(filePath: str, modus: str):
    file = open(filePath, modus)
    content = input("Please type in the new content to be added:\n"
                    "> ")
    file.write(content)
    file.close()


def readAndWrite(filePath: str, modus: str):
    choice = askUserForChoice()
    if choice == "change":
        ### retrieving data
        file = open(filePath, modus)
        content = file.read()
        formattedContent = formatContent(content)
        dataArray: [] = createDataArray(formattedContent)
        printContentWithLineNumber(dataArray)
        ### isolate line from array
        number = askForLineNumber(dataArray)
        lineToAdjust = getLineFromArray(dataArray, number)
        ### access key
        jsonDict = convertToDict(lineToAdjust)
        updatedDict = askForKeyAndUpdateDict(jsonDict)
        ### set new Value on chosen lineNumber
        print(updatedDict)
        dataArray[number] = convertDictToJson(updatedDict)
        printContentWithLineNumber(dataArray)
        saveNewFile(file, dataArray)
        ### saving content to file
    if choice == "append":
        file = open(filePath, 'a')
        appendToFile(file)
        file.close()


def formatContent(content: str):
    contentNoBreaks = removeLineBreaks(content)
    finalContent = removeWhitespace(contentNoBreaks)

    return finalContent


def removeLineBreaks(content: str):
    return content.replace("\n", "")


def removeWhitespace(content: str):
    return content.replace(" ", "")


def saveNewFile(file: TextIO, dataArray):
    file.seek(0)
    for item in dataArray:
        file.write(f'{item},')
    file.truncate()
    file.seek(0)
    content = file.read()


def askForKeyAndUpdateDict(jsonDict: dict):
    key = askForKey(jsonDict)
    newValue = input("Enter the new value:\n> ")
    jsonDict[key] = newValue
    return jsonDict


def convertDictToJson(jsonDict: dict):
    # replace ' with "
    lineToReplace = ""

    print(lineToReplace)
    return lineToReplace

def convertToDict(lineToAdjust):
    jsonObject: dict = {}
    jsonString = lineToAdjust.strip('{}')
    items = jsonString.split(',')

    for item in items:
        key, value = item.split(':')
        key = key.strip('"')
        value = value.strip('"')
        jsonObject[key] = value
    return jsonObject


def getLineFromArray(arr: [], number: int):
    print(f"You chose line {number} with content:\n{arr[number]}")
    return arr[number]


def appendToFile(file):
    newLine = input("Please enter your content:\n"
                    "> ")
    file.write(newLine + ",")


def printContentWithLineNumber(dataArray: []):
    for index, item in enumerate(dataArray):
        print(f"{index}. {item}")


def createDataArray(content: str):
    dataArr: [] = content.split('},')
    dataLen = len(dataArr) - 1
    dataArrComplete = []
    for index, item in enumerate(dataArr):
        if index < dataLen:
            dataArrComplete.append(item + '}')
        else:
            dataArrComplete.append(item)

    return dataArrComplete


def askForLineNumber(arr: []):
    convertedNumber = int(input("Which line do you want to change?\n"
                                "> "))
    arrLength = len(arr)
    valid = False
    while not valid:
        if convertedNumber >= 0 | convertedNumber < arrLength:
            valid = True
        else:
            convertedNumber = int(input("Which line do you want to change?\n"
                                        "> "))
    return convertedNumber


def askForKey(jsonDict: dict):
    print("\nAvailable keys are:", list(jsonDict.keys()), "\n")
    valid = False
    while not valid:
        choice = input("From which key would you like adjust the value?\n"
                       "> ")
        if choice in jsonDict.keys():
            return choice


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
