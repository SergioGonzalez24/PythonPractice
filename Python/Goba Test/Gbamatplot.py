#Un programa que grafique 
import matplotlib.pyplot as plt

#Se define la primera función 
def canastaBasica ():
    nombre = ["leche" , "pollo" , "huevo" , "frijol" , "cereal" , "azúcar" ]
    precio = [ 23.20, 86, 45.50, 35.90, 39, 56.50] 
    colores = ["white" , "yellow" , "blue" , "green" , "pink" , "red"]
    plt.title (" Precio de productos de la canasta básica en pesos mexicanos. A noviembre del 2020 ")
    plt.ylabel ( "Precio ")
    plt.xlabel ( " Productos ")
    grafico1 = plt.barh (nombre, precio, label = 'Productos canasta básica', color = colores)
    plt.legend( grafico1, nombre)
    plt.show()

#Se define la segunda función 
def productosElectrónicos ():
    nombre = ["Eco dot" , "Roku" , "Xiaomi mi smart band" , "ADATA 64 gb" , "Tv Samsung crystal" , "Logitech teclado" ]
    cantidad = [ 46260, 508, 10556, 4470, 2700, 2051 ] 
    plt.ylabel ( "Productos vendidos ")
    plt.xlabel ( " Nombre ")
    plt.pie ( cantidad, labels = nombre, autopct = '%.1f')
    plt.title ("Número de productos vendidos. De la lista de más vendidos de AMAZON ") 
    plt.show()
    

#Se llaman las funciones 
canastaBasica ()
productosElectrónicos ()