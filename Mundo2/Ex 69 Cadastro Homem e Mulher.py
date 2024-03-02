'''Faça um programa que leia o sexo e me diga quantas pessoas maior de 18, quantas mulheres menor de 18 e quantos homem foram cadastrados.
'''
homem = 0
idadem = 0
mulher = 0
idadef = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F] ?')).upper().strip()[0]

    '''Fazendo contagem de Sexo e idade'''
    if idade >= 18:
        idadem += 1
    if sexo == 'M':
        homem += 1
    if idade < 18 and sexo == 'F':
        mulher += 1

    '''Parando o sistema de cadastro'''
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break

print('=*+' * 20)
print(f'''Nesse cadastro encontramos:
{homem} Homens cadastrados.
Foram cadastrados {idadem} maior de idade.
{mulher} Mulheres com menos de 18 anos.
''')



