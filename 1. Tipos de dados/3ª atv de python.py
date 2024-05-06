import os
os.system("cls || clear")

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))

media = (nota1 + nota2) / 2
soma = nota1 + nota2
produto = nota1 * nota2

if nota1 > nota2:
    maior = nota1
else: 
    maior = nota2

if nota1 < nota2 :
    menor = nota1
else: 
    menor = nota2

print(f"\nSoma: {soma}")
print(f"Produto: {produto}")
print(f"Média: {media}")

if nota1 == nota2 :
    print("Os números são iguais.")

else: 
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")

