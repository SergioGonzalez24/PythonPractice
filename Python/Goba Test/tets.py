import time
from googletrans import Translator

mesActual=time.strftime("%B")
translator=Translator()

d1=translator.detect(mesActual)

mesTrad=tarnslator.translate(mesActual,src=d1.lang,dest="es")


print(mesTrad.lower())