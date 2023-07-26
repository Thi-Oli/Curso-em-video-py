'''Escreva um programa que leia dois valores inteiros
compare-os. Mostrando na tela uma mensagem:
- O Primeiro numero é MAIOR
- O Segundo numero é MENOR
- Os dois são iguais'''

# Coletando DOIS números inteiros
n1 = int(input('Digite um número --> '))
n2 = int(input('Digite outro numero --> '))
# Comparando os numeros
if n1 > n2:
    print('O primeiro número é maior que o segundo')
elif n2 > n1:
    print('O segundo número é maior que o primeiro')
elif n1 == n2:
    print('Os dois números são iguais')
print('Obrigado !')