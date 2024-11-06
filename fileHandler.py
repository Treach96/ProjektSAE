
READ_MODUS = "r"
WRITE_MODUS = "w"
READ_AND_WRITE_MODUS = "r+"
WRITE_AND_READ_MODUS = "w+"
def initial():
    print("Hello")

def openFile(filepath):
    file = open(filepath)
    modus = askForModus()
    parserSwitch(file, modus)

def askForModus():
    userIn = input("What do you want to do?\n"
                  "Use numbers to select your choice:\n"
                  "1. read -- only shows content of file\n"
                  "2. write -- current content will be overridden\n"
                  "3. read and write -- shows file and writes to it\n"
                  "4. write and read -- shows file and truncates it, removing its existing content\n"
                   "> ")
    return modeSwitch(userIn)

def modeSwitch(userIn):
    match userIn:
        case 1:
            return READ_MODUS
        case 2:
            return WRITE_MODUS
        case 3:
            return READ_AND_WRITE_MODUS
        case 4:
            return WRITE_AND_READ_MODUS

def checkForFileType(file):
    filesplit = file.split(".")
    return filesplit[1]

def parserSwitch(file, modus):
    filetype = checkForFileType(file)
    match filetype:
        case "json":
            jsonParser.useFile(file, modus)
