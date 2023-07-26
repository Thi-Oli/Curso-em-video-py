#Monte um algoritimo que leia um valor e mostre seu dobro / triplo e raiz quadrada

#Crie uma variavel que receba um valor inteiro

n = int(input('Digite um valor!  ->'))

d = n * 2
t = n * 3
r = n ** (1/2)

print('Seu numero escolhido foi {}, o valor dobrado é de {}, o valor em triplo {} e a raiz é de {}'.format(n, d, t, r))

