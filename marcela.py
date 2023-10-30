# Exercício Python 29: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
peso = []

for massa in range(5):
    kg = float(input('Insira o valor de seu peso: '))
    peso.append(kg)

peso2 = sorted(peso)

print('O menor peso é:' , peso2[0])
print('O maior peso é:' , peso2[4])