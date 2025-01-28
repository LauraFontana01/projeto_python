# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 29/10/2024
# Operadores Lógicos
# A empresa "DataMax" está desenvolvendo um novo software de análise estatística e precisa de uma funcionalidade que permita aos usuários inserir três números e, em seguida, exibir na tela qual é o maior número, qual é o menor número ou se os números são todos iguais. Essa funcionalidade é crucial para os analistas de dados da "DataMax" que trabalham com conjuntos de dados diversos e precisam rapidamente identificar as características básicas desses conjuntos, como a presença de outliers ou a uniformidade dos números.

import os

os.system('cls')

print('-'*50)
print('Análise Estatística DataMax')
print('-'*50)

a = float(input('Digite um número:'))
b = float(input('Digite outro número:'))
c = float(input('Digite mais um número:'))

# Cada proposição é uma resposta diferente que está sendo inserida
if (a == b) and (b == c) :
    print('Os números são iguais!')
elif (a > b) and (b > c):
    print(f'{a} é o maior número!')
elif (b > a) and (a > c):
    print(f'{b} é o maior número!')
else:
    print(f'{c} é o maior número!')

# Por ser dois grupos de códigos, a resposta poderá se duplicar caso seja igual
if (a == b) and (b == c) :
    print()  # repetir mesmo em branco para que ela não seja repetida novamente
elif (a < b) and (b < c):
    print(f'{a} é o menor número!')
elif (b < a) and (c < a):
    print(f'{b} é o menor número!')
else:
    print(f'{c} é o menor número!')



print('-'*50)
print('')
print('-'*50)