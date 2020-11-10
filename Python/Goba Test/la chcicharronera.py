#Un programa que resuelva ecuaciones de segundo grado 

#Importamos la libreria Math, seleccionamos las operaciones necesarias y les asignamos un nombre
import math

#El usuario ingresa sus datos 
a = float ( input ( "Ingrese el valor de la x^2: " ))
b = float ( input ( "Ingrese el valor de la x: " ))
c = float ( input ( "Ingrese el valor de la constante: " ) )

#Se realizan la operaciones con la raíz positiva 
dentroderaiz = ( b ** 2 - (4 * a * c ) ) 

if dentroderaiz < 0: 
    print ("Tu sistema no tiene solución :( ")

else:

    raizPositiva = ( - b + ( math.sqrt ( dentroderaiz ) ) )/ (2 * a )

    #Se realizan la operaciones con la raíz negativa 

