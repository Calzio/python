import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Cliente:
    nome: str
    idade: int
    cpf: int
    endereco: str
    telefone: float

@dataclass
class Veiculo:
    placa: str
    cor: str
    numero_passageiros: int
    capacidade_tanque: int
    velocidade_max: int
    consumo_medio: float

clientes = []
veiculos = []

print(f"=== Cliente ===")
nome = input("\nDigite seu nome: ")
idade = int(input("Digite sua idade: "))
cpf = int(input("Digite seu cpf(sem pontuações): "))
endereco = input("Digite seu endereço: ")
telefone = float(input("Digite o seu telefone: "))

print(f"\n=== Veículo ===")
placa = input("\nDigite a placa: ")
cor = input("Digite a cor do seu veículo: ")
numero_passageiros = int(input("Digite o número de passageiros suportados: "))
capacidade_tanque = int(input("Digite a capacidade que o tanque do seu veículo suporta(em Litros): "))
velocidade_max = int(input("Digite a velocidade máxima(em Km): "))
consumo_medio = float(input("Digite o consumo médio do veículo(em Litros): "))

cliente = Cliente(nome = nome, idade = idade, cpf = cpf, endereco = endereco, telefone = telefone)
veiculo = Veiculo(placa = placa, cor = cor, numero_passageiros = numero_passageiros, capacidade_tanque = capacidade_tanque, velocidade_max = velocidade_max, consumo_medio = consumo_medio)

clientes.append(cliente)
veiculos.append(veiculo)


for dados in cliente:
    print(f"Nome: {dados.nome}")
    print(f"Idade: {dados.idade}")
    print(f"CPF: {dados.cpf}")
    print(f"Endereço: {dados.endereco}")
    print(f"Telefone: {dados.telefone}")

for dados in veiculo:
    print(f"Placa: {dados.placa}")
    print(f"Cor: {dados.cor}")
    print(f"Numeros de passageiros: {dados.numero_passageiros}")
    print(f"Capacidade do tanque: {dados.capacidade_tanque}")
    print(f"Velocidade máxima: {dados.velocidade_max}")