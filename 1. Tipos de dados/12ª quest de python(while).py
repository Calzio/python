import os
os.system("cls || clear")

nota = float(input("Digite uma nota: "))

while nota < 0 and nota > 10 :

    nota = float(input("Digite uma nota: "))

print(f"Nota informada: {nota}")

print("Fim")