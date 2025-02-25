
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

    
def criar_usuario (usuarios):
    cpf = int(input('Digite seu CPF.'))
    usuarios = filtrar_usuario(cpf, usuarios)
    nome = input('Informe o nome completo:')
    




def main ():
    LIMITE_SAQUE = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = int(menu())
        
        if opcao == 1:
            valor = float(input('Digite o valor que será depositado: R$ '))

            saldo , extrato = depositar(saldo, valor, extrato)




