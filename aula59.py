"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal # O Decimal mostra mais casas decimais, e ele serve para ser mais preciso

numero_1 = decimal.Decimal('0.1') # Ele transforma a String no tipo correto
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}') # Isso retorna um tipo String
print(round(numero_3, 2)) # Isso retorna o tipo correto como float ou int