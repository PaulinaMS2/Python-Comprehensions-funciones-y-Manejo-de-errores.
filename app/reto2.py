import read_csv as rc
import charts as ch

data = rc.read_csv('./data.csv')
#Para hacer más corto el alcance de esta gráfica
data = list(filter(lambda item: item['Continent'] == 'North America', data))

def world_population_percentage():
    dict_population = {}
    for i in data:
        dict_population[i['Country/Territory']] = i['World Population Percentage'] 
    return dict_population

if __name__ == '__main__':
    result= world_population_percentage()
    country = result.keys()
    population = [float(value) for value in result.values()]
    ch.generate_pie_chart(country, population)
    