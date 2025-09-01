"""
Iterando strings com while
"""

#       012345678910
nome = ' Lucas Irvin' # Iteráveis
tamanho = 0

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

print(nome[4])

l1 = -1
l2 = 0

while l1 < tamanho_nome:
    l1 += 1
    l2 += 1 
    print(f'{nome[l1:l2:]}', end="*")