'''Refaça o exercício 51. Lendo o primeiro termo e a razão de uma PA.
Mostrando os 10 primeiros termos usando a estruta WHILE.'''

# Pedindo um n inteiro
p = int(input('Digite o primeiro termo> '))
r = int(input('Digite a razão> '))
cont = 0
# Fazer contagem até 10
# Criando looping

while cont < 10:
    p = p + r
    cont += 1
    print(p, end=' -> ')
print('Acabou')
