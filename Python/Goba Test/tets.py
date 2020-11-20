import time
from googletrans import Translator

mesActual=time.strftime("%B")
translator=Translator()
translator.translate(mesActual,dest='es')



print ("el mes actual es ", time.strftime("%B"))