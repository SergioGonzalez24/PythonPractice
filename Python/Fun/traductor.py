from googletrans import Translator
texto1=input("Escribe tu texto aqui")

translator=Translator()

dt1 = translator.detect(texto1)
print(dt1.lang)

translated = translator.translate(texto1, src=dt1.lang, dest="fr")
print(translated.text)