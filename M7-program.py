#Ejercicio 1: Creación de un bucle "while"
#Ejercicio 1: Uso de ciclos while en Python


# Declaramos 2 variables

new_planet = "" #Declaramos la variable vacia
planets = []    #Dejamos la cadena vacia


# Escribe el ciclo while solicitado

while new_planet.lower() != 'done': #si se escribe done el ciclo se rompera 
    if new_planet:                  #si no -> el ciclo continuara
        planets.append(new_planet)
    new_planet = input("Ingrese un nuevo Planeta: ")


#*****************************************************************************************
#Ejercicio 2: Creación de un ciclo "for"
#Ejercicio: - Ciclo para una lista

# Escribe tu ciclo for para iterar en una lista de planetas

for planet in planets:
    print(planet)   #Impresion de los datos ingresados 