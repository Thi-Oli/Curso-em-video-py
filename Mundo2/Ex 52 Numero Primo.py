'''Faça um programa que leia um numero inteiro e mostre se ele é um número primo.'''

#1 Coletando uma variável
n = int(input('Digite um numero inteiro: '))

for c in range(1, n+1):
    if n % c == 0:
        print('\033[31m', end =' ')
    else:
        print('\033[32m', end = ' ')
    print('{}'.format(c), end = '')

