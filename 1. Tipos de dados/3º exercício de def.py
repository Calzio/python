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

def multiplicacao(n1,n2):
    resultado = n1 * n2
    return resultado

def subtracao(n1,n2):
    resultado = n1 - n2
    return resultado

def divisao(n1,n2):
    resultado = n1 / n2
    return resultado

cabecalho()
num1 = int(input(f"Digite o primeiro número: "))
num2 = int(input(f"Digite o segundo número: "))

soma = somar(num1,num2)
multip = multiplicacao(num1,num2)
subt = subtracao(num1,num2)
div = divisao(num1,num2)

cabecalho()
print(f"Soma: {soma}")
print(f"Multiplicação: {multip}")
print(f"Subtração: {subt}")
print(f"Divisão: {div}")