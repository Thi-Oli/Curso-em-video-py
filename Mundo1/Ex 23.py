'''Faça um programa que leia de 0 a 9999 e separe
sua Unidade , dezena , centena e milhar'''

# Lendo um numero
n = int(input('Digite um numero de 0 a 9999 -> '))
print('O número escolhido foi ', n)
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade é {}'.format(u))
print('Dezena é {}'.format(d))
print('Centena é {}'.format(c))
print('Milhar é {}'.format(m))