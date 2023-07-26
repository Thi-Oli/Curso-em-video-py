'''Crie um programa que leia vários números pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999 que é a condição de parada. No final mostre quantos números foi diitado e a soma entre eles.'''

#Flag = o número de parada.

# Pegando um valor
print('Se você digitar 999, o programa irá parar!')
n = int(input('Digite um valor de 0 a 998 ----> '))
soma = 0
cont = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um valor de 0 a 998 ----> '))

print('Cotagem {} - E a soma dos numeros digitados foram {}'.format(cont, soma))


