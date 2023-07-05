#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
# de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa

#Ler os valores dos catetos.
import math
catop = int(input('Digite o valor do Cateto Oposto: '))
catad = int(input('Digite o valor do cateto Adjacente: '))

#hip = math.sqrt(catad + catop)
hip = math.sqrt(catop**2 + catad**2)

print('O comprimento da Hipotenusa é {:.3f}'.format(hip))




