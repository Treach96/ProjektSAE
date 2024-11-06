
def useFile(filePath, modus):
    print("You selected this modus: ", modus)
    file = open(filePath, modus)
    modusHandler(modus, file)

def modusHandler(modus, file):
    match modus:
        case "w":
            print("Write mode activated")
        case "r+":
            print("Read and Write mode activated")
        case "w+":
            print("Write and Read mode activated, file will be overridden")







