import os
os.system ("cls || clear")

def cabecalho():
    os.system("cls || clear")
    print("----------------")
    print("==Senai | Fieb==")
    print("----------------")

def somar(n1,n2):
    resultado = n1 + n2
    return resultado

cabecalho()
num1 = int(input(f"Digite o primeiro número: "))
num2 = int(input(f"Digite o segundo número: "))

soma = somar(num1,num2)

cabecalho()
print(f"Soma: {soma}")