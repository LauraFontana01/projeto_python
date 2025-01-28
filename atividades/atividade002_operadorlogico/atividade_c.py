# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 29/10/2024
# Operadores Lógicos
# A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de velocidade para ajudar a promover a segurança nas estradas. Eles precisam de um programa que permita aos usuários inserir a velocidade de um carro e, em seguida, exibir na tela uma mensagem adequada com base na velocidade fornecida. O objetivo principal é alertar os motoristas caso ultrapassem o limite de velocidade de 60 km/h, incentivando-os a dirigir dentro dos limites legais e, assim, reduzir o risco de acidentes.
# inserir a velocidade de um carro e exibir na tela uma mensagem adequada com base na velocidade fornecida; objetivo principal é alertar os motoristas caso ultrapassem o limite de velocidade de 60 km/h

import os

os.system('cls')

print('-'*50)
print('SafeDrive: Segurança nas estradas!')
print('-'*50)

numero = float(input('Insira a velocidade que o carro estava: ' ))

if numero <= 60:
  print(f'Esse valor é inferior ao limite de velocidade!')
elif numero > 60:
   print(f'Esse valor é superior ao limite de velocidade!')
else:
   print()

print('-'*50)