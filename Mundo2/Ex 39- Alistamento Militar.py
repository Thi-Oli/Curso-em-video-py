'''Faça um programa que leia o ano de nascimento de um jovem e informe de acordo
com sua idade:
- Se ele AINDA VAI SE ALISTAR ao servico militar.
- Se não é a HORA DE SE ALISTAR.
- Se já PASSOU DO TEMPO do alistamento.
Seu pragrama deve mostrar quanto tempo falta e quanto tempo passou para o alistamento'''
# Coletando ano da maquina
from datetime import date
ano = date.today().year
# Coletando Ano de nascimento para analise
nascimento = int(input('Digite o ano que você nasceu --> '))
idade = ano - nascimento
if idade < 18:
    print("""Infelizmente você ainda não pode se alistar no Exército!
Ainda faltam {} anos para você se alistar !""".format(18 - idade))
elif idade == 18:
    print('Parabêns você vai ser alistado, pode trazer seus documentos amanhã de manhã!')
elif idade > 18:
    print("""Já se passou {} anos do alistamento, você vai direto para o Exercíto!
Pode trazer seus documento amanhã de manhã!""".format(idade - 18))
else:
    print('OBRIGADO !')

