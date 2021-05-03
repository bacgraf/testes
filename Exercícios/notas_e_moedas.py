'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule
o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50,
20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas
necessárias.

Entrada:
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída:
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''


cedulas = (100, 50, 20, 10, 5, 2, 1)
moedas = (1, 0.5, 0.25, 0.10, 0.05, 0.01)
total = []
total2 = []

print('Insira o valor:')
a = float(input())
index = 0
indexm = 0
inteiro = int(a)
decimal = round((a-inteiro)*100,0)


for i in cedulas:
    c, inteiro = divmod(inteiro, i)
    total.append(c)

for i in moedas:
    m, a = divmod(a, i)
    total2.append(m)


for i in cedulas:
    print(f'{total[index]} notas de R$ {i},00')
    index += 1

for i in moedas:
    print(f'{total2[indexm]} moedas de R$ {i}')
    indexm += 1

