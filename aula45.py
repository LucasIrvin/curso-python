"""
Iterável -> str, range, etc  -> É um elemento que pode te entregar uma coisa por vez, é um elemento que tem um metodo dentro dele chamado de (__iter__).
Metodo -> Um metodo é o negocio que chamamos depois do '.'
Iterador -> Quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
#for letra in texto

texto = 'Luiz' # iterável
# iterador = iter(texto) # iterador

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break

for letra in texto:
    print(letra)