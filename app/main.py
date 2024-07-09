import utils #Mi propio modulo

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

def run():
    result = utils.get_population()
    print(result)

    country = input("Ingrese el país para obtener su población => ").lower()

    result = utils.population_by_country(countries, country)
    print(result)

if __name__ == '__main__': #Si se ejecuta este archivo, se ejecuta la función run
    run()

#Manejar la dualidad de poder ser ejecutados como scripts desde la terminal o ejecutados como modulo en otro archivo
