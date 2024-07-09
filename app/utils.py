#Este será el modulo de las funciones

def get_population():
    keys = ['colombia', 'bolivia', 'argentina']
    values = [50000, 11000, 44000]
    return keys, values

def population_by_country(data,country):
    result = list(filter(lambda x: x['country']== country, data))
    return result

