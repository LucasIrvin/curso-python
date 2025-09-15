"""
split e join com list e str
split - divide uma string
join - une uma string
strip - Corta os espaços no começo e no fim da String
rstrip - Corta os espaços da direita
lstrip - Corta os espaços da esquerda
"""

frase = '     Olha só que,      coisa interessante'
lista_frases_cruas = frase.split(',')

lista_frases = []

for indice, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[indice].strip())

# print(lista_frases)
# print(lista_frases_cruas)

frase_unidas = '*'.join(lista_frases)
print(frase_unidas)