'''Leia um nome completo
1ª O nome com todas letras maiusculas
2ª O nome com todas letras minusculas
3ª Quntas letras ao todo sem considerar espaços
4ª Quantas letras tem o primeiro nome'''

# Lendo um nome completo
nome = str(input('Digite seu nome completo -> ')).strip()
# Colocando o nome em maiusculo
print('Seu nome em maiusculo fica ->', nome.upper())
# Colocando seu nome em minusculo
print('Seu nome em minusculo fica ->', nome.lower())
# COntando quantas caracter sem contar espaços
#nome1 = nome.replace(' ', '')
print('Seu nome tem {} de caracteres sem contar os espaços'.format(len(nome) - nome.count(' ')))
#Quntas letras tem o primeiro nome
print('Seu primeiro nome tem {} caracteres'.format(nome.find(' ')))