import os
import datetime

def choose():
    def quest01():
        print("\n--->> Questão 01 <<---")

        soma_areas = 0
        areas = []
        qtd_vendas = int(input("Quantas vendas foram realizadas no dia? "))
    
        for reps in range(qtd_vendas):
            area = float(input(f"Digite a área do apartamento {reps + 1}: "))
            soma_areas += area
            areas.append(area)
    
        print(f"\nSoma das áreas de todas as vendas: {soma_areas:.2f}m²")
        print(f"Menor área dos apartamentos {min(areas):.2f}m²")
        print(f"Maior área dos apartamentos {max(areas):.2f}m²")

    def quest02():
        print("\n--->> Questão 02 <<---")

        nomes = []
        nomes_lidos = []
        lista_final = []

        while True:
            novo_nome = input("Digite o nome do aluno(a): ")

            if novo_nome.capitalize() == "Sair":
                break
            else:
                nomes.append(novo_nome)

        with open("./conversadores.txt", "w", encoding="utf8") as file:
            file.writelines("\n".join(nomes))

        with open("./conversadores.txt", "r", encoding="utf8") as file:
            nomes_lidos = file.read().split()
            nomes_lidos_capitalize = [nome.capitalize() for nome in nomes_lidos]

            for nome in nomes_lidos_capitalize:
                if nomes_lidos_capitalize.count(nome) > 1:
                    if nome not in lista_final:
                        lista_final.append(nome)
    
        print(f"\nNomes que aparecerm mais de uma vez: {lista_final} !")

    def quest03():
        print("\n--->> Questão 03 <<---")

        def habilitacao(ano_nascimento):
            ano_atual = datetime.datetime.now().year

            if (ano_atual - ano_nascimento) >= 18:
                return "Autorizado: 18 anos ou mais"
            else:
                return "Negado: menos de 18 anos"
    
        ano_nascimento = int(input("Digite o ano de seu nascimento: "))
        print(habilitacao(ano_nascimento))

    os.system("cls")
    escolha = int(input("Escolha a questão (0 para sair): "))

    if escolha == 1:
        quest01()
    elif escolha == 2:
        quest02()
    elif escolha == 3:
        quest03()
    elif escolha == 0:
        print("--->> FIM <<---")
        return 1
    
    voltar = input("\nVoltar ao menu inicial (S/N)? " ).upper()

    if voltar == "S":
        return 0
    else:
        return 1


while True:
    sair = choose()

    if sair == 1:
        break