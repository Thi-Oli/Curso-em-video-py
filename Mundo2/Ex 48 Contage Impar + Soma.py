'''Faça um programa que faça uma soma de todos os numeros impares que são multiplos de 3
e se encontra no intervalo de 0 a 500'''
s = 0
cont = 0
for c in range(0, 500, 3):
    if c % 3 == 0:
        s += c
        cont += 1
        print('A soma de todos os {} valores solicitados é {}'.format(cont, s))