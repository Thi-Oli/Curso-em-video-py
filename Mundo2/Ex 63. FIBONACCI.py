'''Faça um programa que leia um numero n inteiro e mostre os n primeiros numero
de uma sequencia de fibonacci'''


#Pegar quantos elementos vai mostrar
n = int(input('Quantos elementos você quer ver: '))
#Fazer looping
cont = 0
inicio = 0
começo = 1
fibo = 0
while cont != n:
    print(inicio)
    fibo = inicio + começo
    inicio = começo
    começo = fibo
    cont += 1

'''começo = int(input('Digite um valor: '))
contagem = int(input('Digite quantos valores: '))
inicio = 0
cont = 0

while cont != contagem:
    print(inicio)
    fibo = inicio + começo
    inicio = começo
    começo = fibo
    
    cont += 1
print('Acabou')'''




