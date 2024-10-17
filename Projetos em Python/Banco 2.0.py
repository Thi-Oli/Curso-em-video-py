
def menu():
    print('{:=^40}'.format(' MENU '))
    print(''' Digite a opção desejada
        [1]Deposito
        [2]Saque
        [3]Extrato
        [4]Sair

        -> ''')
    
    
def sacar(numero_saque, limite, limite_saque, extrato, saldo, valor):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saque
    
    if excedeu_saldo:
        print('Operação Falhou! Você não tem saldo para sacar!')

    elif excedeu_limite:
        print('Operação Falhou! Você excedeu o limite de saque!')

    elif excedeu_saque:
        print('Operação Falhou! Você excedeu o limite de saque diario!')

    elif valor > 0:
        saldo -= valor
        print('Saque realizado! Obrigado')
        limite_saque += 1
        extrato += f'Saque de R${valor:.2f}'

    return saldo, extrato


def depositar (saldo, valor, extrato):
    if valor > 0:
        saldo = float(input('Digite o valor de deposito R$'))
        extrato += f'Valor deposito R${valor:.2f}'   

        return saldo, extrato


def extrato(saldo, extrato):
    print(':=^40'.format(' MENU '))
    print('Não houve transações\n' if not extrato else extrato)
    print('=' * 20)


