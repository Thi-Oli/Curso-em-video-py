#Desenvolva um codigo que leia duas notas e mostre a media do aluno

#Guardar 2 variaveis para nota
#Fazer a divisao e mostrar a media

n1 = float(input('Digite sua nota : '))
n2 = float(input('Digite sua nota : '))

media = (n1 + n2) / 2

print('Sua media é de {:.2f}, Obrigado!'.format(media))