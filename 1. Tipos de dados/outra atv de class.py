import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pet:
    nome: str
    idade: int
    raca: str
    porte: str
    alimentacao: str

pets = []

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
raca = input("Digite a raça: ")
porte = input("Digite o porte: ")
alimentacao = input("Digite a dieta do seu pet: ")
pet = Pet(nome = nome, idade = idade, raca = raca, porte = porte, alimentacao = alimentacao)
pets.append(pet)

for dados_pet in pets:
    print(f"Nome: {dados_pet.nome}")
    print(f"Idade: {dados_pet.idade}")
    print(f"Raça: {dados_pet.raca}")
    print(f"Porte: {dados_pet.porte}")
    print(f"Alimentação: {dados_pet.alimentacao}")