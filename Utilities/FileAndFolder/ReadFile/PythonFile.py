from Utilities.FileAndFolder.ReadFile.File import *


#####################################################################################################################
############################# Class Python File #####################################################################
#####################################################################################################################

class PythonFile(file):
    data: str
    path: str

    def __init__(self, path: str) -> None:
        """
        :param path: str path to file
        :param path:
        """
        super().__init__(path)
        self.path: str = path
        self.read()

    def read(self) -> None:
        """
        read file
        :return:
        """
        try:
            with open(self.path, 'r') as f:
                self.data = f.read()
                f.close()
        except Exception as e:
            print(e)
            exit()

    def write(self, data: str) -> None:
        """
        write data to file
        :param data:
        :return:
        """
        try:
            with open(self.path, 'w') as f:
                f.write(data)
                f.close()
        except Exception as e:
            print(e)
            exit()

    def getData(self) -> str:
        """
        get data
        :return:
        """
        return self.data

    def get(self, key: str) -> object:
        """
        get data of key
        :param key:
        :return:
        """
        return self.data
