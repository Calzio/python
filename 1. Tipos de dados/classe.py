import os
from dataclasses import dataclass

os.system("cls || clear")

QUANTIDADE_ALUNOS = 3

@dataclass
class Aluno:
    nome: str
    idade: str

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    aluno = Aluno(nome = nome, idade = idade)
    alunos.append(aluno)

for dados_aluno in alunos:
    print(f"Nome: {dados_aluno.nome}")
    print(f"Idade: {dados_aluno.idade}")

print("Salvando dados em um arquivo.")

nome_arquivo = "cadastro_de_aluno.txt"

with open(nome_arquivo, "w") as arquivo:
    for dados_alunos in alunos:
        arquivo.write(f"{dados_aluno}.nome,{dados_aluno.idade}\n")

print("Dados salvos com sucesso.")

input("\nLendo dados em um arquivo.")
lista_alunos = []
#Lendo dados do arquivo
with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo:
        nome, idade = linha.strip().split(",")
        lista_alunos.append(Aluno(nome = nome, idade = int(idade)))

for aluno in lista_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")