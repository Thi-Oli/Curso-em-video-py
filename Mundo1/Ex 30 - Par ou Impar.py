'''Crie um programa que leia um número inteiro e informe se ele é PAR ou IMPAR'''

# Lendo um valor
n = int(input('Digite um numero --> '))
if n % 2 == 0: # % (MÓDULO) significa o resto da divissão.
    print('PAR')
else:
    print('IMPAR')