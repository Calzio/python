import os
import time 

def menu():
    print("== Opções ==")
    print("1 - Depósito")
    print("2 - Saldo Bancário")
    print("3 - Saque")
    print("4 - Pagamento de boleto")
    print("5 - Pix")
    print("6 - Transferência")
    print("0 - Finalizar consulta")
    
def depositar(dinheiro, valor_deposito):
    resultado = dinheiro + valor_deposito
    return resultado
    
def sacar(dinheiro, valor_saque):
    resultado = dinheiro - valor_saque
    return resultado
    
def boletos(dinheiro, valor_boleto):
    resultado = dinheiro - valor_boleto
    return resultado
    
def pagar_pix(dinheiro, valor_pix):
    resultado = dinheiro - valor_pix
    return resultado
    
def pagar_transferencia(dinheiro, valor_transferencia):
    resultado = dinheiro - valor_transferencia
    return resultado

def depositar_1(dinheiro, valor_deposito1):
    resultado = dinheiro + valor_deposito1
    return resultado
        
dinheiro = 3000

login = input("Já tem uma conta no nosso banco(s/n):")
if login == 's':
    menu()
    opcoes = int(input("Digite a opção desejada: "))
    if opcoes == 1:
        valor_deposito = float(input("Quanto deseja depositar: "))
        deposito = depositar(dinheiro, valor_deposito)
        print(f"O valor do deposito foi: {deposito}")
    elif opcoes == 2:
        saldo_bancario = dinheiro
        print(f"O saldo é: {saldo_bancario}")
    elif opcoes == 3:
        valor_saque = float(input("Quanto deseja sacar: "))
        saque = sacar(dinheiro, valor_saque)
        print(f"O valor sacado é: {saque}")
    elif opcoes == 4:
        tipo_boleto = input("Qual é o boleto que deseja pagar: ")
        valor_boleto = float(input("Valor do boleto: "))
        boleto = boletos(dinheiro, valor_boleto)
        print(f"O boleto a ser pago é: {tipo_boleto}")
        print(f"O valor do boleto é: {boleto}")
    elif opcoes == 5:
        cpf_pix = input("Digite o pix da pessoa: ")
        valor_pix = float(input("Valor do pix: "))
        pix = pagar_pix(dinheiro, valor_pix)
        print(f"O CPF é: {cpf_pix}")
        print(f"O valor do pix é: {pix}")
    elif opcoes == 6:
        valor_transferencia = float(input("Valor da transferência: "))
        transferencia = pagar_transferencia(dinheiro, valor_transferencia)
        print(f"Valor da transferência é: {transferencia}")
    elif opcoes == 0:
        os.system("cls||clear")
    
if login == 'n':
    dinheiro = 0
    os.system ("cls||clear")
    
    print("=== CRIANDO CONTA ===")
    conta = input("Conta empresarial ou pessoal?: ")
    
    if conta == "empresarial":
        cnpj = int(input("Digite o CNPJ: "))
        nomeEmpresa = input("Digite o nome da empresa: ")
        emailEmpresa = input("Digite o email da empresa: ")
    elif conta == "pessoal":
        cpf = int(input("Digite o CPF: "))
        nomeUsuario = input("Digite o seu nome: ")
        emailPessoal = input("Digite o seu email: ")
    else:
        print("*operação inválida*")
       
    time.sleep(2)
       
    os.system("cls||clear")
    print("=== MOSTRANDO RESULTADOS ===")
    if conta == "empresarial":
        print(f"CNPJ: {cnpj}")
        print(f"Nome da empresa: {nomeEmpresa}")
        print(f"Email empresarial: {emailEmpresa}")
    elif conta == "pessoal":
        print(f"CPF: {cpf}")
        print(f"Nome do usuário: {nomeUsuario}")
        print(f"Email do usuário: {emailPessoal}")
    
    input("\n*Pressione ENTER para continuar*")    
    os.system("cls||clear")
    
    valor_deposito1 = float(input("Para começarmos, digite o valor do primeiro depósito: "))
    primeiro_deposito = depositar_1(dinheiro, valor_deposito1)
    dinheiro = primeiro_deposito
    
    menu()
    opcoes = int(input("Digite a opção desejada: "))
    if opcoes == 1:
        valor_deposito = float(input("Quanto deseja depositar: "))
        deposito = depositar(dinheiro, valor_deposito)
        print(f"O valor do deposito foi: {deposito}")
    elif opcoes == 2:
        saldo_bancario = dinheiro
        print(f"O saldo é: {saldo_bancario}")
    elif opcoes == 3:
        valor_saque = float(input("Quanto deseja sacar: "))
        saque = sacar(dinheiro, valor_saque)
        print(f"O valor sacado é: {saque}")
    elif opcoes == 4:
        tipo_boleto = input("Qual é o boleto que deseja pagar: ")
        valor_boleto = float(input("Valor do boleto: "))
        boleto = boletos(dinheiro, valor_boleto)
        print(f"O boleto a ser pago é: {tipo_boleto}")
        print(f"O valor do boleto é: {boleto}")
    elif opcoes == 5:
        cpf_pix = input("Digite o pix da pessoa: ")
        valor_pix = float(input("Valor do pix: "))
        pix = pagar_pix(dinheiro, valor_pix)
        print(f"O CPF é: {cpf_pix}")
        print(f"O valor do pix é: {pix}")
    elif opcoes == 6:
        valor_transferencia = float(input("Valor da transferência: "))
        transferencia = pagar_transferencia(dinheiro, valor_transferencia)
        print(f"Valor da transferência é: {transferencia}")
    elif opcoes == 0:
        os.system("cls||clear")

