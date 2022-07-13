from Utilities.FileAndFolder.ReadFile import *
from Utilities.FileAndFolder.ReadFoldersContained import *


######################################################################################################################
############################## Special Functions #####################################################################
######################################################################################################################


def existFolder(folder: str) -> bool:
    """
    check if folder exist
    :param folder: str, folder to check
    :return: bool, True if exist, False if not
    """
    return os.path.isdir(folder)

def moveFolder(folder: str, folderDestination: str) -> None:
    """
    move a folder in a folder
    :param folder: str, folder to move
    :param folderDestination: str, folder to move the folder
    :return: None
    """
    if existFolder(folder):
        try:
            sh.move(folder, folderDestination)
        except Exception as e:
            print(e)
    else:
        print("Folder not found : " + folder)

def copyFolder(folder: str, folderDestination: str) -> None:
    """
    copy a folder in a folder
    :param folder: str, folder to copy
    :param folderDestination: str, folder to copy the folder
    :return: None
    """
    if existFolder(folder):
        try:
            sh.copy(folder, folderDestination)
        except Exception as e:
            print(e)
    else:
        print("Folder not found : " + folder)

def deleteFolder(folder: str) -> None:
    """
    delete a folder
    :param folder: str, folder to delete
    :return: None
    """
    if existFolder(folder):
        try:
            sh.rmtree(folder)
        except Exception as e:
            print(e)
    else:
        print("Folder not found : " + folder)

