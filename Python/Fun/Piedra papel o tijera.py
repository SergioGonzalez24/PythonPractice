import random


pregunta=input("si o no ")
preg_m=pregunta.lower()

if preg_m =="si":
    choice=True
elif preg_m == "no":
    choice=False
else :
    print("No valido")
    choicse=False

def lap_choice(lap):

    lap.randint(1,3)
    if lap ==1:
        #piedra
        lap=1
    elif lap ==2:
        #papel
        lap=2
    elif lap ==3:
        #tijera
        lap=3
def PPT ():

    a=input("has tu eleccion piedra, papel o tijera")
    usrAns=a.lower()

    if usrAns=="piedra" or "papel" or "tijera":
        if usrAns=="piedra":
            piedra=1
            #Hacer la comparacion ntre la eleccion del usuario y la computadora
        elif usrAns=="papel":
            papel=2
            #Hacer la comparacion ntre la eleccion del usuario y la computadora
        elif usrAns=="tijera":
            tijera=3
            #Hacer la comparacion ntre la eleccion del usuario y la computadora

while choice==True:

    back=True
    PPT()

    
    while back==True:

        back=input("¿Otra vez?")
        back_m=back.lower()

        if back_m=="si":
            continue
        elif back_m=="no":
            choice= False
            break
        else:
            back=True
