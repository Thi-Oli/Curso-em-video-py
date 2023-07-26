'''Desenvolva um programa que pergunte a distancia da sua viagem e calcule em KM
Para viagens abaixo de 200km o preço é R$0,50
Para viagens acima de 200Km o preço é R$0,45 '''

# Lendo a distancia da viagem
d = int(input('Informe a distancia da sua viagem --> '))
'''if d < 200:
    print('O preço da viagem ficou em R${:.2f}, tenha uma boa viagem'.format(0.5 * d))
else:
    print('O preço da  viagem ficou em R${:.2f}, tenha uma boa viagem'.format(0.45 * d))'''
# Resposta
preco = d * 0.5 if d <= 200 else d * 0.45
print('O valor da sua viagem ficou em R${:.2f}'.format(preco))