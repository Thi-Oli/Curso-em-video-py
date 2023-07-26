'''Faça um programa que pegue 3 valores em retas e veja se forma um triângylo'''

'''Forma de triângulo
Para cada lado deve ser menor que a soma dos outros dois
a < b + c
b < c + a
c < a + b'''
print('=-='*20)
print('ANALISADOR DE TRIANGULO')
print('=-='*20)
# Lendo três valores em retas.
a = float(input('Digite a primeira medida --> '))
b = float(input('Digite a segunda medida --> '))
c = float(input('Digite a terceira medida --> '))
# Aplicando fórmula
if a < b + c and b < a + c and c < a + b:
    print('Com essas medidas você forma um triangulo')

    if a == b and b == c and c == a:
        print('É um Triangulo EQUILATERO !')
    elif a == b or b == c or c == a:
        print('É um Triangulo ESCALENO')
    elif a != b and b != c and c != a:
        print('É um Triângulo ISÓCELES')
else:
    print('Com essas medidas você não forma um triangulo')

'''Refaça o DESAFIO 35 dos triangulos. Acrescentando o recurso de mostrar que tipo
de triangulo será:
- EQUILATERO: Todos os lados iguais
- ISÓCELES: Dois lados iguais
- ESCALENO: Todos os lados diferentes'''