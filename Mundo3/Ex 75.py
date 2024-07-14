
numpar = num9 = 0
num = (int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),)

for i in num:
    if i == 9:
        num9 =+ 1
print(f'Os numeros digitafos foram, {num}')
print(f'Apareceram o total de {num9} numero 9')

if 3 in num:
    print(f'O numero Três apareceu na {num.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado.')

print('Os numeros pares são:', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')



