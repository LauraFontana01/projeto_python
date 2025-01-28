# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 30/10/2024
# Estudos da biblioteca Math

# Importando as bibliotecas 
import os
import math


os.system('cls')

print('-'*50)
print('Estudos da Biblioteca Matemática MATH')
print('~'*50)
print()

# Declarações
base = 2
expoente = 3
angulo = 30
radicando = 81
co = 5 # cateto oposto
ca = 10 # cateto adjascente

# Processamento
potencia = math.pow(base, expoente)
raizQuadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(co, ca)

# Saida
print(f'{base} elevado a {expoente} é igual a: {potencia}')
print(f'A raiz quadrada de {radicando} é: {raizQuadrada}')
print(f'O seno de {angulo} é: {seno:.2f}')
print(f'O cosseno de {angulo} é: {cosseno:.2f}')
print(f'A tangente de {angulo} é: {tangente:.2f}')
print(f'O valor da hipotenusa é: {hipotenusa:.2f}')
print('-'*50)