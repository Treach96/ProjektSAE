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
    def read(self, filePath: str):
        pass

    @abstractmethod
    def readAndWrite(self, filePath: str, modus: str):
        pass

    @abstractmethod
    def writeToFile(self, filePath: str, modus: str):
        pass

    @abstractmethod
    def createDataArray(self, content: str):
        pass

    @abstractmethod
    def convertToDict(self, lineToAdjust):
        pass

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
        convertedNumber = int(input("Which line do you want to change?\nInsert number"
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
        # todo: loop after change "do you want to further adjust some keys?" no -> loop with read/ r+/ w+ -> no -> exit
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
