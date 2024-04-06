# Faça um programa que leia e valide as seguintes informações. Ao final, imprima as informações:
#    
# a)  Nome: maior que 3 caracteres;
# b)  Idade: entre 18 e 90;
# c)  Salário: maior que zero;
# d)  Sexo: 'F' ou 'M';
# e)  Estado Civil: 'S', 'C', 'U', 'V', 'D';
#         
# Use a função len(string) para saber o tamanho de um texto (número de caracteres).
import os
import platform

if (platform.system() == "Linux") or (platform.system() == "Darwin"):
    os.system("clear")
elif platform.system() == "Windows":
    os.system("cls")

nome = input("Digite um nome: ")

while len(nome) <= 3:
    print("ATENÇÃO: Nome muito curto, digite ao menos 3 caracteres!")
    nome = input("Digite um nome maior: ")

idade = int(input("Digite uma idade: "))

while 18 > idade or idade > 90:
    print("ATENÇÃO: A idade deve estar entre 18 e 90 anos!")
    idade = int(input("Digite uma idade dentro do intervalo: "))

salario = float(input("Digite um salário: "))

while salario <= 0:
    print("ATENÇÃO: O salário dever ser maior que zero (senão é trabalho análogo à escravidão)!")
    salario = float(input("Digite uma salário maior que zero: "))

sexo = input("Digite o sexo biológico [(F)eminino | (M)asculino]: ")

while sexo.upper() != "F" and sexo.upper() != "M":
    print("ATENÇÃO: Insira apenas o primeiro caractere do  sexo BIOLÓGICO (F/M)!")
    sexo = input("Digite o sexo [(F)eminino | (M)asculino]: ")

estado_civil = input("Digite o estado civil [(S)olteiro | (C)asado | (U)nião estável | (V)iúvo | (D)ivorciado]: ")

while estado_civil.upper() != 'S' and estado_civil.upper() != 'C' and estado_civil.upper() != 'U' and estado_civil.upper() != 'V' and estado_civil.upper() != 'D':
    print("ATENÇÃO: Insira apenas o primeiro caractere (S/C/U/V/D)!")
    sexo = input("Digite o estado civil [(S)olteiro | (C)asado | (U)nião estável | (V)iúvo | (D)ivorciado]: ")

print("\nInformações sobre o funcionário: ")
print(f" Nome: {nome}\n Idade: {idade} anos\n Salário: R${salario:.2f}")

if sexo.upper() == "F":
    print(" Sexo: Feminino")
elif sexo.upper() == "M":
    print(" Sexo: Masculino")

if estado_civil.upper() == "S":
    print(" Estado civil: Solteiro")
elif estado_civil.upper() == "C":
    print(" Estado civil: Casado")
elif estado_civil.upper() == "U":
    print(" Estado civil: União estável")
elif estado_civil.upper() == "V":
    print(" Estado civil: Viúvo")
elif estado_civil.upper() == "D":
    print(" Estado civil: Divorciado")
