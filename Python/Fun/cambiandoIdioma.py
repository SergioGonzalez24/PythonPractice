#CODIGO CREADO POR SERGIO GONZALEZ
#12/07/2020

import pyttsx3
from googletrans import Translator

#INPUT DE DATOS A TRADUCIR
texto1=input("Introduce tu texto aqui ")

#CODIGO ENCARGADO DE DETECTAR EN QUE IDIOMA ESTA NUESTRO INPUT

translator=Translator()

dt1 = translator.detect(texto1)
print(dt1.lang)

#CODIGO ENCARGADO DE TRADUCIR EL TEXTO AL IDIOMA EN ESPAÑOL

translated = translator.translate(texto1, src=dt1.lang, dest="es")
print(translated.text)

#CODIGO ENCARGADO DE HABLAR

engine = pyttsx3.init()

engine.setProperty('rate', 125) 

engine.say(translated.text)
engine.runAndWait()

