# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 30/10/2024
# Operadores Lógicos
# A empresa "RootCalc" está desenvolvendo um software de cálculo de raízes de equações quadráticas para auxiliar engenheiros e cientistas em suas análises e projetos. Eles precisam de um programa que calcule as raízes da equação quadrática 𝑥²−6𝑥+5 sem depender de funções ou métodos predefinidos, utilizando apenas os conceitos e operações básicas aprendidos até o momento. Essas raízes são conhecidas como 𝑥’ = 5 e 𝑥’’ = 1, e o programa deve ser capaz de calcular essas raízes de forma precisa, seguindo os princípios matemáticos fundamentais.
# 𝑥²−6𝑥+5 

import os


os.system('cls')

print('-'*50)
print('RootCalc: Cálculo de raízes de equações quadráticas!')
print('-'*50)

a = 1
b = -6
c = 5
resposta = ''

# Processamento // a potencia vem primeiro!
delta = (b ** 2) - (4 * a * c)
raiz_delta = delta ** 0.5 
raiz_1 = b 
