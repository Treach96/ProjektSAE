from handlers.abstractHandler import Handler


class jsonHandler(Handler):
    def askForKey(self, jsonDict: dict):
        return super().askForKey(jsonDict)

    def askForKeyAndUpdateDict(self, jsonDict: dict):
        return super().askForKeyAndUpdateDict(jsonDict)

    def convertToDict(self, lineToAdjust):
        jsonDict: dict = {}
        jsonString: str = lineToAdjust.strip('{}')
        items: [str] = jsonString.split(',')

        for item in items:
            key, value = item.split(':')
            key: str = key.strip('"')
            value: str = value.strip('"')
            jsonDict[key]: dict = value
        print(jsonDict)
        return jsonDict

    def printContentWithLineNumber(self, dataArray: []):
        super().printContentWithLineNumber(dataArray)

    def askUserForChoice(self):
        return super().askUserForChoice()

    def getLineFromArray(self, arr: [], number: int):
        return super().getLineFromArray(arr, number)

    def askForLineNumber(self, arr: []):
        return super().askForLineNumber(arr)

    def createDataArray(self, content: str):
        dataArr: [] = content.split('},')
        dataLen: int = len(dataArr) - 1
        dataArrComplete: [] = []
        for index, item in enumerate(dataArr):
            if index < dataLen:
                dataArrComplete.append(item + '}')
            else:
                dataArrComplete.append(item)

        return dataArrComplete

    def __init__(self):
        pass

    def useFile(self, filePath: str, modus: str):
        super().modusHandler(modus, filePath)

    def modusHandler(self, modus: str, filePath: str):
        super().modusHandler(modus, filePath)

    def read(self, filePath: str):
        file = open(filePath, 'r')
        content: str = file.read()
        formattedContent: str = formatContent(content)
        dataArr: [] = self.createDataArray(formattedContent)
        self.printContentWithLineNumber(dataArr)
        file.close()

    def writeToFile(self, filePath: str, modus: str):
        file = open(filePath, modus)
        content: str = input("Please type in the new content to be added:\n"
                             "> ")
        file.write(content)
        file.close()

    def readAndWrite(self, filePath: str, modus: str):
        choice: str = self.askUserForChoice()
        if choice == "change":
            ### retrieving data
            file = open(filePath, modus)
            content: str = file.read()
            formattedContent: str = formatContent(content)
            dataArray: [] = self.createDataArray(formattedContent)
            self.printContentWithLineNumber(dataArray)
            ### isolate line from array
            number: int = self.askForLineNumber(dataArray)
            lineToAdjust: [str] = self.getLineFromArray(dataArray, number)
            ### access key
            jsonDict: dict = self.convertToDict(lineToAdjust)
            ### set new Value on chosen lineNumber
            updatedDict: dict = self.askForKeyAndUpdateDict(jsonDict)
            dataArray[number]: str = convertBackToString(updatedDict)
            self.printContentWithLineNumber(dataArray)
            ### saving content to file
            saveToFile(file, dataArray)
        if choice == "append":
            file = open(filePath, 'a')
            appendToFile(file)
            file.close()


def formatContent(content: str):
    contentNoBreaks: str = removeLineBreaks(content)
    finalContent: str = removeWhitespace(contentNoBreaks)
    return finalContent


def removeLineBreaks(content: str):
    return content.replace("\n", "").replace("[", "").replace("]", "")


def removeWhitespace(content: str):
    return content.replace(" ", "").replace("\\", "")


def saveToFile(file, dataArray):
    file.seek(0)
    for item in dataArray:
        file.write(f'{item},')
    file.truncate()


def convertBackToString(jsonDict: dict):
    dataArr: [] = []
    partString: str = ''
    for key, value in jsonDict.items():
        dataArr.append(f'"{key}":"{value}"')

    # output: ['id:10', 'player_name:Emlynn', 'char_name:Bengle', 'Hp:31']
    for index, item in enumerate(dataArr):
        if index < len(dataArr) - 1:
            partString += f'{item},'
        else:
            partString += f'{item}'

    jsonString: str = "{" + partString + "}"
    return jsonString


def convert2(jsonDict: dict):
    dataArr: [] = []
    for key, value in jsonDict.items():
        dataArr.append(f'"{key}":"{value}"')

    x = "{" + ",".join(dataArr) + "}"
    print("Version 2: ", x)


def appendToFile(file):
    newLine: str = input("Please enter your content:\n"
                    "> ")
    file.write(newLine + ",")


def printContentWithLineNumber(dataArray: []):
    for index, item in enumerate(dataArray):
        print(f"{index}. {item}")


def askUserForChoice():
    userInput: str = input(
        "\nWhat do you want to do here? Select number to choose:\n"
        "1. change value of key\n"
        "2. append new entry\n"
        "> ")
    match userInput:
        case "1":
            return "change"
        case "2":
            return "append"
