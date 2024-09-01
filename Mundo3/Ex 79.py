valor = list()

while True:
    continuar = 'n/a'
    val = int(input('Digite um valor: '))
    if val in valor:
        print('NÃO PODE REPETIR VALOR')
    else:
        valor.append(val)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar in 'N':
        break
valor.sort()
print(f'Os números digitados em ordem fica assim: {valor}')
print('OBRIAGDO!')


    
