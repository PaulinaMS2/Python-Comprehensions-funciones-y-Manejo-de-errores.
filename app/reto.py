import read_csv as rc
import charts as ch
import re

data = rc.read_csv('./data.csv')

def choose_country():
    country = input('Ingrese el nombre del país que quiere conocer: ')
    for i in data: 
        if i['Country/Territory'] == country:
            return i
    print('País no encontrado')
    exit()
        
def historical_data():
    country = choose_country()
    valores = {re.sub(r' Population$', '', year): population for year, population in country.items() if re.search(r'^\d+$', re.sub(r' Population$', '', year)) }
    return valores.keys(), valores.values()


        
if __name__ == '__main__':
   labels, values = historical_data()
   values = [int(value) for value in values]
   ch.generate_bar_char(labels, values)
   
