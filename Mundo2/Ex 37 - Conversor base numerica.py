'''Escreva um programa que leia um numero inteiro qualquer e peça para o usuario
escolher qual a BASE DE CONVERSÃO:
1 para BINÁRIO
2 para OCTAL
3 para HEXADECIMAL'''

# Pedindo para escolher uma conversão
num = int(input('Digite um numero para conversão -> '))
print('=+=' * 20)
print("""Escolha um numero para conversão
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL""")
op = int(input('Digite aqui --> '))

# CONVERTENDO PARA BINARIO
if op == 1:
    nbin = bin(num)
    print('O número {} convertendo para BINÁRIO fica {}!'.format(num, nbin[2:]))
#Convertendo para OCTAL
elif op == 2:
    noc = oct(num)
    print('O número {} convertendo para OCTAL fica {}!'.format(num, noc[2:]))
#CONVERTENDO PARA HEXADECIMAL
elif op == 3:
    nhex = hex(num)
    print('O número {} convertendo para HEXADECIMAL fica {}'.format(num, nhex[2:]))

else:
    print('Digite uma opção válida para conversão !')

