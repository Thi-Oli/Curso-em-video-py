import random

''' Importando Biblioteca random'''

from random import shuffle
#gravando nomes para sorteio
a1 = input('Digite um nome: ')
a2 = input('Digite um nome: ')
a3 = input('Digite um nome: ')
a4 = input('digite um nome: ')

alunos = [a1 , a2 , a3 , a4]
shuffle(alunos) # Shuffle utiliza-se para embaralhar uma lista
print('A ordem de apresentacao é:', alunos)