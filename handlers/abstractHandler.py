from abc import ABC
from abc import abstractmethod


class Handler(ABC):

    @abstractmethod
    def useFile(self, filePath: str, modus: str):
        self.modusHandler(modus, filePath)

    @abstractmethod
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
    def read(self, filePath: str):
        pass

    @abstractmethod
    def readAndWrite(self, filePath: str, modus: str):
        pass

    @abstractmethod
    def writeToFile(self, filePath: str, modus: str):
        pass
