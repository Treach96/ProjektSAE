import jsonHandler
# The fileHandler will define the modus the user wants to use and
# check for the filetype to parse it to an appropriate handler
READ_MODUS = "r"
WRITE_MODUS = "w"
READ_AND_WRITE_MODUS = "r+"
WRITE_AND_READ_MODUS = "w+"

def openFile(filePath):
    modus = askForModus()
    if modus == READ_MODUS:
        file = open(filePath, modus)
        for line in file:
            print(line)
        file.close()
    else:
       handlerSwitch(filePath, modus)

def askForModus():
    userIn = input("What do you want to do with the file?\n"
                  "Use the number to select your choice:\n"
                  "1. read -- only shows content of file\n"
                  "2. write -- current content will be overridden\n"
                  "3. read and write -- shows file and writes to it\n"
                  "4. write and read -- shows file and truncates it, removing its existing content\n"
                   "> ")
    return modeSwitch(userIn)

def modeSwitch(userIn):
    match userIn:
        case "1":
            print("You selected read mode. File will be printed into console.")
            return READ_MODUS
        case "2":
            return WRITE_MODUS
        case "3":
            return READ_AND_WRITE_MODUS
        case "4":
            return WRITE_AND_READ_MODUS

def checkForFileType(filepath):
    filesplit = filepath.split(".")
    return filesplit[1]

def handlerSwitch(filePath, modus):
    filetype = checkForFileType(filePath)
    match filetype:
        case "json":
            jsonHandler.useFile(filePath, modus)
