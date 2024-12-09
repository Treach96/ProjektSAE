from abc import ABC
from abc import abstractmethod


class Handler(ABC):

    @abstractmethod
    def useFile(self, filePath: str, modus: str):
        self.modusHandler(modus, filePath)

    @abstractmethod
    # todo: add loop for content
    def modusHandler(self, modus: str, filePath: str):
        match modus:
            case "r":
                print("Read mode activated:")
                self.read(filePath)
            case "r+":
                print("Read and Write mode activated. File will be adjusted.")
                self.readAndWrite(filePath, modus)
            case "w+":
                print("Write and Read mode activated. File will be replaced.")
                self.writeToFile(filePath, modus)

    @abstractmethod
    def saveToFile(self, file, dataArr: []):
        file.seek(0)
        saveFormat = askForSavingFormat()
        if saveFormat == "default":
            savingArr(file, dataArr)
        if saveFormat == "json":
            convertedArr: [] = convertToJson(dataArr)
            savingArr(file, convertedArr)
        if saveFormat == "csv":
            convertedArr: [] = convertToCsv(dataArr)
            savingArr(file, convertedArr)
        # todo: ask for futher changes? no-> exit
        choice: str = input("Do you want to do something else with this file?\n"
                            "chose \"yes\" or \"no\"\n"
                            "> ")
        if choice == "no":
            exit()

    @abstractmethod
    def convertBackToString(self, jsonDict: dict):
        pass

    @abstractmethod
    def read(self, filePath: str):
        pass

    @abstractmethod
    def readAndWrite(self, filePath: str, modus: str):
        pass

    @abstractmethod
    def writeToFile(self, filePath: str, modus: str):
        file = open(filePath, modus)
        content: str = input("Please type in the new content to be added:\n"
                             "> ")
        file.write(content)
        file.close()

    @abstractmethod
    def createDataArray(self, content: str):
        pass

    @abstractmethod
    def convertToDict(self, lineToAdjust):
        pass

    @abstractmethod
    def appendToFile(self, file):
        newLine: str = input("Please enter your content:\n"
                             "> ")
        file.write(newLine + ",")

    @abstractmethod
    def askForKeyAndUpdateDict(self, jsonDict: dict):
        key = self.askForKey(jsonDict)
        newValue = input("Enter the new value:\n> ")
        jsonDict[key] = newValue
        return jsonDict

    @abstractmethod
    def askForKey(self, jsonDict: dict):
        print("\nAvailable keys are:", list(jsonDict.keys()), "\n")
        valid = False
        while not valid:
            choice = input("From which key would you like adjust the value?\n"
                           "> ")
            if choice in jsonDict.keys():
                return choice

    @abstractmethod
    def getLineFromArray(self, arr: [], number: int):
        print(f"You chose line {number} with content:\n{arr[number]}")
        return arr[number]

    @abstractmethod
    def askForLineNumber(self, arr: []):
        convertedNumber = int(
            input("Which line do you want to change?\nInsert number"
                  "> "))
        arrLength = len(arr)
        valid = False
        while not valid:
            if convertedNumber >= 0 | convertedNumber < arrLength:
                valid = True
            else:
                convertedNumber = int(
                    input("Which line do you want to change?\n"
                          "> "))
        return convertedNumber

    @abstractmethod
    def printContentWithLineNumber(self, dataArray: []):
        for index, item in enumerate(dataArray):
            print(f"{index}. {item}")

    @abstractmethod
    def askUserForChoice(self):
        userInput = input(
            "\nWhat do you want to do here? Select number to choose:\n"
            "1. change value of key\n"
            "2. append new entry\n"
            "3. exit\n"
            "> ")
        match userInput:
            case "1":
                return "change"
            case "2":
                return "append"
            case "3":
                exit()


def savingArr(file, dataArr: []):
    dataLen = len(dataArr) - 1
    for index, item in enumerate(dataArr):
        if index == dataLen:
            file.write(f'{item}')
        else:
            file.write(f'{item},')
    file.truncate()


def convertToJson(dataArr: []):
    # todo: add converter
    convertedArr: [] = []
    return convertedArr
    pass


def convertToCsv(dataArr: []):
    # todo: add converter
    convertedArr: [] = []
    return convertedArr
    pass


def askForSavingFormat():
    valid = False
    while not valid:
        choice: str = input(
            "Choose format. Insert number to select your choice.\n"
            "0. default\n"
            "1. json\n"
            "2. csv\n"
            "> ")
        if choice == "0":
            return "default"
        if choice == "1":
            return "json"
        if choice == "2":
            return "csv"


def saveAsJson(dataArray: []):
    # todo: implement converter
    pass


def saveAsCsv(dataArray: []):
    # todo: implement converter
    pass
