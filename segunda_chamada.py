import os

def choose():
    def quest01():
        print("\n--->> Questão 01 <<---")

        valores_ph = []
        valor = 0

        while True:
            valor = int(input("Insira o valor do pH: "))

            if valor == -1:
                break
            else:
                valores_ph.append(valor)
        
        for reps in range(len(valores_ph)):
            if valores_ph[reps] < 7:
                print(f"pH da solução {reps + 1} ({valores_ph[reps]}): ÁCIDO")
            elif valores_ph[reps] > 7:
                print(f"pH da solução {reps + 1} ({valores_ph[reps]}): BÁSICO")
            else:
                print(f"pH da solução {reps + 1} ({valores_ph[reps]}): NEUTRO")

    def quest02():
        print("\n--->> Questão 02 <<---")

        nome_atleta = input("Informe o seu nome: ")
        soma_saltos = 0
        saltos = []

        for reps in range(5):
            valor_salto = float(input(f"Digite o valor do {reps + 1}º salto: "))
            saltos.append(valor_salto)
            soma_saltos += valor_salto

        print("        *** Resultado ***        ")
        print(f"Atleta: {nome_atleta}")

        for reps in range(5):
            print(f"{reps + 1}º salto: {saltos[reps]:.2f}")

        print(f"Média dos saltos: {(soma_saltos / 5):.2f}")

    def quest03():
        print("\n--->> Questão 03 <<---")

        nome_time1 = input("Digite o nome do time 1: ")

        try:    
            gols_time1 = int(input("Quantos gols foram marcados pelo time 1? "))            
        except ValueError:
            print(f"Valor de gols inválido!")
            exit(1)

        nome_time2 = input("Digite o nome do time 2: ")

        try:    
            gols_time2 = int(input("Quantos gols foram marcados pelo time 2? "))
        except ValueError:
            print(f"Valor de gols inválido!")
            exit(1)
        
        if gols_time1 > gols_time2:
            print(f"Vencedor: {nome_time1}")
        elif gols_time2 > gols_time1:
            print(f"Vencedor: {nome_time2}")
        else:
            print(f"Empate")

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