'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e ultimo nome separadamente'''

# Lendo um nome
n = input('Digite seu nome completo -> ').strip()
print('Seu nome é', n)
print('==================================================')
n1 = n.title().split()
print('Seu primeiro é {} e o utimo é {}'.format(n1[0], n1[-1]))