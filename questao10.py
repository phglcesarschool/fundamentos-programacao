# Escreva um programa que leia um arquivo com um conjunto de nomes (1 por linha).
# O programa deve ordenar os nomes e gerar um novo arquivo com os nomes ordenados.

with open("questao10.txt", "r") as file:
    nomes = file.readlines()

    # Remover \n
    for idx in range(len(nomes)):
        nomes[idx] = nomes[idx].rstrip("\n")

    nomes.sort()
    print(nomes)

    with open("questao10_ordenado.txt", "w") as order_file:
        order_file.writelines("\n".join(nomes))