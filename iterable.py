for i in range(10):
    print(i)

my_iter = iter(range(1,4))
print(my_iter)
#Podemos controlar la manera en la que se ejecuta
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter)) Lanza un error de stopIteration

#Para obtener manualmente un iterador

