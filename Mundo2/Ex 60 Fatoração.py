'''Faça um programa que leia um numero qual quer e mostre o seu fatoramento.
EX: 5! = 5x4x3x2x1 = 120 '''

#Pegar um valor n
n = int(input('Digite um valor: '))
resultado = 1
count = 1
#Looping do valor n até 1
while count <= n:
    resultado *= count
    count += 1
print(resultado)


