'''Faça um programa que faça o computador escolher um numero de 0 a 5
e peça para o usuario adivinhar qual numero o computador escolheu
mostre na tela se o úsuario acertou ou errou'''
from random import randint
from time import sleep
# Fazendo o computador escolher um numero
r = randint(0, 5) # Randint é um metodo que escolhe um numero de 0 a 5.
print('-=-' * 30)
print('Tente adivinhar o numero que estou pensando de 0 a 5, vamos lá')
print('-=-' * 30)
# Pedindo para o usuario escolher um numero
u = int(input('Digite um numero de 0 a 5 --> '))
print('PROCESSANDO...')
sleep(3)
if u == r:
    print('PARABENS VOCÊ ACERTOU')
else:
    print('ERROU ! EU PENSEI NO NUMERO {} '.format(r))
