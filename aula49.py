"""
Listas em Python
Tipo list - Mutável 
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, Ler, Alterar, apagar = list[i] (CRUD)
"""
# Se eu apagar um item da lista todos os itens a frente vão ser diferentes
#        0   1   2   3
# A lista só é interessante quando se trabalha no fim dela! A não ser que ela seja pequena
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(50)
# O Pop remove o ultimo objeto da lista.
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido, ', ultimo_valor)