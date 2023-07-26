'''Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores M e F. Caso contrario peça a digitação novamente até ter um valor correto'''

sexo = str(input('Digite seu sexo [M/F]: ')).upper()
while sexo != 'M' and 'F':
    sexo = str(input('Sexo inválido, digite seu sexo [M/F]: ')).upper()
if sexo == 'M' or 'F':
    print('Sexo {} guardado com sucesso !'.format(sexo))