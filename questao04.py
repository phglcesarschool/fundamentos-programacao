# Faça um programa que carregue uma lista com os modelos de cinco carros. Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#   a) Quantos litros cada carro consome para percorrer 1000km e o quanto isto custará (considere o litro gasolina ao custo de R5,90)
#   b) O modelo mais econômico
#
import os
import platform

if (platform.system() == "Linux") or (platform.system() == "Darwin"):
    os.system("clear")
elif platform.system() == "Windows":
    os.system("cls")

carros = []
consumo = []
melhor_consumo = 0
gasolina = 5.90

for i in range(5):
    carros.append(input("Insira um modelo de carro: "))

for carro in carros:
    consumo.append(float(input(f"Quantos km/l faz o {carro}? ")))

for i in range(len(consumo)):
    if consumo[i] > melhor_consumo:
        melhor_consumo = consumo[i]
        carro_economico = carros[i]
    
    print(f"Para percorrer 1000km, o(a) {carros[i]} consome {(1000 / consumo[i]):.1f} litros ao custo de R${(consumo[i] * gasolina):.2f}")

print(f"\n O(A) {carro_economico} é o carro mais econômico!")
