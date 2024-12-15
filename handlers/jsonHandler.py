from typing import override

from handlers.abstractHandler import Handler


class jsonHandler(Handler):

    def transformJsonArrToDict(self, dataArr: []):
        pass

    def convertJStringToDict(self, jString: str):
        super().convertJStringToDict(jString)

    def transformArrToDict(self, dataArr: [], originalFile: str):
        super().transformArrToDict(dataArr, originalFile)

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

    def readAndWrite(self, filePath: str, modus: str):
        choice: str = ""
        originalFile = "json"
        while choice != "exit":
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
                jsonDict: dict = self.convertLineToDict(lineToAdjust)
                ### set new Value on chosen lineNumber
                updatedDict: dict = self.askForKeyAndUpdateDict(jsonDict)
                dataArray[number]: str = self.convertBackToString(updatedDict)
                self.printContentWithLineNumber(dataArray)

                ### saving content to file
                self.saveToFile(file, dataArray, originalFile)
                file.close()
                # todo: loop glätten
            if choice == "append":
                file = open(filePath, 'a')
                self.appendToFile(file)
                file.close()

    def writeToFile(self, filePath: str, modus: str):
        super().writeToFile(filePath, modus)

    def appendToFile(self, file):
        super().appendToFile(file)

    def saveToFile(self, file, dataArr: [], originalFile: str):
        super().saveToFile(file, dataArr, originalFile)

    def convertBackToString(self, jsonDict: dict):
        dataArr: [] = []
        partString: str = ''
        for key, value in jsonDict.items():
            if isCastableToInt(value):
                dataArr.append(f'"{key}":{value}')
            else:
                dataArr.append(f'"{key}":"{value}"')

        # output: ['id:10', 'player_name:Emlynn', 'char_name:Bengle', 'Hp:31']
        for index, item in enumerate(dataArr):
            if index < len(dataArr) - 1:
                partString += f'{item},'
            else:
                partString += f'{item}'

        jsonString: str = "{" + partString + "}"
        return jsonString

    def askForKey(self, jsonDict: dict):
        return super().askForKey(jsonDict)

    def askForKeyAndUpdateDict(self, jsonDict: dict):
        return super().askForKeyAndUpdateDict(jsonDict)

    @override
    def convertLineToDict(self, lineToAdjust: str):
        jsonDict: dict = super().convertJStringToDict(lineToAdjust)

        return jsonDict

    def printContentWithLineNumber(self, dataArray: []):
        super().printContentWithLineNumber(dataArray)

    def askUserForChoice(self):
        return super().askUserForChoice()

    def getLineFromArray(self, arr: [], number: int):
        return super().getLineFromArray(arr, number)

    def askForLineNumber(self, arr: []):
        return super().askForLineNumber(arr)

    # todo: use dict to save format and not dataArray
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


def formatContent(content: str):
    contentNoBreaks: str = removeLineBreaks(content)
    finalContent: str = removeWhitespace(contentNoBreaks)
    return finalContent


def isCastableToInt(value: str):
    try:
        int(value)
        return True
    except ValueError:
        return False


def removeLineBreaks(content: str):
    return content.replace("\n", "").replace("[", "").replace("]", "")


def removeWhitespace(content: str):
    return content.replace(" ", "").replace("\\", "")


def convert2String(jsonDict: dict):
    dataArr: [] = []
    for key, value in jsonDict.items():
        if isinstance(value, int):
            dataArr.append(f'"{key}":{value}')
        else:
            dataArr.append(f'"{key}":"{value}"')

    x = "{" + ",".join(dataArr) + "}"
    return x


def printContentWithLineNumber(dataArray: []):
    for index, item in enumerate(dataArray):
        print(f"{index}. {item}")


def askUserForChoice():
    userInput: str = input(
        "\nWhat do you want to do here? Select number to choose:\n"
        "1. change value of key\n"
        "2. append new entry\n"
        "3. exit"
        "> ")
    match userInput:
        case "1":
            return "change"
        case "2":
            return "append"
        case "3":
            exit()
