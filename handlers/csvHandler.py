from handlers.abstractHandler import Handler


class csvHandler(Handler):

    def useFile(self, filePath: str, modus: str):
        super().useFile(filePath, modus)

    def modusHandler(self, modus: str, filePath: str):
        super().modusHandler(modus, filePath)

    def read(self, filePath: str):
        file = open(filePath, 'r')
        content = file.read()
        print(content)
        file.close()

    def readAndWrite(self, filePath: str, modus: str):
        pass

    def writeToFile(self, filePath: str, modus: str):
        pass

    def __init__(self):
        pass
