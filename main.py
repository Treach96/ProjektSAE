from tkinter import Tk
from tkinter.filedialog import askopenfilename
import fileHandler

# retrieve filePath and check filetype
def getFileFrom():
    Tk().withdraw()
    filePath = askopenfilename()
    return filePath

def parseFileToProcess(file):
        fileHandler.openFile(file)

file = getFileFrom()
parseFileToProcess(file)