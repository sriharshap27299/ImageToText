from googletrans import Translator
from pytesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#This is the custom path for Tesseract - OCR

from PIL import Image

flag = 1

while flag:
        translator = Translator()
        im = Image.open('german.jpg');
        # german.jpg is an example image you can replace it with any image name present in the
        # current working directory
        str = image_to_string(im)
        print("Identifying Text...")
        print("Identified Text: \n"+str)
        print("Translating Text to English...")
        translation = translator.translate(str, dest='en')
        # Here 'en' means translating text to English change it to any language you want
        print("Translated Text: \n"+translation.text)
        flag = 0



