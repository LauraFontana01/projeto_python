# Calcule porcentagem de edsconto em roupitchas


import os


os.system('cls')

print('-'*50)
print('Calculadora de Descontos LauriRouperie: Tudo com 40 por centro de desconto')
print('-'*50)

roupa = float(input('Digite o valor da roupa escolhida: '))


operacao = roupa * 0.40
descontofinal = roupa - operacao

print(f'A roupa irá custar {descontofinal}')