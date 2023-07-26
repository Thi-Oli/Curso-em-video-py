'''JOKEMPÔ'''
from random import randint
from time import sleep
print('==' * 20)
print('{:^40}'.format('VAMOS JOGAR JOKENPÔ'))
print('==' * 20)
sleep(0.5)
print('VOU ESCOLHER MEU ITEM PRIMEIRO')
sleep(0.5)
print('HMMMM....')
sleep(1)
print('CERTO! AGORA SUA VEZ')
sleep(0.5)
# Fazendo computador escolher
item = ('papel', 'tesoura', 'pedra')
computador = randint(0, 2)
# Jogador escolhando sua jogada
print('==' * 20)
jogador = int(input('''Escolha seu item !
[0] PAPEL
[1] TESOURA
[2] PEDRA 
Pode escolher -> '''))
print('==' * 20)
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)
print('==' * 20)
#Mostrando escolhas
print(f'COMPUTADOR JOGOU: {item[computador]}')
print(f'JOGADOR JOGOU: {item[jogador]}')
print('==' * 20)
# Resultado
if computador == 0: #Computador jogou PAPEL
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: # Computador jogou TESOURA
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JODADA INVALIDA')
elif computador == 2: # Computador jogou PEDRA
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')

