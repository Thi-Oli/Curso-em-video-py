#Faça um programa que leia um angulo qual quer e mostre na tela seu seno, cosseno e tangente.
''' Os modulos sin(Seno), cos(Cosseno) e tan(Tangente), precisa do valor em radianos para converter a viável.'''

import math
angulo = float(input('Digite um Angulo: '))
coseno = math.cos(math.radians(angulo))
print('O Angulo {} tem seu Cosseno  {:.3f}'.format(angulo, coseno))
seno = math.sin(math.radians(angulo))
print('O Angulo {} tem seu Seno {:.3f}'.format(angulo, seno))
tang = math.tan(math.radians(angulo))
print('O Angulo {} tem a tangente {:.3f}'.format(angulo, tang))






