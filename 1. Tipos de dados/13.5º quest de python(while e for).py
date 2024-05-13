import os
os.system("cls||clear")

soma = 0

for i in range (1,3) :
    while True:
        nota = float(input("Digite uma nota: "))
        if nota < 0 or nota > 10:
            print("Nota inválida... \n")
        else: 
            soma+=nota
            break

media = soma / 2

print(f"Média: {media}")