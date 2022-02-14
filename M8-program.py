#Ejercicio 1: Creación de diccionarios de Python
#Ejercicio: Crear y modificar un diccionario de Python


# Crea un diccionario llamado planet con los datos propuestos
planet = {
    
    'name': 'Mars',
    'moons': 10
    
}


# Muestra el nombre del planeta y el número de lunas que tiene.
print(f'{planet["name"]} posee: {planet["moons"]} moons')


# Agrega la clave circunferencia con los datos proporcionados previamente
planet['circumference (km)'] = { #'circunferencia (km)'
                                
    'polar': 6752,
    'equatorial': 6792
    
}


# Imprime el nombre del planeta con su circunferencia polar.
print(f'{planet["name"]} tiene una circunferencia polar de:  {planet["circumference (km)"]["polar"]}')


#*****************************************************************************************

#Ejercicio 2: Programación dinámica con diccionarios
#Ejercicio: Cálculo de valores

# Añade el código para determinar el número de lunas.
# Planets and moons
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}


# Almacenamos los datos en una variable llamada moons
moons = planet_moons.values()

# Agrega el código para contar el número de lunas. 
planets = len(planet_moons.keys())


# GUardamos los datos en una  variable llamada total_moons
total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

# Calculamos el promedio  (total_moons / planetas)
average = total_moons / planets

# Mostramos el promedio
print("El Promedio es: ",average)
