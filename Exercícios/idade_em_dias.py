'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste
nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com
objetivo de testar raciocínio matemático simples.

Entrada:
O arquivo de entrada contém um valor inteiro.

Saída:
Imprima a saída conforme exemplo fornecido.
'''

tempo = ('Ano(s)', 'Mes(es)', 'Dia(s)')
escala = (365, 30, 1)
total= []

print('Insira sua idade em dias:')
a = int(input())
index = 0

for i in escala:
    m, a = divmod(a, i)
    total.append(m)

for i in tempo:
    print(f'{total[index]} {i}')
    index += 1