#Alcance de las variables (Scope)
#Local scope: Una variable solo tendra alcance dentro del bloque de código que fue creado
price = 100 #Alcance global

def increment():
    price = 150 #Alcance local, es nuevo y diferente al global
    price = price + 200 #Alcance local, un contexto diferente
    print(price)
    return price

print(price)
price_2 = increment()
print(price_2)