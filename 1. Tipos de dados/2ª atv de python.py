import os
os.system("cls || clear")

print("Solicitano dados para o usuário.")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
media = soma / 2
produto = num1 * num2

if num1 > num2:
    maior = num1
else: 
    maior = num2

if num1 < num2 :
    menor = num1
else: 
    menor = num2

print("\nExibindo resultados.")
print(f"Primeiro número: {num1}")
print(f"Segundo número: {num2}")

print(f"\nSoma: {soma}")
print(f"Produto: {produto}")
print(f"Média: {media}")
print(f"Maior Número: {maior}")
print(f"Menor número: {menor}") 
