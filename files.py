# file = open('./text.txt')
# # #print(file.read()) #Leerlo completo

# # print(file.readline()) #Leer linea por linea de forma manual
# # print(file.readline())

# for line in file:
#     print(line)

# file.close() #Cerrar el archivo

#Cerrar automáticamente el archivo
with open('./text.txt', 'w+') as file: #Con el r+ puedes agregar nuevas lineas y el w+ sobreescribe el archivo
    for line in file:
        print(line)
    #COMO ESCRIBIR EN EL ARCHIVO (WRITE)
    file.write('\n Nuevas cosas en el archivo') #\n es un salto de linea
    file.write('\n Nuevas cosas en el archivo otra vez')



