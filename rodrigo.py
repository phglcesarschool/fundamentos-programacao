import os

def choose():
    def quest01():
        print("\n--->> Questão 01 <<---")
    
    def quest02():
        print("\n--->> Questão 02 <<---")
    
    def quest03():
        print("\n--->> Questão 03 <<---")

        def filtrar_numeros(lista, limite_inferior, limite_superior):
            return [numero for numero in lista if limite_inferior <= numero <= limite_superior]

        def filtrar_numeros_simples(lista, limite_inferior, limite_superior):
            novos_numeros = []

            for numero in lista:
                if limite_inferior <= numero <= limite_superior:
                    novos_numeros.append(numero)
    
            return numero

        numeros = []

        for i in range(10):
            numero = int(input(f"Digite o {i+1}º número inteiro: "))
            numeros.append(numero)

        limite_inferior = int(input("Digite o limite inferior: "))
        limite_superior = int(input("Digite o limite inferior: "))

        resultado = filtrar_numeros(numeros, limite_inferior, limite_superior)
        print(f"Lista filtrada: {resultado}")

        resultado_simples = filtrar_numeros_simples(numeros, limite_inferior, limite_superior)
        print(f"Lista filtrada simples: {resultado_simples}")
    
    def quest04():
        print("\n--->> Questão 04 <<---")

        def imprimir_lista(numero):
            lista = []

            for i in range(numero):
                lista.append(int(i + 1))

            return print(*lista)

        while True:
            numero = int(input("Digite um número: "))

            if numero == 0:
                break
            else:
                imprimir_lista(numero)
    
    def quest05():
        print("\n--->> Questão 05 <<---")

        def minutos(horas):
            return horas * 60
        
        def segundos(horas):
           return horas * 3600

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

    os.system("cls")
    escolha = int(input("Escolha a questão (0 para sair): "))

    if escolha == 1:
        quest01()
    elif escolha == 2:
        quest02()
    elif escolha == 3:
        quest03()
    elif escolha == 4:
        quest04()
    elif escolha == 5:
        quest05()
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