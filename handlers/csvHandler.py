from typing import override, List

from handlers.abstractHandler import Handler


class csvHandler(Handler):

    def askForKeyAndUpdateDict(self, jsonDict: dict):
        return super().askForKeyAndUpdateDict(jsonDict)

    def askForKey(self, jsonDict: dict):
        return super().askForKey(jsonDict)

    @override
    def convertToDict(self, lineToAdjust, dataArr: []):
        csvDict = {}
        keys: str = dataArr[0]
        keys: List[str] = keys.split(",")
        items = lineToAdjust.split(',')
        for index, item in enumerate(items):
            value = item
            key = keys[index]
            csvDict[key] = value
        return csvDict

    def getLineFromArray(self, arr: [], number: int):
        return super().getLineFromArray(arr, number)

    def askForLineNumber(self, arr: []):
        return super().askForLineNumber(arr)

    def askUserForChoice(self):
        choice = super().askUserForChoice()
        return choice

    def printContentWithLineNumber(self, dataArray: []):
        super().printContentWithLineNumber(dataArray)

    def createDataArray(self, content: str):
        dataArray: [] = content.splitlines()
        return dataArray

    def useFile(self, filePath: str, modus: str):
        super().useFile(filePath, modus)

    def modusHandler(self, modus: str, filePath: str):
        super().modusHandler(modus, filePath)

    def read(self, filePath: str):
        file = open(filePath, 'r')
        content = file.read()
        dataArr: [] = self.createDataArray(content)
        super().printContentWithLineNumber(dataArr)
        print(dataArr)
        file.close()

    def readAndWrite(self, filePath: str, modus: str):
        choice = self.askUserForChoice()
        match choice:
            case "change":
                print("changes will be made")
                file = open(filePath, modus)
                content = file.read()
                dataArr: [] = self.createDataArray(content)
                super().printContentWithLineNumber(dataArr)
                number = self.askForLineNumber(dataArr)
                lineToAdjust = self.getLineFromArray(dataArr, number)
                lineDict = self.convertToDict(lineToAdjust, dataArr)
                updatedDict = self.askForKeyAndUpdateDict(lineDict)
                print(updatedDict)
            case "append":
                print("Content will be appended")

    def writeToFile(self, filePath: str, modus: str):
        pass

    def __init__(self):
        pass
