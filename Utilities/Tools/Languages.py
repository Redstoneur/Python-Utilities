import locale

# import googletrans
# from googletrans import Translator


######################################################################################################################
############################## Functions Translator ##################################################################
######################################################################################################################

# listOfLanguages: list = list(googletrans.LANGUAGES.keys())

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
#     text_translated = Translator().translate(text, dest=language_of_translation)
#     print(text_translated.text)
#     translator = Translator()
#     if language_of_text == language_of_translation:
#         return text
#     elif (language_of_text not in listOfLanguages and language_of_text is not None) \
#             or language_of_translation not in listOfLanguages:
#         return None
#     else:
#         try:
#             print(translator.translate(['bonjour'], dest=language_of_translation).text)
#             return translator.translate(text, dest=language_of_translation).text
#         except Exception as e:
#             print(e)
#             return None
#
# if __name__ == "__main__":
#     #     txt_fr = "Bonjour"
#     #     txt_en = "Hello"
#     #
#     #     translator = Translator()
#     #
#     #     translate = translator.translate(txt_fr, src="fr", dest="en")
#     #     print(translate)
#     #
#     #     print("the text '"+txt_fr+"' is in the language '"+translator.detect(txt_fr)+"'")
#     #     print("the text '"+txt_en+"' is in the language '"+translator.detect(txt_en)+"'")
#     #
#     #     print("the text '"+txt_fr+"' is translated in the language '"+translator.detect(translator.translate(text=txt_fr, src="fr", dest="en").text)+"'")
#     #     print("the text '"+txt_en+"' is translated in the language '"+translator.detect(translator.translate(text=txt_en, src="en", dest="fr").text)+"'")
#     #
#     #     print(Translator.detect("Bonjour"))
#     print(translateSimple("Bonjour", "fr", "en"))
#     # print(translateSimple("Hello", "en", "fr"))
