
def my_print(message):
    print(message)

my_print('Im calling the function')
my_print('Im calling the function again')

def suma(a,b):
    print(a + b)
    
suma(10,20)

#Funciones:Return

def sum_with_range(min,max):
    suma = 0
    for x in range(min,max):
        suma += x
    return suma

print(sum_with_range(10,30))

#Funciones: Parametros por defecto y múltiples returns

def find_volume(length=1,width=1,depth=1): #Asignación parámetros por defecto
    volume = length * width * depth
    return volume, width, depth, 'result' #Retorna una tupla

print(find_volume(10)) #Puedo cambiar  el valor de cualquier parámetro 
print(find_volume(10,20,3))

