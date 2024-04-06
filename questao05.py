# Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais: taxa_imposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.
import os
import platform

if (platform.system() == "Linux") or (platform.system() == "Darwin"):
    os.system("clear")
elif platform.system() == "Windows":
    os.system("cls")

def somaImposto(taxa_imposto, custo):
    return custo + (custo * (taxa_imposto / 100))

custo = float(input("Informe o custo do item: "))
taxa_imposto = float(input("Informe a taxa do imposto (em %): "))

while (taxa_imposto < 0) or ( taxa_imposto > 100):
    print("ATENÇAO: A taxa deve estar entre 0 e 100")
    taxa_imposto = float(input("Informe a taxa do imposto (em %): "))

valor_final = print(f"O valor final do item - somado o imposto - é de R${somaImposto(taxa_imposto, custo):.2f}")