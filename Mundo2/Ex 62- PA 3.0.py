'''Melhore o exercício 61 perguntando se o usuário quer ver mais termos...'''

# Pegar primeiro termo e razão
p = int(input('Digite o primeiro termo -> '))
r = int(input('Razão -> '))
cont = 0
#Mostrar menu de escolha
print('''Escolha quantos termos você quer ver.
[1] Padrão
[2] Personalizado
[3] Trocar
[4] Encerrar''')
op = int(input('Escolha uma opção -> '))
# Criar looping de escolha
while op != 4:
    if op == 1:
        while cont < 10:
            p = p + r
            cont += 1
            print(p, end = ' -> ')
        print('Acabou')
        op = int(input('Escolha outra opção ou digite 4 para encerrar -> '))
    elif op == 2:
        pers = int(input('Digite quantos termos você quer ver -> '))
        while cont < pers:
            p = p + r
            cont += 1
            print(p, end=' -> ')
        print('Acabou')
        op = int(input('Digite outra opção ou digite 4 para encerrar -> '))
    elif op == 3:
        print('Ok, vamos trocar os valores para você.')
        p = int(input('Digite outro termo -> '))
        r = int(input('Digite outra razão -> '))
        print('''Escolha quantos termos você quer ver.
        [1] Padrão
        [2] Personalizado
        [3] Trocar
        [4] Encerrar''')
        op = int(input('Escolha uma opção -> '))

print('Obrigado, volte sempre!')


