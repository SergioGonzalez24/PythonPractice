###Calculadora de Triangulos
###Desarrollador: Sergio Gonzalez

while True:
    #Seleccion de triangulo
    print("Programa para calcular Triangulos")
    print("Seleccione su Triangulo.\n1-.Rectangulo\n2-.Isoseles\n3-.Escaleno\n4-.Equilatero")
    print("")
    tipo_de_triangulos=int(input())

    #Menu de Seleccion

    
    if tipo_de_triangulos == 1:

        print("Introduzca las medidas de los lados de su triangulo rectangulo")
        lado_1=(input(print("a= ")))
        print("________________")
        lado_2=(input(print("b= ")))
        print("________________")
        lado_3=(input("c= "))
        print("______________")


        if lado_3=="x":
            float(lado_1)
            float(lado_2)
            lado_3=lado_1+lado_2
            print("c= ",lado_3)
        elif lado_1=="x":
            print("")
        elif lado_2=="x":
            print("")
         

    

