set_A = {'col', 'bol', 'mex'}
set_B = {'bol', 'per'}

#Union de conjuntos
set_c = set_A.union(set_B)
print(set_c)
print(set_A | set_B) #Con el operador | se realiza la union de los conjuntos

#Interseccion (elementos comunes)
set_d = set_A.intersection(set_B)
print(set_d)
print(set_A & set_B) #Con el operador & se realiza la interseccion de los conjuntos

#Diferencia (elimina elementos de B en A)
set_e = set_A.difference(set_B)
print(set_e)
print(set_A - set_B) #Con el operador - se realiza la diferencia de los conjuntos

#Difrerncia simetrica (Solo elementos que no se repiten)
set_f = set_A.symmetric_difference(set_B)
print(set_f)
print(set_A ^ set_B) #Con el operador ^ se realiza la diferencia simetrica de los conjuntos
