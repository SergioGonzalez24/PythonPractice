import random, sys

print("Piedra Papel o Tijera")

#Funciones a usar
def turnoJugador(eleccion):
    if eleccion == "r":
        print("Piedra contra...")
        return 1
    elif  eleccion == "p":
        print("Papel contra...")
        return 2
    elif eleccion == "t":
        print("Papel contra...")
        return 3

def turnoComp (randomNum):
    if randomNum == 1:
        print(" Piedra")
        return 1
    elif  randomNum == 2:
        print(" Papel")
        return 2
    elif randomNum == 3:
        print(" Tijera")
        return 2

#Variables que guardan datos de juego (Partidas ganadas, perdidas o empatadas)
ganados = 0
perdidos = 0
empatados = 0

while True: #While Principal
    print("%s Ganados, %s Perdidos, %s Empatados" %(ganados,perdidos,empatados))

    while True: #while eleccion jugador
        eleccionJ = input("Elije Piedra (R), Papel (P), Tijera (T), salir (S) ")
        eleccionJ.lower()

        if eleccionJ == "s":
            print("Gracias por jugar, vuelva pronto")
            sys.exit() #Salir del Programa

        elif eleccionJ == "r" or eleccionJ == "p" or eleccionJ == "t":
            randomNum=random.randint(1,3)
            resComp=turnoComp(randomNum)

            if turnoJugador(eleccionJ) == turnoComp(randomNum) :
                print("Es un empate")
                empatados+=1
                break
            elif turnoJugador(eleccionJ) > turnoComp(randomNum):
                print("Ganaste!")
                ganados+=1
                break
            elif turnoJugador(eleccionJ) < turnoComp(randomNum):
                print("Perdiste !")
                perdidos+=1
                break
