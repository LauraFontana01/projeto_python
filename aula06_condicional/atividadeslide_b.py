# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 29/10/2024
# Operadores Lógicos
# A empresa "DataMax" está desenvolvendo um novo software de análise estatística e precisa de uma funcionalidade que permita aos usuários inserir três números e, em seguida, exibir na tela qual é o maior número, qual é o menor número ou se os números são todos iguais. Essa funcionalidade é crucial para os analistas de dados da "DataMax" que trabalham com conjuntos de dados diversos e precisam rapidamente identificar as características básicas desses conjuntos, como a presença de outliers ou a uniformidade dos números.
#  o maior número, qual é o menor número ou se 
# os números são todos iguais
import os

os.system('cls')

print('-'*50)
print('Análise Estatística DataMax')
print('-'*50)

numero1 = float(input('Digite um número:'))
numero2 = float(input('Digite outro número:'))
numero3 = float(input('Digite mais um número:'))

if numero1 == numero2 < numero3:
    resposta: f'{numero1} é igual a {numero2} e menores que {numero3}'
elif numero1 == numero2 > numero3:
    resposta:f'{numero1} é maior que {numero2} e igual a {numero3}'
elif numero1 > numero2 == numero3:
    resposta: f'{numero1} é maior que {numero2} e {numero3}'
elif numero1 < numero2 == numero3:
    resposta: f'{numero1} é menor que {numero2} e {numero3}'
elif numero1 > numero2 > numero3:
    resposta:f'{numero1} é maior que {numero2} e {numero3}'
elif numero1 < numero2 < numero3:
    resposta:f'{numero1} é menor que {numero2} e {numero3}'
elif numero1 > numero2 < numero3:
    resposta: f'{numero1} é maior que {numero2} e menor que {numero3}'
elif numero1 < numero2 > numero3:
   resposta: f'{numero1} é igual a {numero2} e {numero3}'
else:
    resposta:f'Os números {numero1}, {numero2} e {numero3} são iguais!'

print('-'*50)
print(resposta)
print('-'*50)