''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''

# Lendo 3 valores

v1 = int(input('Digite um valor -->'))
v2 = int(input('Digite um valor -->'))
v3 = int(input('Digite um valor -->'))

# Colocando em ordem crescente usando o metodo .SORTED
lista = [v1, v2, v3]
lista1 = sorted(lista)
print('O menor número é {} e o menor é {}'.format(lista1[0], lista1[-1]))

'''Resposta
a = int(input('Digite um valor -->'))
b = int(input('Digite um valor -->'))
c = int(input('Digite um valor -->'))
# Analisando o número menor.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Analisando o númeo maior.    
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior número que você digitou foi {} e o menor foi {}, OBRIGADO !'.format(menor, maior))    

'''
