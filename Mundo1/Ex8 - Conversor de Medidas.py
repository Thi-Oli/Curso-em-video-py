#Escreva um programa que leia um valor em metros e converta ele em centimetros e milimetros

m = float(input('Digite um valor em metros:  '))

cm = m * 100
mm = m * 1000

print('Seu valor em metro é {}m, em centimetro fica {}cm e em Milimetro fica {}mm'.format(m, cm, mm))
