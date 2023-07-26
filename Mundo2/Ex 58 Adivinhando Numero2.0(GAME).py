'''Melhore o EX 28 - O computador vai pensar em um numero de 0 até 10.
E o programa só vai acabar quando o usuario acertar mostrando quantas tentativas.'''

cont = 0
#Fazer o computador escolher um numero de 0 até 10.
from random import randint
computador = randint(1, 10)
#Pedir um numero ao usuario e comparar com a escolha do computador
jogador = int(input('Digite um valor de 1 a 10 :'))
while computador != jogador:
    jogador = int(input('Você não acertou! Digite outro valor: '))
# Fazer contagem de tentativas
    cont += 1
print('PARABÊNS! Você acertou e você tentou {} vezes para adivinhar!'.format(cont))
