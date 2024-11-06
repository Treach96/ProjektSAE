from tkinter import Tk
from tkinter.filedialog import askopenfilename
import fileHandler as fiHan


# retrieve filePath and parse it to the fileHandler
def getFileFrom():
    Tk().withdraw()
    filePath = askopenfilename()
    return filePath


def parseFileToProcess(filePath):
    fiHan.openFile(filePath)


filePath = getFileFrom()
parseFileToProcess(filePath)
