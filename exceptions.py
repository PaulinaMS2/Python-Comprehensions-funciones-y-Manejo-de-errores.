#Debemos manejar y controlar los errores para que no se nos caiga el programa si alguno de esos sucede

try:
    print(0/0)
    assert 1 != 1, 'Uno no es igual a uno'
    age = 10
    if age < 18:
        raise Exception('No se permite menores de edad')

except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error) 


#Capturar la excepción propia
try:
    age = 10
    if age < 18:
        raise Exception('No se permite menores de edad')
except Exception as error:
    print(error)
print('Continuó')