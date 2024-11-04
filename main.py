from tkinter import Tk
from tkinter.filedialog import askopenfilename


def getFileFrom():
    Tk().withdraw()
    filename = askopenfilename()
    return filename

file = getFileFrom()
openFile = open(file)
