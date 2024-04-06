# Uma pesquisa foi feita e cada pessoa respondeu ao seguinte questionário:
#      Sexo: ( )M ( )F
#      Idade: ____ anos
#      Você é um zumbi: ( )S ( )N
#      Você é vegetariano: ( )S ( )N
# Considere um arquivo que contém as respostas de todas as pessoas entrevistadas. Considere que as respostas foram armazenadas da seguinte forma:
#      a) um entrevistado por linha e suas respostas separadas por vírgulas:
#          1) sexo (um caracter, podendo ser ‘M’,‘F’)
#          2) idade
#          3) zumbi (um caracter, podendo ser ‘S’ ou ‘N’)
#          4) vegetariano (um caracter, podendo ser ‘S’ ou ‘N’)
# Faça um programa que leia este arquivo e devolva as seguintes informações:
#      • Qual é o percentual de zumbis em relação ao número total de pessoas entrevistadas?
#      • Qual é o percentual de homens não zumbificados abaixo de 40 anos em relação ao número total de homens entrevistados?
#      • Qual é o percentual de mulheres zumbificadas acima de 40 anos, que são vegetarianas, em relação ao número total de mulheres entrevistadas?
#
# Vamos assumir que cada linha do arquivo termina com ',', sem isso, após a função str.split(), o último elemento da lista terminará com '\n' (e.g. “S\n”)
import os
import platform

if (platform.system() == "Linux") or (platform.system() == "Darwin"):
    os.system("clear")
elif platform.system() == "Windows":
    os.system("cls")

total_pessoas = total_zumbis = total_homens = total_mulheres = 0 
total_HNZMe40 = 0 # total de homens nao zumbis com menos de 40 
total_MZMa40V = 0 # total de mulheres zumbis, com mais de 40 e vegetarianas

with open("questao09.txt", "r") as frelatorio:
    linhas_relatorio = frelatorio.readlines()

    for linha in linhas_relatorio:
        respostas = linha.split(",")

        # Adiciona em caso de zumbi
        if respostas[2] == "S":
            total_zumbis += 1
        
        # Adiciona ao total de homens
        if respostas[0] == "M":
            total_homens += 1

            # Adiciona se não zumbificado e abaixo de 40 anos
            if int(respostas[1]) < 40 and respostas[2] == "N":
                total_HNZMe40 += 1
        elif respostas[0] == "F":
            total_mulheres += 1

            if int(respostas[1]) > 40 and respostas[2] == "S" and respostas[3] == "S":
                total_MZMa40V += 1
        
        total_pessoas += 1

perc_zumbi = (total_zumbis * 100) / total_pessoas
print(f"Percentual de zumbis: {perc_zumbi:.1f}%")

perc_HNZMe40 = (total_HNZMe40 * 100) / total_homens
print(f"Percentual de homens não zumbificados abaixo dos 40 anos: {perc_HNZMe40:.1f}%")

perc_MZMa40V = (total_MZMa40V * 100) / total_mulheres
print(f"Percentual de mulheres zumbificadas acima dos 40 anos e vegetarianas: {perc_MZMa40V:.1f}%")