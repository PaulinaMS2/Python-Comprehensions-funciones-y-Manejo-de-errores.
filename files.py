file = open('./text.txt')
# #print(file.read()) #Leerlo completo

# print(file.readline()) #Leer linea por linea de forma manual
# print(file.readline())

for line in file:
    print(line)

file.close() #Cerrar el archivo

#Cerrar automáticamente el archivo
with open('./text.txt') as file:
    for line in file:
        print(line)