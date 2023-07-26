'''Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos
de artificio, indo de 10 até 0 com uma pausa de 1 seg entre eles.'''

import emoji
from time import sleep
for c in range(10,0, -1):
    print(c)
    sleep(0)
print(emoji.emojize("Estouro de Fogos de Artifício :fireworks:", variant='emoji_type'))