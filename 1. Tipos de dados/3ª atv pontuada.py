import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def calcular_imc(peso, altura):
    resultado = peso / (altura * altura)
    return resultado
    
# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
imc = 0

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

    imc = calcular_imc(peso, altura)

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"\nUsuário {i+1}:")
    print("Nome:", nomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    imc = calcular_imc(pesos[i], alturas[i])
    print(f"IMC: {imc:.3f}")
    if imc < 18.5:
        print("Abaixo do peso.")
    elif 18.5 <= imc < 25:
        print("Peso normal.")
    elif 25 <= imc < 30:
        print("Sobrepeso.")
    elif 30 <= imc < 35:
        print("Obesidade grau I.")
    elif 35 <= imc < 40:
        print("Obesidade grau II.")
    elif imc >= 40:
        print("Obesidade grau III (mórbida).")


