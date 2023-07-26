#Faça um algoritimo que apresente ao cliente o produto com 5% de desconto.

p = float(input("Digite o preço do produto: R$"))
d = p * 0.05
pf = p - d
print('O preço com desconto deste produto é de R${:.2f}'.format(pf))