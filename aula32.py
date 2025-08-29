"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    conta = numero_int % 2 == 0
    if conta is True:
        print('Este número é par')
    else:
        print('Este número é impar')
except:
    print('Você não digitou um número inteiro!')


