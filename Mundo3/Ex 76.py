listagem = (
    'Abacaxi', 10.50,
    'Limão', 5.90,
    'Beterraba', 6.49,

)
print('_'*40)
print(f'{"TABELA DE PREÇOS":^40}')
print('_'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')
print('_'*40)