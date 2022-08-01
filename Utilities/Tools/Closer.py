from Utilities.Tools.Error import *

listOfLanguages = ["fr", "en"]


def closeProgramme(message: str = None, error: Error = None, code: int = None, language: str = "fr") -> None:
    """
    close the programme
    :param language: str, language of the message
    :param message: str, message to display
    :param error: Error, error to display
    :param code: int, code of the error
    :return: None
    """
    if language == "?" or language not in listOfLanguages:
        print("The language must be in the list: " + str(listOfLanguages))
        while language not in listOfLanguages:
            language = input("Please enter the language: ")

    if message is not None:
        print(message)
    if error is not None:
        print(error)

    if language == "fr":
        input("appuyez sur une touche pour continuer...")
    elif language == "en":
        input("Press Enter to continue...")

    if code is not None:
        exit(code)
    elif error is not None:
        exit(error.code)
    else:
        exit()
