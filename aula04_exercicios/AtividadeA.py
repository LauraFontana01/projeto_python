# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 25/10/2024

# Comando usado para importar a biblioteca do sistema operacional
import os

# Limpeza do terminal
os.system('cls')

# Titulo bonitinho
print('-'*70)
print('Calculando Operações Aritméticas')
print('-'*70)

# Entrada de dados
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite um número diferente do anterior:'))
numero3 = float(input('Digite outro número diferente dos anteriores:'))

# Processamento de operações
soma = numero1 + numero2 + numero3
multiplicacao = numero1 * numero2 * numero3

# Saida de dados
print('=' * 70)
print(f'A soma dos três valores fornecidos é: {soma:.2f}')
print('=' * 70)
print(f'Já os três valores multiplicados resulta em: {multiplicacao:.2f}')
print('=' * 70)