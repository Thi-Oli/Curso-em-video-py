#Desafio 03 Curso em Video ep4

num1 = int(input("Digite um valor: ")) # Caso não utilize o int no começo, o código não realizarar a soma e sim uma concateção das variáveis.

num2 = int(input("Digite outro valor: "))

soma= num1 + num2

#print("Seu resultado é: ", soma) Metodo utilizado no Python2, ainda funcional.

print('O resultado entre {} e {} é {}'.format(num1, num2, soma)) #A formatação segue a ordem colocada no .format.