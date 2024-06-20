teste = ('Zero', 'Um', 'Dois', 'Três', 'Quartro', 'Cinco', 'Seis', 'Sete', 'Oito', 'nove'
       , 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito',
       'Dezenove', 'Vinte')


while True:
    num = int(input('Digite um numero entre 0 e 20:'))
    if 0 <= num <= 20:
        break
    print('Tente novamente,', end=' ')
print(f'Você digitou o numero {teste[num]}')
    