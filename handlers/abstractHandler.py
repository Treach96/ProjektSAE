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
    def saveToFile(self, file, dataArr: [], originalFile: str):
        print("start saving file")
        file.seek(0)
        saveFormat: str = askForSavingFormat()
        dictForm: dict = self.transformArrToDict(dataArr, originalFile)
        if saveFormat == "json":
            convertedArr: [] = convertToJson(dictForm)
        # savingArr(file, convertedArr)
        if saveFormat == "csv":
            convertedArr: [] = convertToCsv(dictForm)
            # savingArr(file, convertedArr)
        # todo: ask for futher changes? no-> exit
        choice: str = input("Do you want to do something else with this file?\n"
                            "chose \"yes\" or \"no\"\n"
                            "> ")
        if choice == "no":
            exit()

    @abstractmethod
    def transformArrToDict(self, dataArr: [], originalFile: str):
        print('start transforming array to dict')
        # {"key":"value","key":"value"}
        # jsonArr: {"id":6,"first_name":"Farand","last_name":"Dunican","gender":"Female","street_name":"Melrose"}
        # csvArr: 10,Beverly,Grelka,Female,Bunker Hill
        newDict: dict = {}
        print("Original filetype detected: ", originalFile)
        match originalFile:
             case "json":
                 pass
             case "csv":
                 pass


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
    def convertLineToDict(self, lineToAdjust):
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
        listOfKeys = list(jsonDict.keys())
        print("\nAvailable keys are: [", ', ' .join(listOfKeys), "]\n")
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
        print("Content of Array will be printed.")
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

    @abstractmethod
    def convertJStringToDict(self, jString: str):
        newDict: {} = {}
        tempStr: str = jString.strip('{}')
        tempArr: [str] = tempStr.split(',')

        for item in tempArr:
            key, value = item.split(':')
            key: str = key.strip('"')
            value: str = value.strip('"')
            newDict[key]: dict = value
        print("created successfully dict")
        return newDict

    @abstractmethod
    def transformJsonArrToDict(self, dataArr: []):
        newDict: {} = {}
        for dataItem in dataArr:
            itemStr: str = dataItem
            newDict = self.convertJStringToDict(itemStr)
        print("created successfully dict")
        return newDict

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
    print("csv:", dataArr)
    return convertedArr
    pass


def askForSavingFormat():
    valid = False
    while not valid:
        choice: str = input(
            "Choose format. Insert number to select your choice.\n"
            "1. json\n"
            "2. csv\n"
            "> ")
        if choice == "1" or choice == "json":
            return "json"
        if choice == "2" or choice == "csv":
            return "csv"


def saveAsJson(dataArray: []):
    # todo: implement converter
    pass


def saveAsCsv(dataArray: []):
    # todo: implement converter
    pass


