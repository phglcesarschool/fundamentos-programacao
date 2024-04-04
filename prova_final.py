import os

def choose():
    def quest01():
        print("\n--->> Questão 01 <<---")
        print("\n   *** MENU ***   ")
        print("   1 - Banho\n   2 - Tosa\n   3 - Banho e Tosa\n   4 - Outros\n")

        banho = tosa = banho_tosa = outros = 0

        for reps in range(10):
            servico = int(input(f"Qual o serviço para o {reps + 1}º cachorro? "))

            if servico == 1:
                banho += 1
            elif servico == 2:
                tosa += 1
            elif servico == 3:
                banho_tosa += 1
            elif servico == 4:
                outros += 1
            else:
                print("Valor inválido")
                exit(1)
        
        print("\n   *** Total dos serviços ***   \n")
        print(f"   Banho: {banho}\n   Tosa: {tosa}\n   Banho e Tosa: {banho_tosa}\n   Outros: {outros}")

    def quest02():
        print("\n--->> Questão 02 <<---")

        lista_geral = []
        lista_par = []
        lista_impar = []

        for reps in range(10):
            lista_geral.append(int(input(f"Informe um {reps + 1}º valor inteiro: ")))

        for reps in range(10):
            if (lista_geral[reps] % 2) == 0:
                lista_par.append(lista_geral[reps])
            else:
                lista_impar.append(lista_geral[reps])

        print(f"\nLista geral: {lista_geral}")
        print(f"Lista dos pares: {lista_par}")
        print(f"Lista dos ímpares: {lista_impar}")


    def quest03():
        print("\n--->> Questão 03 <<---")

        def minutos(horas):
            return horas * 60
        
        def segundos(horas):
           return horas * 3600

        try:
            horas = int(input("Informe o valor de horas: "))

            if horas <= 0:
                print("ERRO: Valor inválido")
            else:
                escolha = int(input("\nConverter para minutos (insira 1)\nConverter para segundos (insira 2)\n>> Insira a conversão desejada: "))

                if escolha == 1:
                    print(f"{minutos(horas)} minutos equivalem a {horas} horas")
                elif escolha == 2:
                    print(f"{segundos(horas)} segundos equivalem a {horas} horas")
                else:
                    print("ERRO: Valor inválido")
        except ValueError:
            print("ERRO: Valor inválido")
            exit(1)

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