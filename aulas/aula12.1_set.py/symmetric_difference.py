# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 02/12/2024
# Métodos para SET {}: symmetric_difference(set2) ou ^: Retorna um novo set 
# com elementos que estão em um dos sets, mas não em ambos.
 
import os


os.system('cls')

# Titulo
print('-'*50)
print('Testando o método Symmetric Difference no set! c:\n Brownies da Lau')
print('-'*50)

# Set
brownies_antes = {'Choconinho', 'Nesquik', 'Chocolate Branco', 'Tradicional', "Chocolate Crocante"}
brownies_depois = {'Duo Chocolate', 'Galak', 'Chocolate Crocante'}

# Saída Inicial
print(f'Menu Brownies até Novembro: {brownies_antes}')

# 
menunovo = brownies_antes.symmetric_difference(brownies_depois)

# Saída Final
print('.'*50)
print(f'Menu Brownies Novo - A partir de Dezembro: {menunovo}')