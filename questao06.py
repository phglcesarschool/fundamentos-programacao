# Escreva uma função que recebe uma lista e retorna outra contendo apenas os elementos que aparecem duas ou mais vezes na lista de entrada.
# Deve-se inserir valores inteiros na lista até receber o valor negativo (não inserir na lista)
#
#    >> reps(1,2,4,3,2,1,5) → [1,2]
#    >> reps(1,2,3) → []
import os
import platform

if (platform.system() == "Linux") or (platform.system() == "Darwin"):
    os.system("clear")
elif platform.system() == "Windows":
    os.system("cls")

def repetidos(lista_entrada):
    lista_final = []

    for valor in lista_entrada:
        if lista_entrada.count(valor) > 1:
            if lista_final.count(valor) == 0:
                lista_final.append(valor)
    
    lista_final.sort()

    return lista_final

lista_entrada = []

while True:
    valor = int(input("Informe um valor inteiro: "))

    if valor < 0:
        if len(lista_entrada) < 2:
            print("ATENÇA: A lista deve ter ao menos 2 valores")
            print(len(lista_entrada))
        else:
            print(repetidos(lista_entrada))
            break
    else:
        lista_entrada.append(valor)
        print(lista_entrada)
