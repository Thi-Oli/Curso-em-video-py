'''Crie um programa que leia um valor de saque, e conte quantas notas foram utilizadas para realizar esse saque'''
cem = cinq = vint = dez = cinc = um = 0
saque = int(input('Digite o valor que deseja sacar R$'))
total = saque
ced = 50
totced = 0

'''Se o total for maior que a cédula, será substituido pelo valor da cédula'''
while True:
    if total >= ced:
        total -= ced
        totced += 1

    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        '''Se o valor total for menor que a cédula, entra nessa cadeia até encontrar o valor que dê para subtrair.'''
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break