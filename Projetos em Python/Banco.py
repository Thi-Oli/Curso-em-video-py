print(''' Bem vindo(a)! O que você deseja fazer hoje ?
[1] Deposito 
[2] Saque
[3] Extrato
[4] Sair
''')
menu = int(input('Escolha uma opção!'))

while True:    
    
    
#menu 1 para deposito
    if menu == 1:
        print('Digite o valor que será depositado')
        deposito = float(input('R$ '))


#menu 2 para saque
    elif menu == 2:
        saque = float(input('Digite o valor desejado: R$ '))
#menu 2.1 -> Caso o saque seja maior que valor em conta.
        if saque > deposito:
            print('Você não tem saldo em conta!')
#menu 2.2 -> Caso o saque seja maior que 500
        elif saque > 500:
            print('Você ultrapassou seu limite de saque, tente de novo.')
            continue
#menu 2.3 -> Mostra saldo novo e faz contagem de saque
        else:
            deposito = deposito - saque
            print('Saque realizado! Obrigado')
            print(f'Seu saldo é de R${deposito}')

        
    elif menu == 3:
        print(f'''Segue abaixo extrato bancário:
            Depósito: {deposito}
            Ultimo Saque: {saque}''')
            
           
    elif menu == 4:
        print('Saindo...')
        break


    menu = int(input('''Escolha outra opção, ou digite 4 para sair.
    [1] Deposito 
    [2] Saque
    [3] Extrato
    [4] Sair
    '''))

  
