'''Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar
quando o usuario digitar o valor 999. Que é a condição de parada. No final , mostre quantos numeros
foram digitados e qual foi a soma entre eles'''

#Looping infinito
cont = soma = 0
print('Para sair do programa, digite 999')
while True:
    n = int(input('Digite um valor:'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f' Foram digitados {cont} números e a soma deles é de {soma}')

