"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""

import os


lista = []
opcao = ''

while True:
    try:
        print('Selecione uma opção')
        opcao = input('[i]nserir [a]pagar [l]istar: ')

        if opcao == 'i':
            os.system('cls')
            inserir = input('Valor: ')
            lista.append(inserir)
            continue

        if opcao == 'l':
            if lista == []:
                os.system('cls')
                print('Nada para listar')
                continue
            else:
                for indice, nome in enumerate(lista):
                    print(indice, nome)
                continue
        try:
            if opcao == 'a':
                apagar = input('Escolha o índice para apagar: ')
                apagar = int(apagar)
                indices = range(len(lista))
                for indice in indices:
                    if indice == apagar:
                        lista.remove(lista[indice])          
        except ValueError:
            print('Não foi possivel apagar esse indice!')
            
    except KeyboardInterrupt:
        break