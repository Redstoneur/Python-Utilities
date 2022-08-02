from Utilities.Tools.Error import *
from Utilities.Tools.Languages import *


def closeProgramme(message: str = None, error: Error = None, code: int = None, language: str = "fr") -> None:
    """
    close the programme
    :param language: str, language of the message
    :param message: str, message to display
    :param error: Error, error to display
    :param code: int, code of the error
    :return: None
    """
    language = haveLanguage(language)

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
