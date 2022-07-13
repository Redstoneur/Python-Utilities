import os
import shutil as sh
from Utilities.FileAndFolder.ReadFile.File import *
from Utilities.FileAndFolder.ReadFile.SqlFile import *
from Utilities.FileAndFolder.ReadFile.DumpSqlFile import *
from Utilities.FileAndFolder.ReadFile.TxtFile import *
from Utilities.FileAndFolder.ReadFile.JsonFile import *


######################################################################################################################
############################## Special Functions #####################################################################
######################################################################################################################

def existFile(path: str) -> bool:
    """
    check if file exist
    :param path: path to file
    :return: bool, True if exist, False if not
    """
    return os.path.isfile(path)


def moveFile(file: str, folder: str) -> None:
    """
    move a file in a folder
    :param file: str, file to move
    :param folder: str, folder to move the file
    :return: None
    """
    if existFile(file):
        try:
            sh.move(file, folder)
        except Exception as e:
            print(e)
    else:
        print("File not found : " + file)


def copyFile(file: str, folder: str) -> None:
    """
    copy a file in a folder
    :param file: str, file to copy
    :param folder: str, folder to copy the file
    :return: None
    """
    if existFile(file):
        try:
            sh.copy(file, folder)
        except Exception as e:
            print(e)
    else:
        print("File not found : " + file)


def deleteFile(file: str) -> None:
    """
    delete a file
    :param file: str, file to delete
    :return: None
    """
    if existFile(file):
        try:
            os.remove(file)
        except Exception as e:
            print(e)
    else:
        print("File not found : " + file)


def generateFile(path: str, sp: str = None, debug: bool = False) -> None | file:
    """
    generate a read file
    :param path: path to file
    :param sp: specific name's type of file
    :param debug: bool, True if debug, False if not
    :return:
    """
    if existFile(path):
        if path.split('.')[-1] == "sql":
            if sp == 'Dump':
                return dumpSqlFile(path=path)
            else:
                return SqlFile(path=path)
        elif path.split('.')[-1] == "txt":
            return TxtFile(path=path)
        elif path.split('.')[-1] == "json":
            return JsonFile(path=path)
        elif debug:
            print("file type not found : " + path)
            return None
        else:
            print("File type not found")
            return None
    else:
        print("File not found : " + path)
        return None
