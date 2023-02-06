'''This module imports IBM Watson Language Translator and creates functions to translate
English to French and French to English'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey="08RZF0XU9nZDqjOl-FQKXFuyTgAtUopgr2PKr8gnAw6v"
url="https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/0aa6df98-cda4-435a-bc1e-6a5be2ce0007"


authenticator=IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    if english_text is None:
        return None
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text=french_text['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    if french_text is None:
        return None
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text=english_text['translations'][0]['translation']
    return english_text