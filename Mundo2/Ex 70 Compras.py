'''Faça um programa que leia produtos e indetifique, qual o total gasto, produtos que custam mais de
R$1.000 e qual o nome do produto mais barato '''
contproduto = soma = valor1k = 0

while True:
    produto = str(input('Qual produto ? ')).strip().upper()
    valor = int(input('Qual valor ? R$'))
    valormenor = valor
    contproduto += 1
    soma += valor
    produto1 = produto

    if valor > 1000:
        valor1k += 1

    if valor < valormenor:
        valormenor = valor
        produto1 = produto

    '''Parando o sistema'''
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print('=*=' * 20)
print(f'''Pronto!
Seu gastou total foi de R${soma}.
Você está comprando {valor1k} itens acima de R$1.000
O item mais barato que você comprou foi {produto1} que custa R${valormenor}
''')