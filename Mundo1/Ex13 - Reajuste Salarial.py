#Faça um algoritimo que acrescenta 15% no salario do funcionario e mostre a ele]

s = float(input("Digite seu salario: R$"))

a = s * 0.15
sf = s + a

print('Seu novo salário será de R${:.2f}, PARABENS!'.format(sf))