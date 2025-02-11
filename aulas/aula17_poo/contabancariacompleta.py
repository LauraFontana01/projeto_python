# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 11/02/2024
# Diferença entre: parametro (&) recebe valor padrão default e arguento ($) recebe valor real (valor inserido pelo usuario ou já definido; iteração)

import os

class Banco():
    def __init__(self, nome='', agencia=0, conta=0, cpf=0,
                 conta_corrente=0, poupanca=0):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.cpf = cpf
        self.conta_corrente = conta_corrente
        self.poupanca = poupanca

    def deposito(self, valor):
        escolha = input(
            'Conta Corrente (cc) ou Poupaça (po)? ').lower().strip()
        
        if escolha == 'cc':
            print(f'Valor do depósito: (+)R${valor}')
            print(f'Saldo anterior (CC): R${self.conta_corrente}')
            self.conta_corrente += valor
            print(f'\tSaldo atual na Conta Corrente: R${self.conta_corrente}')
            print('-'*70)

        elif escolha == 'po':
            print(f'\nValor do deposito: (+)R${valor}')
            print(f'\Saldo anterior na Poupança: R${self.poupanca}')
            self.poupanca += valor
            print(f'\tSaldo atual na Poupança: R${self.poupanca}')
            print('-'*70)

        else:
            print('Opção Inválida!')

        def saque(self, valor):
            escolha = input(
                'Conta corrente (cc) ou Poupança (po)?').lower().strip()
            
            if escolha == 'cc':
                print(f'\nValor sacado: (-)R${valor}')
                print(f'\Saldo anterior na CC: R${self.conta_corrente}')
                self.conta_corrente -= valor
                print(f'\tSaldo Atual na CC: R${self.conta_corrente}')
                print('-'*70)

            elif escolha == 'po':
                print(f'\nValor sacado: (-)R${valor}')
                print(f'\Saldo anterior em Poupança: R${self.poupanca}')
                self.poupanca -= valor
                print(f'\tSaldo Atual na Poupança: R${self.poupanca}')
                print('-'*70)

            else:
                print('Opão Inválida!')


os.system('cls')

# Coletar dados do usuário para criar uma nova conta
print('Digite os dados para criar uma nova conta: ')
nome = input('Nome: ')
agencia = int(input('Agência: '))
conta = int(input('Número da Conta: '))
cpf = int(input('CPF: '))
conta_corrente = float(input('Saldo inicial da Conta Corrente: '))
poupanca = float(input('Saldo inicial da Poupança: '))


# Criar um novo correntista
correntista = Banco(nome, agencia, conta, cpf, conta_corrente, poupanca)


print('-'*70)
print('Movimentação Bancária')
print('-'*70)
opcao = input('Depósito ou saque (D/S)?').upper().strip()

if opcao == 'D':
    valor = float(input('Qual o valor do deposito? '))
    correntista.deposito(valor)

elif opcao == 'S':
    valor = float(input('Qual o valor do saque? '))
    correntista.saque(valor)

else: 
    print('Opção Inválida!')
