# Autor: Laura Fontana
# Data: 30/10/2024
# Estudos pra provuska de amanhã
# Medias Escolares onde abaixo de 3 é reprovado, menor que 5 é recuperação e maior que 7 passou de ano
import os


os.system('cls')

print('-'*50)
print('Calculadora de Médias Escolares')
print('-'*50)

nota1 = float(input('Digite a 1ª Nota: '))
nota2 = float(input('Digite a 2ª Nota: '))
nota3 = float(input('Digite a 3ª Nota: '))

if (nota1 + nota2 + nota3 / 3) > 7:
    print('Parabéns, você foi aprovado!')
elif (nota1 + nota2 + nota3 / 3) >= 5:
    print('Você está de recuperação!')
else:
    print('Você está reprovado!')

print('-'*50)

    

