lista = list()
par = list()
impar = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar ? [S/N] ')).upper()
    if continuar in 'N':
        break

for v in lista:

    if v % 2 == 0:
        par.append(v)

    elif v % 2 == 1:
        impar.append(v)

print(lista)
print(par)
print(impar)
