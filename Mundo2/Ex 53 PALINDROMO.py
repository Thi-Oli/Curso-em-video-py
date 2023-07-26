'''Crie um programa que leia uma frase qual quer e diga se ela é um
polindroma. Desconsiderando os espaços.
EX: APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MAROTONA'''

#Pegando uma frase
f = str(input('digite uma frase: ')).strip().lower()
# Criar variavel nova para separar
fs = f.split()
junto = ''.join(fs)
# Criar uma variavel para pegar o inverso
inverso = ''
# Criando looping para inverter a frase
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
#Comparando inverso e junto
if inverso == junto:
    print('É um POLINDROMO')
else:
    print('NÂO É POLINDROMO')



