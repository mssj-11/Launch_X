#------------------------------------------------------------------------------------
#Problema 1
# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.
print("Ejercicio #1")
#Creacion de la variable con el valor inicial
Vel_asteroide = 49     #Asteroide que  viaja a una velocidad de 49 km/s / cambiar valor menor a 25 en caso de querer mostrar el segundo mensaje

if Vel_asteroide > 25: #Si es superior a 25 kilómetros 
    print('*Advertencia* - Un asteroide se acerca a gran velocidad!!!')#si necesita una advertencia - se mostarra el mensaje

else:#Si la expresión de prueba es true o false - se mostrara el sig. mensaje
    print('*Estas a salvo por Ahora* - Sigue con tu dia :)')

print("")
#------------------------------------------------------------------------------------
#Problema 2
# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False
print("Ejercicio #2")
#Creacion de la variable con el valor inicial
Vel_asteroide = 19      #Velocidad inicial a 19 km/s

if Vel_asteroide > 20:  #Si es superior a 19 kilómetros 
    print('Se puede observar una gran luz en el cielo') #Primera condicion - se mostrara el mensaje 
    
    #si es diferente o igual a 20
elif Vel_asteroide == 20:   
    print('A veces produce un rayo de luz que se puede ver desde la Tierra')
    
else:
    print('No , No veo Nada :)')

print("")
#------------------------------------------------------------------------------------
#Problema 3
print("Ejercicio #3")
# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

Nueva_Vel_asteroide = 25    #Valor de la velocidad (25 km) del nuevo asteroide
Tam_asteroide = 55          #Tamaño del asteroide

if Nueva_Vel_asteroide > 25 and Tam_asteroide > 25: #Si es mas grande que 25 km pero mas 1000 
    print('Un asteroide viene en direccion hacia la Tierra')
    
elif Nueva_Vel_asteroide >= 20: #Si la velocidad mayor o igual a 20 km/s
    print('A veces produce un rayo de luz que se puede ver desde la Tierra')
    
elif Tam_asteroide < 25:
    print('No hay ningun problema :)')
    
else:
    print('Yo no veo nada :)')


#------------------------------------------------------------------------------------
