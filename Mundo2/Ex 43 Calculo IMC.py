'''Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status de acordo
com a tabela abaixo:
- Abaixo de 18.5: ABAIXO DO PESO
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade  Mórbida'''

# Colentadno dados
altura = float(input('Digite sua altura em Metros -> '))
peso = float(input('Digite seu Peso em Kg -> '))
imc =  peso / (altura ** 2)
print (imc)

if imc < 18.5:
    print('Cuidado, seu IMC está abaixo do ideial.! Seu IMC é de {:.2f}'.format(imc))
elif imc <= 25:
    print('Muito bem, seu IMC é o ideal.! Seu IMC é de {:.2f}'.format(imc))
elif imc <= 30:
    print('Atenção você está com Sobrepeso.! Seu IMC é de {:.2f}'.format(imc))
elif imc <= 40:
    print('CUIDADO!, Você está com OBESIDADE! Seu IMC é de {:.2f}'.format(imc))
elif imc > 40:
    print('URGENTE! Você está com OBESIDADE MÓRBIDA! Seu IMC é de {:.2f}'.format(imc))
else:
    print('Siga as instruções de forma correta para realizar o calculo!')

print('Obrigado por utilizar nosso sistema, SE CUIDE !')
