#Manera clasica
numbers = []
for element in range(1,11):
    numbers.append(element**2)

print(numbers)

#List comprehension
numbers_v2 = [element**2 for element in range(1,11)]
print(numbers_v2)

#List comprehension con condicion
#Manera clasica de crear una lista de pares
even_numbers = []
for element in range(1,11):
    if element % 2 == 0:
        even_numbers.append(element)
print(even_numbers)

#List comprehension
even_numbers_v2 = [ element for element in range(1,11) if element % 2 ==0]
print(even_numbers_v2)

