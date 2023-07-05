'''Faça um programa que informe se o ano pe bisexto ou não'''

'''a = int(input('Digite o ano que quer saber se é bisexto ou não --> '))
b = (a % 4)+((a % 100) != 0)+(a % 400)
if b == 0:
	print('O Ano {} é BISEXTO'.format(a))
else:
	print(' O Ano {} NÃO BISEXTO'.format(a))'''

##Resposta
from datetime import date

ano = int(input('Que ano você quer analisar ?'))
if ano == 0:
	ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print('O ano {} é BISEXTO'.format(ano))
else:
	print('O ano {} NÂO É BISEXTO'.format(ano))