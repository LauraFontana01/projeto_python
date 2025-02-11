# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 04/11/2024
# Biblioteca Math
# # º Receber número
# º Imprimir raiz quadrada do número.
# º Arredondar as raízes pra cima ou pra baixo.
# º Validar números negativos.
# º Avisar ao usuário que o resultado será um número complexo.

import os 

import math


os.system('cls')

print('-'*50)
print('Calculadora de Raiz Quadrada')
print('-'*50)

numero = float(input('Digite um número: '))



if numero < 0:
    print('O resultado será um número complexo!')
else:
    raizquadrada = math.sqrt (numero) # função math.sqrt(x) retorna a raiz quadrada de um número x. O valor de x deve ser positivo!
    arredondar_acima = math.ceil(raizquadrada) # função math.ceil(x) retorna o menor número inteiro maior ou igual a x. Rla arredonda o número para cima, para o próximo inteiro.
    print(f'A raiz quadrada de {numero} é: {arredondar_acima}')


print(f'-'*50)