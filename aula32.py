"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um número inteiro: ')

# try:
#     numero_int = int(numero)
#     conta = numero_int % 2 == 0
#     if conta is True:
#         print('Este número é par')
#     else:
#         print('Este número é impar')
# except:
#     print('Você não digitou um número inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    hora = input('Que horas são? ')
    hora_int = int(hora)
except:
    print('Digite um número inteiro!')

if hora_int >= 0 and hora_int <= 11: 
    print('Bom dia')
elif hora_int >= 12 and hora_int <= 17:
    print('Boa tarde')
elif hora_int >= 18 and hora_int <= 23:
    print('Boa noite')
else:
    print('Esse horário não existe')



