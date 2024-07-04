import random
#Manera tradicional
dict = {}
for i in range(1,11):
    dict[i] = i**2

print(dict)

#Dictionary comprehension
dict_v2 = {i : i**2 for i in range(1,11)}
print(dict_v2)

#Ej2: Generar un diccionario a partir de una lista
#Manera tradicional
countries = ['colombia', 'mexico', 'bolivia', 'peru']
population = {}
for i in countries:
    population[i] = random.randint(1,100)
print(population)

#Dictionary comprehension
population_v2 = {country : random.randint(1,100) for country in countries}
print(population_v2)

#Ej3 : Generar un diccionario a partir de dos listas
#Manera tradicional
dict1 = {}
countries = ['colombia', 'mexico', 'bolivia', 'peru']
population = [100,400,234,456]
for i,j in zip(countries,population):
    dict1[i] = j
print(dict1)

#Dictionary comprehension
dict2 = {i:j for i,j in zip(countries, population)}
print(dict2)
print(list(zip(countries, population)))

#Dictionary comprehension con condicion
countries = ['colombia', 'mexico', 'bolivia', 'peru']
population = {country: random.randint(1,100) for country in countries}
print(population)

dict_pmayora = {country: population for country, population in population.items() if population > 50}
print(dict_pmayora)

#Ej: Crear un diccionario a partir de un string
text = 'Hola, soy Paulina'
unique = {c: c.upper() for c in text if c in 'aeiou' }

print(unique)