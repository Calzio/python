import os
os.system("cls||clear")

nota1: float = -1
nota2: float = -1

while (nota1 < 0 or nota1 > 10):
    nota1 = float(input("Digite a primeira nota: "))

while (nota2 < 0 or nota2 > 10):
    nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"Média: {media}")