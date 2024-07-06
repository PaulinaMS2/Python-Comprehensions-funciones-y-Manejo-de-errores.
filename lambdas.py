
def increment(x):
    return x + 1

#Transformar esta funcion en una lambda
increment_v2 = lambda x: x+1

print(increment(2))
print(increment_v2(3))

full_name = lambda name, last_name: f'{name.title()} {last_name.title()}'
print(full_name('David', 'muñoz'))

#Ejemplo de una función lambda con list_comprehension
increment_v3 = lambda lista: [x + 1 for x in lista]
print(increment_v3([1, 2, 3]))