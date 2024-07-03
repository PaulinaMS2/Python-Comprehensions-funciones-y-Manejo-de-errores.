#CRUD set
set_countries = {'colombia', 'mexico', 'bolivia'} 

size = len(set_countries)
print(size)

print('colombia' in set_countries)
print('peru' in set_countries)

#Añadir elemento al conjunto
set_countries.add('peru')
print(set_countries) #Aunque se agregue varias veces el mismo elemento solo se imprime una vez

#Actualizar un conjunto (agregar un conjunto a otro)
set_countries.update({'argentina', 'chile', 'peru'})
print(set_countries)

#Eliminar un elemento
set_countries.remove('bolivia')
set_countries.discard('bol') #Si el elemento no existe no arroja error
print(set_countries)

set_countries.clear() #Vacía el conjunto
print(set_countries)

