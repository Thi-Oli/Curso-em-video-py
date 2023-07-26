'''Faça um programa que mostre a tabuada de vários números, um de cada vez. para cada
valor digitado pelo usuario.O programa será intenrrompido quand o numero for negativo'''

print('TABUADA 3.0 (DIGITE UM NUMERO NEGATIVO PARA SAIR DO PROGRAMA!')
#Escolhendo valor da tabuada
while True:
    valor = int(input('Qual tabuada você quer ver ->'))
    #Fazendo BREAK de numero negativo
    if valor < 0: #Qual quer valor menor que ZERO é negativo!
        break
    #Fazendo Tabuada de 1 a 10.
    for c in range (1, 10+1):
        r = valor * c
        print(f'{valor}x{c}={r}')

print('FIM')