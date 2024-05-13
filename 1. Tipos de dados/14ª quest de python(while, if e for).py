import os
os.system("cls||clear")

soma = 0

for i in range (1,4) :
    while True:
        nota = float(input("Digite uma nota: "))
        if nota < 0 or nota > 10:
            print("Nota inválida... \n")
        else: 
            soma+=nota
            break

media = soma / 3

print(f"Média: {media}")

if media >= 7:
    print("Passado")
elif media > 5 and media < 6.9:
    print("Recuperação")
else:
    print("Reprovado")