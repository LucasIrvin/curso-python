"""
Fatiamento de Strings

012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::] - I = Inicio, F = Fim, P = Passo é quantos caracteres ele vai pular
Sempre que eu querer o final tem que pegar 1 a mais do que ta pedindo pois o indice final não é incluido
Obs. : a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'
print(len(variavel))
print(variavel[::-1])