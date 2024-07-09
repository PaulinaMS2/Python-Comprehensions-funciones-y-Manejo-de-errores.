import functools as ft
#Reducir algo a un solo valor
numbers = [1,2,3,4,5,6]
sum_numbers = ft.reduce(lambda counter,item: counter + item, numbers)
print(sum_numbers)


