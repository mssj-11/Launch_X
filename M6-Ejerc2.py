# Lista de planetas
planets = ['Mercuro', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']


# Solicitamos el nombre de un planeta *Pista:  input()*
user_planet = input('Ingresa el nombre de un planeta empezando con letra (Mayuscula)')


# Busca el planeta en la lista
planet_index = planets.index(user_planet)


# Muestra los planetas más cercanos al sol
print('Los planetas mas cercas ' + user_planet)
print(planets[0:planet_index])



# Muestra los planetas más lejanos al sol
print('Here are the planets further than ' + user_planet)
print(planets[planet_index + 1:])

