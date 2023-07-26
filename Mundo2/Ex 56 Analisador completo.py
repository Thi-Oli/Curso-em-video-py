'''Analise os dados de 4 pessoas e me mostre qual é o nome da pessoa mais velha e a idade do sexo masculino.
E mostre quantas mulher abaixo de 20 anos tem.'''
media = 0
idadev = 0
nomev = ''
cont = 0
# Pegando info das pessoas.

for i in range(1,5):
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual seu sexo ? [M/F] ')).strip().lower()

#Pegar media
    media += idade / 4

#Pegar informações da pessoa mais velha
    if i == 1:
        nomev = nome
        idadev = idade
    else:
        if idade > idadev and sexo == 'm':
            idadev = idade
            nomev = nome

# Pegar informações de mulheres com idade inferior a 20
    if sexo == 'f':
        if idade < 20:
            cont += 1

print('A média de idade desse grupo é de {}'.format(media))
print('A pessoa mais velha tem {} anos e se chama {}'.format(idadev, nomev))
print('Tem {} mulher menor de idade.'.format(cont))