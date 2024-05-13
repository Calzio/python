import os
os.system("cls || clear")

nome = input("Digite o nome: ")
sexo = input("Digite o seu sexo(F ou M): ")
estadoCivil = input("Digite seu estado civil: ")

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if  sexo == "f" or estadoCivil == "casada" and sexo == "F" or estadoCivil == "Casada":
    tempoCasada = int(input("Tempo casada(em anos): "))
    print("Acabou.")

print(f"Nome: {nome.capitalize()}")

if sexo == "f":
    print(f"Sexo: Feminino")
else:
        print(f"Sexo: Masculino")

print(f"Estado civil: {estadoCivil.capitalize()}")
if sexo == "f" and estadoCivil == "casada":
     print(f"Tempo de casada: {tempoCasada}")