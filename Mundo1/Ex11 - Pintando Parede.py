#Faça um programa que calcule a area quadrada de uma parede e mostre quantos litros de tinta deve se
#Usar para pinta-la, sabendo que 1 litro pinta 2m quadrados.

l = float(input('Digite a largura da parede: '))
al = float(input('Digite a altura da parede: '))

a = l * al
t = a / 2

print('Sua área é de {}m², você precisa de {:.2f}Litros de tinta.'.format(a , t))