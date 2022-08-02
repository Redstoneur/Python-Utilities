import os
from time import sleep
import platform as plt
from Utilities.Tools.Error import Error


######################################################################################################################
############################## Functions for the terminal ############################################################
######################################################################################################################

def get_os() -> str:
    """
    get the os name
    :return:
    """
    return plt.system()


def get_CPU() -> str:
    """
    get the name of the CPU
    :return: str, name of the CPU
    """
    if get_os() == "Windows":
        return execute_command_with_return("wmic cpu get name").message
    else:
        return execute_command_with_return("lscpu").message


def get_RAM() -> str:
    """
    get the RAM of the computer
    :return: str, RAM of the computer
    """
    if get_os() == "Windows":
        return execute_command_with_return("wmic memorychip get capacity").message
    else:
        return execute_command_with_return("free -m").message
        # return execute_command_with_return("free -h").message


def get_Disk_space() -> str:
    """
    get the disk space
    :return: str, disk space
    """
    if get_os() == "Windows":
        return execute_command_with_return("wmic logicaldisk get name, freeSpace").message
    else:
        return execute_command_with_return("df -h").message


def get_Network() -> str:
    """
    get the network of the computer
    :return: str, network of the computer
    """
    if get_os() == "Windows":
        return execute_command_with_return("ipconfig").message
    else:
        return execute_command_with_return("ifconfig").message


def get_IP() -> str:
    """
    get the IP of the computer
    :return: str, IP of the computer
    """
    config: str = get_Network()

    return config.split("\n")[1].split(" ")[1]


def get_information_of_computer() -> dict:
    """
    get the information of the computer
    :return: dict, information of the computer
    """
    return {
        "OS": get_os(),
        "CPU": get_CPU(),
        "RAM": get_RAM(),
        "Disk": get_Disk_space(),
        "IP": get_IP(),
        "Network": get_Network()
    }


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


def CleanTerminalWithTime(s: int = 1, divide: int = 100) -> None:
    """
    clean the terminal with a loading bar
    :param s: int, sleep time
    :param divide: int, percentage of the loading bar
    :return: None
    """
    sleep(s / divide)
    CleanTerminal()


def execute_command(command: str, printError: bool = False) -> Error:
    """
    execute a command
    :param command: str, command to execute
    :param printError: bool, print the error or not
    :return: None
    """
    try:
        os.system(command)
    except Exception as e:
        if printError:
            print(e)
        return Error(success=False, message=str(e), code=500)
    else:
        return Error(success=True, message="success", code=200)


def execute_command_with_return(command: str, printError: bool = False) -> Error:
    """
    execute a command and return the output
    :param command: str, command to execute
    :param printError: bool, print the error or not
    :return: str, output of the command
    """
    try:
        result: str = os.popen(command).read()
    except Exception as e:
        if printError:
            print(e)
        return Error(success=False, message=str(e), code=500)
    else:
        return Error(success=True, message=result, code=200)


def execute_command_with_return_and_error(command: str, printError: bool = False) -> {Error, Error}:
    """
    execute a command and return the output and the error
    :param command: str, command to execute
    :param printError: bool, print the error or not
    :return: str, output of the command, str, error of the command
    """
    try:
        result: str = os.popen(command).read()
        error: str = os.popen(command).read()
    except Exception as e:
        if printError:
            print(e)
        return {
            "result": Error(success=False, message=str(e), code=500),
            "error": Error(success=False, message=str(e), code=500)
        }
    else:
        return {
            "result": Error(success=True, message=result, code=200),
            "error": Error(success=True, message=error, code=200)
        }
