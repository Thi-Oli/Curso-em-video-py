'''Um professor quer sortear um dos quatro alunos para apagar o quadro.
Faça um programa que ajude ele lendo o nome deles e escrevendo o nome escolhido.'''

import random

a1 = input('Digite um nome:')
a2 = input('Digite mais um nome:')
a3 = input('Digite mais um nome:')
a4 = input('Digite mais um nome:')

lista = [a1, a2, a3, a4]
print('O nome sorteado foi', random.choice(lista))
# Choice é utilizado para celecionar apenas 1 item da lista.