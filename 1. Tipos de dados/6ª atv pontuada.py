import os

#Funções 
def mostrarResultado ():
    os.system("cls || clear")
    print(f"Média: {media}")
    print(f"Situação: {situacao}")
    print(notas)

#Sum usado para facilitar a soma de uma sequência de uma lista que no caso é 'notas'
def soma_notas(notas):
    soma = sum(notas)
    return soma

def media_final(soma):
    resultado = soma / tam
    return resultado
    
def verificar_situacao(media):
    resultado = "Aprovado!" if media >= 7 else "Reprovado!"
    return resultado

#Declarando constantes lícidas
tam:int=3
soma = 0
notas=[]
media=[]

os.system("cls || clear")

#Solicitando a nota usando for
for i in range(tam):
	nota = float(input("Digite suas notas: "))
	notas.append(nota)

#Declarando determinadas funções	
soma = soma_notas(notas)
media = media_final(soma) 
situacao = verificar_situacao(media)

#Final
mostrarResultado()

