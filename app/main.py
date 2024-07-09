import utils #Mi propio modulo

result = utils.get_population()
print(result)

countries = [
    {
        'country': 'colombia',
        'population': 50000
    },
    {
        'country': 'bolivia',
        'population': 11000
    },
    {
        'country': 'argentina',
        'population': 44000
    }
]
country = input("Ingrese el país para obtener su población => ").lower()

result = utils.population_by_country(countries, country)
print(result)