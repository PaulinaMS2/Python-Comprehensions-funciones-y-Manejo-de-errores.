#Map: su función es hacer transformaciones a una lista 
#Se obtienen los mismos elementos de la primera lista pero transformados

#Forma tradicional
numbers = [1, 2, 3 , 4]
numbers_v2 = []
for number in numbers:
    numbers_v2.append(number * 4)
print(numbers_v2)

#Usando map y lambda functions
numbers_v3 = list(map(lambda number: number *4, numbers))
print(numbers_v3)

#Modificando dos listas
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7]

result = map(lambda x,y: x+y, list1,list2) #Se obtiene la longitud más pequeña, list2
print(list(result))

#Map con diccionarios
items = [
    {
        'name': 'monitor',
        'price': 300,
    },
    {
        'name': 'teclado',
        'price': 100
    },
    {
        'name': 'mouse',
        'price': 50
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

#sin lambda function
def add_taxes(item):
    item['taxes'] = item['price'] * 0.19
    return item

new_items = list(map(add_taxes, items))
print(new_items)
print(items) #Se modifica el diccionario original