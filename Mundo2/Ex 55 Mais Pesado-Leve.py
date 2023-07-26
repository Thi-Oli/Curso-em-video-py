'''Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi a maior e a menor'''
maior = 0
menor = 1
#1 - Pegar 5 valores de KG
for c in range(0,3):
    kg = float(input('Digite seu peso em KG '))

#2 - Pegar maior peso
if kg > maior:
    maior = kg
#3 - pegar menor peso
if kg > menor and maior > menor:
    menor = kg
print(maior)
print(menor)
