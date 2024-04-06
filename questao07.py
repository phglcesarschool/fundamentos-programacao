# Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, o mês e o ano para 3 variáveis inteiras.
# Antes disso, verifique se as barras estão no lugar certo e se “DD”, “MM” e “AAAA” são numéricos.
import os
import platform

if (platform.system() == "Linux") or (platform.system() == "Darwin"):
    os.system("clear")
elif platform.system() == "Windows":
    os.system("cls")

data = input("Informe uma data (DD/MM/AAAA): ")

while data[2] != "/" and data[5] != "/":
    print("ATENÇÃO: Informe uma data no formato DD/MM/AAAA")
    data = input("Informe uma outra data (DD/MM/AAAA): ")

if data[0:2].isnumeric():
    dia = data[0:2]
else:
    print("ATENÇÃO: O dia deve ser apenas numéricos")
    exit(1)

if data[3:5].isnumeric():
    mes = data[3:5]
else:
    print("ATENÇÃO: O mês deve ser apenas numéricos")
    exit(1)

if data[6:10].isnumeric():
    ano = data[6:10]

else:
    print("ATENÇÃO: O ano deve ser apenas numéricos")
    exit(1)

print(f"Dia {dia}")
print(f"Mês {mes}")
print(f"Ano {ano}")
