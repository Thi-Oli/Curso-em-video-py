lista = list()
cont = 0
while True:

    continuar = 's/n'
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar ? [S/N]')).upper()
    if continuar == 'N':
        break
    

lista.sort(reverse=True)
if 5 in lista:
    print('Numero 5 está na lista')
else:
    print('Numero 5 não está na lista.')
print(f'Foram digitados {cont} valores')
print(f'A lista ordenadar de forma descrescente é {lista}')


