import random 
numero = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
print(numero)

print(f'O maior numero foi {max(numero)}')
print(f'O menor numero foi {min(numero)}')
