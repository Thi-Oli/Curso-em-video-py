'''Crie um programa que leia 7 anos de péssoas.
E mostre quantas já são maior de idade e quantas não são.'''

from datetime import date
anoatual = date.today().year
print(anoatual)
cont = 0
print('Coloque o ano de nascimento de 7 pessoas')
#1Coletando o ano de 7 pessoas
for i in range(1, 8):
    nascimento = int(input('Qual o ano de seu nascimento: '))
    #nascimento += 1 # Contagem de quantas vezes o programa passou por aqui.

# 2 - Verificando se é de maior ou não
    if 21 > anoatual - nascimento:
        cont += 1
        restante = 7 - cont
print('Tem {} maior de idade e {} menor de idade'.format(cont, restante))
