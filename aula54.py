"""
Exercício
Exiba os índices da lista

0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Lucas', 'Helena', 'Luiz', 'Fernanda']
lista.append('Irvin')
indices = 0

for nome in lista:
    print(indices, nome)
    indices += 1

