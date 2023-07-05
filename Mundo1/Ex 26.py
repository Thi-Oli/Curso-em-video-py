''' Faça um programa que leia uma frase e mostre
1ª Qyatas x aoarece a letra 'A'
2ª Em que posição ela aparece a primeira vez
3ª Em que posição ela mostra pela ultima vez'''

# Lendo a frase
f = str(input('Digite uma frase qual quer -> ')).strip()
# Contando quantas x a letra "a" aparece
print('Esta frase tem {} letras "a"'.format(f.lower().count('a')))
# Em que posição ela aparece na primeira vez.
f1 = f.lower().split()
print('A letra "a" aparece no indice {} da primeira palavra'.format(f1[0].find('a')))
# Em que posição aparece na ultima palavra
print('A letra "a" aparece no indice {} da ultima palavra'.format(f1[-1].find('a')))


'''Resposta
f = str(input('Digite uma frase')).lower().strip()
print('Nesta frase tem {} letras A'.format(f.count('a')))
print('A letra aparece na porsição {} da frase'.format(f.find('a') +1))
print('A ultima letra A aparece na posição {} da frase'.format(f.rfind('a') +1))
'''


