respuestas = {
   'computadora': 'Con mi computadora puedo programar usando Python',
   'celular': 'En mi celular puedo aprender usando la app de Platzi',
   'cable': 'En mi celular puedo aprender usando la app de Platzi'
}

def message_creator(text):
   if text in respuestas.keys():
    return respuestas[text]
   else:
     return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)