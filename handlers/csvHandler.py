from typing import override, List

from handlers.abstractHandler import Handler


class csvHandler(Handler):
    def convertLineToDict(self, lineToAdjust):
        pass

    def convertJStringToDict(self, jString: str):
        pass

    def transformJsonArrToDict(self, dataArr: []):
        pass

    def transformArrToDict(self, dataArr: [], originalFile: str):
        super().transformArrToDict(dataArr, originalFile)

    def __init__(self):
        pass

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
        choice: str = ""
        key = "csv"
        while choice != "exit":
            choice = self.askUserForChoice()
            if choice == "change":
                print("changes will be made")
                file = open(filePath, modus)
                content: str = file.read()
                dataArr: [] = self.createDataArray(content)
                super().printContentWithLineNumber(dataArr)
                number: int = self.askForLineNumber(dataArr)
                lineToAdjust: [] = self.getLineFromArray(dataArr, number)
                lineDict: dict = self.convertLineToDict(lineToAdjust, dataArr)
                updatedDict: dict = self.askForKeyAndUpdateDict(lineDict)
                dataArr[number]: str = self.convertBackToString(updatedDict)
                self.printContentWithLineNumber(dataArr)
                self.saveToFile(file, dataArr, key)
                file.close()
            if choice == "append":
                file = open(filePath, 'a')
                self.appendToFile(file)
                file.close()

    def writeToFile(self, filePath: str, modus: str):
        pass

    def appendToFile(self, file):
        super().appendToFile(file)

    def saveToFile(self, file, dataArr: [], originalFile: str):
        super().saveToFile(file, dataArr, originalFile)

    def convertBackToString(self, jsonDict: dict):
        dataArr: [] = []
        for key, value in jsonDict.items():
            dataArr.append(f'"{value}",')

        item: str = "".join(dataArr)
        updatedString = item.replace("\"", "")
        if updatedString.endswith(","):
            updatedString = updatedString[:-1]
        return updatedString

    def askForKeyAndUpdateDict(self, jsonDict: dict):
        return super().askForKeyAndUpdateDict(jsonDict)

    def askForKey(self, jsonDict: dict):
        return super().askForKey(jsonDict)

    @override
    def convertToDict(self, lineToAdjust, dataArr: []):
        """
        Converts a line of CSV data into a dictionary using the first line of the CSV as keys.

        Args:
            lineToAdjust (str): The CSV line to be converted into a dictionary.
            dataArr (List[str]):  The array of CSV lines, where the first line contains the keys.

        Returns:
            dict: A dictionary where the keys are from the first line of the CSV and the values are from the line to adjust.
        """
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
