'''Crie um programa que leia o nome de uma cidade e diga
se ela começa ou não com a palavra 'Santo' '''

# Lendo o nome da cidade
n = str(input('Digite o nome da sua cidade -> ')).strip()
n1 = n.capitalize().split()
print('Santo' in n1[0])

'''Resposta
n = str(input('Digite o nome da sua cidade')).strip()
print(n[:5].upper == 'SANTO']
'''

