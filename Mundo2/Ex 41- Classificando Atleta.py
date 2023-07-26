'''A confederação Nacional precisa de um programa que leia o ano de nascimento de
atletas e mostre sua categoria de acordo com a idade:
- Até 9 anos: MIRIM
- ATÉ 14 Anos: INFANTIL
- Até 19 Anos: JUNIOR
- Até 20 Anos: SÊNIOR
- ACIMA: MASTER'''

# Coletando ano
from datetime import date
ano = date.today().year
nascimento = int(input('Digite o ano que você nasceu -->'))
idade = ano - nascimento
print(idade)
if idade <= 9:
    print('Você tem {} anos, então você entra como MIRIM na CONFEDERAÇÃO NACIONAL !'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, então você entra como INFANTIL na CONFEDERAÇÃO NACIONAL !'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, então você entra como JUNIOR na CONFEDERAÇÃO NACIONAL !'.format(idade))
elif idade = 20:
    print('Você tem {} anos, então você entra como SÊNIOR na CONFEDERAÇÃO NACIONAL !'.format(idade))
elif idade > 21:
    print('Você tem {} anos, então você entra como MASTER na CONFEDERAÇÃO NACIONAL !'.format(idade))

print('OBRIGADO POR SE APRESENTAR ! E BOA SORTE !')
