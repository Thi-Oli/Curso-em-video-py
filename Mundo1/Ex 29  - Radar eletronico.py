'''Escreve um programa que leia a velocidade de um carro.
1ª se ele ultrapassar 80kmh, mostre uma mensagem dizendo que ele foi multado.
2ª A multa vai custar R$7,00 por cada Km acima'''

# Lendo um Kilometragem
k = float(input('Digite quantos Kmh você andou --> '))
if k > 80:
    print('Você passou do limite de 80Kmh, você foi multado')
    m = (k - 80) * 7
    print('O valor da multa ficou em R${:.2f}, mais ATENÇÂO !'.format(m))
print('Tenha um Bom dia , dirija com segurança !')