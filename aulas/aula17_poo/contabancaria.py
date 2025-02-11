# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 11/02/2024
# Diferença entre: parametro (&) recebe valor padrão default e arguento ($) recebe valor real (valor inserido pelo usuario ou já definido; iteração)

import os


class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo, agencia, tipo_conta):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.agencia = agencia
        self.tipo_conta = tipo_conta


# Solicitando entrada de dados do usuário
print('-'*50)
os.system('cls')
numero_conta = input('Digite o número da conta: ')
nome_titular = input('Digite o nome do titular: ')
saldo = float(input('Digite o saldo inicial: '))
agencia = input('Digite a agência: ')
tipo_conta = input('Digite o tipo de conta: ')

# Criando um objeto da classe ContaBancaria com os dados fornecidos pelo usuário
conta = ContaBancaria(numero_conta, nome_titular, saldo, agencia, tipo_conta)

# Acessando e imprimindo atributos do objeto
print('-'*70)
print('\nInformações da Conta Bancária: ')
print('-'*70)
print(f'Número da Conta: {conta.numero_conta}')
print(f'Nome do Titular: ')
print(f'Saldo: {conta.saldo}')
print(f'Agência: {conta.agencia}')
print(f'Tipo de Conta: {conta.tipo_conta}')
print('-'*70)