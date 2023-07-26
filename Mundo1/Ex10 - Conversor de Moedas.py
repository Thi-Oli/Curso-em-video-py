#Crie um programa que converta seu saldo em dolar.

s = float(input('Digite seu saldo em conta R$'))
d = s / 5.06

print('Seu saldo é de R${:.2f}, e você pode comprar U${:.2f}, Obrigado.'.format(s, d))
