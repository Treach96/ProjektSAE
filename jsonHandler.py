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
        case "w+":
            print("Write and Read mode activated, file will be overridden")


def writeToFile(filePath, modus):
    file = open(filePath, modus)
    content = input("Please type in the content to be added:\n"
                     "> ")
    print(content)
    file.write(content)
    file.close()