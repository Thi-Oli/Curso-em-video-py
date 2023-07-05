'''Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00. Calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%.  '''

# Lendo o salário para calculo
s = float(input('Digite qual seu salário --> R$'))

if s <= 1250:
	sn = s + (s * 15 / 100)
	print('Seu novo salário é de R${:.2f}'.format(sn))
else:
	sn =s + (s * 10 / 100)
	print('Seu novo salário é de R${:.2f}'.format(sn))