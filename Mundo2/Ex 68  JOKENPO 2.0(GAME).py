'''Faça um programa que jogue PAR OU IMPAR com o computador.
O jogo só será interrompido quando o jogador PERDER. Mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.'''

from random import randint
vt = 0
#Computador e jogador escolhendo seu numeros
while True:
    computador = randint(0, 10)
    print('=-=' * 10)
    #Jogador escolhando PAR ou IMPAR, o que sobrar é do COMPUTADOR.
    print('''VAMOS JOGAR PAR OU IMPAR!
    [1] PAR
    [2] IMPAR''')
    print('=-=' * 10)
    escolha = int(input('FAÇA SUA ESCOLHA -> '))
    jogador = int(input('Escolha um numero de 0 a 10 -> '))
    print('~~~' * 10)
    #Mostrar o que cada jogador escolheu.
    print(f'Jogador escolheu {jogador} e Computador escolheu {computador}')
   #Verificador de PAR ou IMPAR.
    resultado = computador + jogador
    if resultado % 2 == 0:
        if escolha == 1:
            print('JOGADOR VENCEU!')
            vt += 1
        else:
            print('COMPUTADOR VENCEU!')
            break
    else:
        if escolha == 2:
            print('JOGADOR VENCEU!')
            vt += 1
        else:
            print('COMPUTADOR VENCEU')
            break
print('=-=' * 10)
print(f'Jogador venceu {vt} consecutivas')