import sys #Sistema operativo

print(sys.path)

import re #Expresiones regulares
text = 'My phone number is 344-55-66, el código es 47 y mi número de la suerte es el 10'
result = re.findall('[0-9]+', text)
print(result)

import time #Manejo de tiempo y fechas
timestap = time.time()
local = time.localtime()
result = time.asctime(local)
print(result)

import collections #Manejar listas
numbers = [1, 1, 2,3,4,4,5,6,6,21]
counter = collections.Counter(numbers)
print(counter)
strings = ['hola', 'hola', 'mundo', 'mundo', 'mundo']
counterS = collections.Counter(strings)
print(counterS)