#Tambien aplican algunas propiedades de los conjuntos
#Se pueden moficar, No tienen orden, No tienen elementos repetidos

set_countries = {'colombia', 'mexico', 'bolivia'} 
print(set_countries) #Si hay un elemto repetido, solo se imprime una vez
print(type(set_countries))

set_numbers = {1,2,3,4,5,2}
print(set_numbers)

set_from_string = set('hola mundo') #Nota: Guarda el espacio como un elemento
print(set_from_string)

set_from_tuple = set(('abc', 'def', 'ghi', 'abc'))
print(set_from_tuple)

numbers = [1,2,3,1,2,3,4] #Forma sencilla de eliminar elementos repetidos 
set_from_list = set(numbers)
print(set_from_list)
unique_numbers = list(set_from_list)
print(unique_numbers, type(unique_numbers))
