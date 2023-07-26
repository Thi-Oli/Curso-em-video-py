'''Crie um programa que leia vários numeros inteios. Mostre a média entre todos
os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer continuar'''

# Pegar valores
print('Caso queira PARAR é só digitar PARAR')
v1 = int(input('Digite um valor: '))
ok = str(input('Digite continuar, para continuar: ')).strip().lower()
media = 1
menor = v1
soma = 0
maior = 0
# Criar contagem para média
while ok == 'continuar':
    media += 1
    v = int(input('Digite um valor: '))
    if v > maior:
        maior = v
    if v < menor:
        menor = v
    soma += v
    ok = str(input('Digite continuar, para continuar:  ')).strip().lower()

    if ok != 'continuar':
        print('A soma dos valores digitados foi de {}'.format(soma + v1))
        valor_media = (soma + v1) / media
        print('A média dos valores digitados é de {:.2f}'.format(valor_media))
    # Guardar valor primeiro valor para comparar MAIOR e MENOR.

print('O maior valor entre os valores digitados foi {}'.format(maior))
print('O menor valor entre os valores digitados foi {}'.format(menor))

