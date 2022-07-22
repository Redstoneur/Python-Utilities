import os
import platform as plt


######################################################################################################################
############################## Functions for the terminal ############################################################
######################################################################################################################

def get_os() -> str:
    """
    get the os name
    :return:
    """
    return plt.system()


def CleanTerminal() -> None:
    """
    clean the terminal
    :return: None
    """
    # if the os is windows
    if get_os() == "Windows":
        os.system("cls")
    else:  # if the os is linux
        os.system("clear")
