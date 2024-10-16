options = (''' Bem vindo(a)! O que você deseja fazer hoje ?
[1] Deposito 
[2] Saque
[3] Extrato
[4] Sair

--> ''')
extrato = ''
SAQUE_DIARIO = 3
LIMITE_SAQUE = 500
cont_saque = 0
deposito = 0

while True:    
    
    menu = int(input(options))
    
#menu 1 para deposito
    if menu == 1:
        print('Digite o valor que será depositado')
        deposito = float(input('R$ '))
        extrato += f'Valor depositado R${deposito:.2f}\n'

#menu 2 para saque
    elif menu == 2:
        if cont_saque <= SAQUE_DIARIO:
            saque = float(input('\nDigite o valor de saque: R$ \n'))
        else:
            print('Limite de saque atingido.')

#menu 2.1 -> Caso o saque seja maior que valor em conta.
        if saque > deposito:
            print(f'\nVocê não tem saldo em conta!\n')


#menu 2.2 -> Caso o saque seja maior que 500
        elif saque >= LIMITE_SAQUE:
            print('\nVocê ultrapassou seu limite de saque, tente de novo.\n')


#menu 2.3 -> Mostra saldo novo e faz contagem de saque
        else:
            deposito = deposito - saque
            print('Saque realizado! Obrigado')
            print(f'Seu saldo é de R${deposito}')
            cont_saque += 1
            extrato += f'Saque de R${saque:.2f}\n'

    elif menu == 3:
        print('EXTRATO'.center(40 , '='))
        print(f'\nNão houve transações\n'if not extrato else extrato)
        print('==' * 20)

            
           
    elif menu == 4:
        print('Saindo...')
        break


  
