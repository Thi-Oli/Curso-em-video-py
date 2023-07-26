'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] SOMA
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA'''

#Pegar dois valores
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
#Fazer usuário escolher uma opção
print('''[1] SOMA
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA''')
op = int(input('Escolha uma opção: '))
#Criar looping
while op != 5:
    if op == 1:
        soma = v1 + v2
        print('A soma dos valores escolhidos é {}'.format(soma))
        op = int(input('Escolha outra opção: '))
    elif op == 2:
        mult = v1 * v2
        print('A multiplicação dos valores escolhidos é de {}'.format(mult))
        op = int(input('Escolha outra opção: '))
    elif op == 3:
        if v1 > v2:
            print('O maior numero foi {}'.format(v1))
            op = int(input('Escolha outra opção: '))
        else:
            print('O maior numero foi {}'.format(v2))
            op = int(input('Escolha outra opção: '))
    elif op == 4:
        print('OK! Vamos escolher outros numeros!')
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
        op = int(input('Escolha uma opção: '))

print('FINALIZANDO PROGRAMA!')

