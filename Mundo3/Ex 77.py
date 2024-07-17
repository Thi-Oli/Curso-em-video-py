listagem = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in listagem:
    print(f'\nNa palavra {p.upper()}', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


