'''Escreva um programa para aprovar um empréstimo bancário para a compra de um imóvel.
O programa vai perguntar o VALOR DA CASA , o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar'''

'''Calcule o valor da prestação mensal. Sabendo que não pode exceder 30% do salário ou então o empréstimo
será negado'''

# Lendo os valores SALARIO, PARCELAS, VALOR DA CASA.
s = float(input('Digite seu salário !  R$'))
vc = float(input('Digite o valor do imóvel !  R$'))
p = int(input('Digite em quantos anos pretende pagar !  '))

# Calculando Ano e valor do imovel por Mês
parcela = p * 12
vcasa = vc / parcela
# Calculando 30% do salario
salario = s * 30 / 100

if vcasa < salario:
    print("""PARABÊNS ! Seu empréstimo para comprar seu imóvel foi aprovado !
          Ficaram {} parcelas de R${:.2f} em {} Anos , Obrigado""".format(parcela, vcasa, p))
else:
    print('Infelizmente não será possivel')


