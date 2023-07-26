'''Crie um programa que leia o nome de uma pessoa e diga se ela
tem "Silva" no nome'''

# Lendo um nome
n = input('Digite seu nome -> ').strip()
n1 = n.title()
print('Silva' in n1)

'''Resposta
nome = str(input('Digite seu nome')).strip()
print('Seu nome tem silva ? {}'.format('silva' in nome.lower()))
'''