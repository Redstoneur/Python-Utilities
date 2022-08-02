from Utilities.Tools.OSTermCommande import CleanTerminal, CleanTerminalWithTime


def TerminalLoader(message: str, start: int = 0, stop: int = None, s: int | float = 2, divide: int = 100) -> int:
    """
    Load the terminal with the information of the computer
    :return:
    """
    CleanTerminal()
    if stop is None:
        stop = divide
    i = start
    for i in range(start, stop):
        print(message + " (" + str(i) + "%" + ")")
        f = ">"
        if i == divide - 1:
            f = ""
        print("[" + "-" * i + f + " " * (divide - 1 - i) + "]")
        print("")
        CleanTerminalWithTime(s=s, divide=divide)
    return i + 1
