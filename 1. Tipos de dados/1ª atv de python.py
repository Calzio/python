import os
os.system("cls || clear")

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))

media = (nota1 + nota2) / 2

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {nota1}")
print(f"Segunda nota: {nota2}")
print(f"Média: {media}")

if media >= 7 :
    print("Aprovado")
else :
    print("Reprovado")