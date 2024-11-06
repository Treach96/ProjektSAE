import json


def useFile(filePath, modus):
    print("You selected this modus: ", modus)
    modusHandler(modus, filePath)


def modusHandler(modus, filePath):
    match modus:
        case "w":
            print("Write mode activated")
            writeToFile(filePath, modus)
        case "r+":
            print("Read and Write mode activated")
            readAndWrite(filePath, modus)
        case "w":
            print("Write and Read mode activated, file will be overridden")


def writeToFile(filePath, modus):
    file = open(filePath, modus)
    content = input("Please type in the new content to be added:\n"
                    "> ")
    print(content)
    file.write(content)
    file.close()


def readAndWrite(filePath, modus):
    file = open(filePath, modus)
    print(file.read())
    choice = askUserForChoice()
    if choice == "change":
        print("change")
        key = askForKey()
    if choice == "append":
        print("append")
    file.close()


def askForKey():



def askUserForChoice():
    userInput = input("What do you want to do here? Select number to choose:\n"
                      "1. change value of key\n"
                      "2. append new entry\n"
                      "> ")
    match userInput:
        case "1":
            return "change"
        case "2":
            return "append"
