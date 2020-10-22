import pyttsx3


T=open("ElOso.txt","r")
leer=T.read()
print(leer)
T.close()

engine = pyttsx3.init()
engine.say(leer) #leer la lectura en voz alta
engine.runAndWait()