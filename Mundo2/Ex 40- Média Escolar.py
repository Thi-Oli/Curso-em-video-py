'''Escreva um código que leia duas notas de um aluno e calcule sua média.
Mostrando uma mensagem no final de acordo com a média atingida.
- Média abaixo de 5.0:
REPROVADO
- Média entre 5.0 e 6.9:
RECUPERÇÃO
- Média 7.0 ou superior:
APROVADO'''

# Coletando duas notas
n1 = float(input('Digite a nota do primeiro bimestre --> '))
n2 = float(input('Digite a nota do segundo bimestre --> '))
# Calculando média
m = (n1 + n2) / 2
if m < 5.0:
    print("""Infelizmente você foi Reprovado, ESTUDE MAIS !'
Sua média foi de {:.2f}""".format(m))
elif m > 5.0 and m < 6.9:
    print("""Infelizmente você ficou de Recuperação
Sua média foi de {:.2f}""".format(m))
elif m > 7.0:
    print("""PARABÊNS você foi APROVADO !
Sua média foi de {:.2f}""".format(m))
