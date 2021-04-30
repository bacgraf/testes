'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por
 hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas
  decimais.

Entrada:
O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número,
quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

Saída:
Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois
da igualdade. No caso do salário, também deve haver um espaço em branco após o $.

# >>>25
# >>>100
# >>>5.5
# Numero = 25
# Salario = R$ 550.00
#
# >>>1
# >>>200
# >>>20.50
# Numero = 1
# Salario = R$ 4100.00
'''

print('Insira o número do funcionário: ')
num = int(input())
print('Insira as horas trabalhadas: ')
horas = int(input())
print('Insira o valor hora: ')
val_hora = float(input())

print(f'Numero = {num}')
sal = horas * val_hora
print(f'Salario = {sal}')