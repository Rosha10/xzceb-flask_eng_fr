import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ[ 'apikey' ]
apiurl = os.environ[ 'apiurl' ]

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator = authenticator)
language_translator.set_service_url(apiurl)

def english_to_french(english_text):

    ''' This function translates English Text to French'''
    result = language_translator.translate(text = english_text, model_id='en-fr').get_result()

    french_text = result ['translations'] [0] ['translation']

    if english_text == " ":
        print("Please enter a word")
    else:
        pass

    return french_text

def french_to_english(french_text):

    '''This function translates French text to English'''
    
    result = language_translator.translate(text = french_text, model_id='fr-en').get_result()
    english_text = result['translations'][0]['translation']

    if french_text == " ":
        print("Entrez un mot")
    else:
        pass

    return english_text
