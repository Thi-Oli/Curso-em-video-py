'''Refaça o Ex 9 mostrando a tabuada de um numero que o usuário escolher
Só que agora utilizando o metodo FOR'''

n = int(input('Digite um numero inteiro: '))
print('=-=' * 10)
for c in range(0, 10+1):
    v = n * c
    print('{} x {} = {}'.format(n, c, v))