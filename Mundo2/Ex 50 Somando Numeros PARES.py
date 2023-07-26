'''Desenvolva um programa que leia 6 numeros e mostre apenas aqueles que forem PARES.]
Se o valor for impar-desconsidere'''

cont = 0
soma = 0

for c in range(1, 7):
    n = int(input('Digite o {}ª número inteiro: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você digitou {} Números PARES e a soma foi {}'.format(cont , soma))

