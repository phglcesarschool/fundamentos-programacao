# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos:
#  [0-25]
#  [26-50]
#  [51-75]
#  [76-100]
#
# A entrada de dados deverá terminar quando for lido um número negativo.
import os
import platform

if (platform.system() == "Linux") or (platform.system() == "Darwin"):
    os.system("clear")
elif platform.system() == "Windows":
    os.system("cls")

valor = intervalo1 = intervalo2 = intervalo3 = intervalo4 = 0

while valor >= 0:
    valor = int(input("Insira um valor inteiro: "))

    if valor < 0:
        break

    if 0 <= valor <= 25:
        intervalo1 =+ 1
    elif 26 <= valor <= 50:
        intervalo2 += 1
    elif 51 <= valor <= 75:
        intervalo3 += 1
    elif 76 <= valor <= 100:
        intervalo4 += 1

print(f"\nValores no intervalo [0-25]: {intervalo1}")
print(f"Valores no intervalo [26-50]: {intervalo2}")
print(f"Valores no intervalo [51-75]: {intervalo3}")
print(f"Valores no intervalo [76-100]: {intervalo4}")