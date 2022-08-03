import locale

######################################################################################################################
############################## Functions Translator ##################################################################
######################################################################################################################

listOfLanguages: list = ['fr', 'en']


def haveComputerLanguage() -> str:
    """
    give the language of the computer
    :return: str, language of the computer
    """
    return locale.getdefaultlocale()[0].split('_')[0]


def haveLanguage(language: str = "?") -> str:
    """
    check if the language is in the list of languages
    :param language: str, language to check
    :return: str, language of the computer
    """
    while language not in listOfLanguages:
        if language == "?":  # if the language is not given, we ask the user
            print("The language must be in the list: " + str(listOfLanguages))

        if language == "computer":  # if the language is computer, we use the computer language
            language = haveComputerLanguage()
        else:  # if the language is not in the list, we ask the user
            language = input(
                "Please enter the language ('computer' for the computer language and '?' for the list of languages): ")

    return language

# ## fonction de tratuction de la langue
# def translateSimple(text: str, language_of_text: str, language_of_translation: str) -> str | None:
#     """
#     translate the text in the language of the translation
#     :param text: str, text to translate
#     :param language_of_text: str, language of the text
#     :param language_of_translation: str, language of the translation
#     :return: str, translated text
#     """
#
# if __name__ == "__main__":
