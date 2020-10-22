
### Codigo obtenido de StackOverflow 
### Uso para estudio
### Modificado por Sergio Gonzalez

isMail = False #la variable isMail esta en false de inicio
email =input("escribe tu correo ") #puedes cambiarla por cualquier texto a validar
for i in email: #Recorre toda la cadena buscando @
    if(i =='@' and '.com'):
         isMail = True #si encuentra .com y @ entones la variable isMail cambia a true
         
if(isMail): print('Es un correo') #Si la variable es verdadera imprime Es un correo
else: print('No es correo') #caso contrario imprime no es correo