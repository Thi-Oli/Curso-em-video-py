'''Elabora um programa que leia o preço de um produto, considerando o seu
PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO
- À vista DINHEIRO/CHEQUE: 10% de desconto
 - À vista no CARTÃO: 5% de desconto
 - Em até 2x no cartão: PREÇO NORMAL
 - 3x ou mais: 20% de juros'''

#Colentando dados
vproduto = float(input('Digite o valor do produto -> R$'))
print("""Digite a opção de pagamento !
[1] À vista DINHEIRO ou CHEQUE
[2] À vista no CARTÂO
[3] No CARTÃO em 2x
[4] NO CARTÃO em 3x ou MAIS""")
op = int(input("""Escolha uma opção!
Digite aqui -> """))
if op == 1:
    print('Você recebeu 10% de desconto em sua compra! Valor total a pagar é de R${:.2f}.'
        .format(vproduto - (vproduto * 10 / 100)))
elif op == 2:
    print('Você recebeu 5% de desconto em sua compra! Valor total a pagar é de R${:.2f}'
          .format(vproduto -(vproduto * 5 / 100)))
elif op == 3:
    parcela = vproduto / 2
    print('Sua compra de R${:.2f} em 2x sem juros, ficando 2 parcelas de R${:.2f} '.format(vproduto, parcela))
elif op == 4:
    parcela = int(input('Quantas parcelas ? '))
    juros = vproduto + (vproduto * 20 / 100)
    vparcela = juros / parcela
    print('Sua compra irá ficar R${:.2f}, ficando {}x de R${:.2f}'.format(juros, parcela, vparcela))
else:
    print('Escolha uma opção de PAGAMENTO!')
print('VOLTE SEMPRE')
