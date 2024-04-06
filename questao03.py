# Uma empresa tabular os resultados da seguinte enquete feita a umas organizações:
#
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
#
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
# O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
# Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
# Os valores referentes a cada uma das opções devem ser armazenados num vetor.
# Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.
import os
import platform

opcao = 10
lista_opcoes = 6*[0]  # Por que ser uma lista?
#lista_opcoes = [0,0,0,0,0,0]
total_votos = 0

while opcao != 0:
    if (platform.system() == "Linux") or (platform.system() == "Darwin"):
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    
    print(f"TOTAL DE VOTOS COMPUTADOS: {total_votos}\n")

    opcao = int(input("Digite a opção de sistema opercional utilizado na sua organização\n  1 - Windows Server\n  2 - Unix\n  3 - Linux\n  4 - Netware\n  5 - Mac OS\n  6 - Outro\nOpção escolhida: "))

    if 6 > opcao < 0:
        print('Número inválido, tente outra opção!')
    elif opcao == 0:
        print('\nPesquisa finalizada!')
        break
    else:
        #lista_opcoes[opcao - 1] = lista_opcoes[opcao - 1] + 1
        lista_opcoes[opcao - 1] += 1
        total_votos += 1

# Agora vamos imprimir o resultado

opcoes = ('Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro') # Por que ser uma tupla?
melhor = 0

print('Sistema Operacional: Votos - %')
print('------------------------------')

for i in range(len(lista_opcoes)):
    porcentagem = (lista_opcoes[i] / total_votos) * 100

    print(f"{opcoes[i]}: {str(lista_opcoes[i])} votos - {porcentagem:.1f}%")

    if lista_opcoes[i] > lista_opcoes[melhor]:
        melhor = i
    
print(f'\nTotal de votos: {total_votos}')

porcentagem_melhor = (lista_opcoes[melhor] / total_votos) * 100

print(f'O Sistema Operacional mais votado foi o {opcoes[melhor]}, com {lista_opcoes[melhor]} votos, correspondendo a {porcentagem_melhor:.1f} dos votos.')