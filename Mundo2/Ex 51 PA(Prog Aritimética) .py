'''Desenvolva uma programa que leia o primeiro termo e a razão de uma PA.
No Final mostre os 10 primeiros termos dessa progressão'''

#1 Coletando Primeiro termo e razão
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

#2 Fazendo a contagem dos 10 primeiros
pa = p + (10 - 1) * r #Formula para pegar os 10 primeiros termos
for c in range(p, pa+r, r):
    print(c, end=' ')

print('Acabou')

