"""
Descrição das variáveis:
  - quantidadePares: Quantidade de números pares.
  - quantidadeImpares: Quantidade de números ímpares.
  - quantidadePositivos: Quantidade de números positivos.
  - quantidadeNegativos: Quantidade de números negativos.
  - maiorNumero: O maior número.
  - menorNumero: O menor número.
  - mediapares: Média dos números pares.
  - mediaimpares: Média dos números ímpares.
  - mediageral: Média de todos os números.
  - numerosinvertidos: Os números na ordem inversa.
"""
# Variáveis para armazenar as estatísticas
numeros = []
quantidadePares = 0
quantidadeImpares = 0
quantidadePositivos = 0
quantidadeNegativos = 0
maiorNumero = 0
menorNumero = 0
somaPares = 0
somaImpares = 0
somaGeral = 0

# Variáveis para armazenar os números
maiorNumero = float('-inf')
menorNumero = float('inf')

for i in range (5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    somaGeral += numero
    
# Processando cada número
    if numero % 2 == 0:
        somaPares += numero
        quantidadePares += 1
    else:
        quantidadeImpares += 1
        somaImpares += numero
    
    if numero > 0:
        quantidadePositivos += 1
    elif numero < 0:
        quantidadeNegativos += 1
    
    if numero > maiorNumero:
        maiorNumero = numero
    if numero < menorNumero: 
        menorNumero = numero 

# Calculando as médias
mediapares = somaPares / quantidadePares if quantidadePares > 0 else 0
mediaimpares = somaImpares / quantidadeImpares if quantidadeImpares > 0 else 0
mediageral = somaGeral/numero

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidadePares}")
print(f"Quantidade de ímpares: {quantidadeImpares}")
print(f"Quantidade de positivos: {quantidadePositivos}")
print(f"Quantidade de negativos: {quantidadeNegativos}")
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")
print(f"Soma geral: {somaGeral}")
print(f"Média dos pares: {mediapares}")
print(f"Media dos ímpares: {mediaimpares:.2f}")

numeros.reverse()
print(f"Números lidos na ordem inversa: {numeros}") 




