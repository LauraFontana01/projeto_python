# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 02/12/2024
# Métodos para SET {}: remove(elemento): Remove um elemento do set. 
# Lança um erro se o elemento não estiver presente.

import os


os.system('cls')

# Titulo
print('-'*50)
print('Testando o método remove no set! c:\n Brownies da Lau - estoque')
print('-'*50)

# Set
brownies = {'Choconinho', 'Nesquik', 'Chocolate Branco'}

# Saída Inicial
print(f'Brownies Prontos: {brownies}')

# Remover sabor já vendido (se remover algo inexistente, resulta-rá em erro)
brownies.remove('Choconinho')

# Saída Final
print('.'*50)
print(f'Brownies Restantes: {brownies}')