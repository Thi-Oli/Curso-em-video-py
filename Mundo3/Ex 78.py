# valor = list()
# menor = maior = 0
# for v in range(0, 5):
#     valor.append(int(input('Digite um valor: ')))

    

#     if valor[v] < menor:
#         menor = valor[v]

#     if valor[v] > maior:
#         maior = valor[v]
        


# valor.sort()
# print(menor)
# print(maior)
# print(valor)
# #print(valor.index())
# # print(valor[0])
# # print(valor[-1])

#----------------------------------------------------
valor = list()
for v in range(0, 5):
    valor.append(int(input('Digite um numero:')))
    

for c, v in enumerate(valor):
    print(f'Encontrei na posição {c} o valor {v}!')
    
valor.sort()
print(f'O maior valor digitado foi {valor[-1]}, e o menor foi {valor[0]}')
   
   
   