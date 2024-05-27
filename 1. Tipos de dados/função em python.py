menu = {
    print(f"Prato\t\t\t\t|\tPreço(R$)\t|\tNúmero do item\n")
    print(f"Batata frita |\t\t10,00\t\t|\t\t\t\t\t1\t\t\t\t\n")
    print(f"Hambúrguer   |\t\t19,00\t\t|\t\t\t\t\t2\t\t\t\t\n")
    print(f"X-tudo       |\t\t22,00\t\t|\t\t\t\t\t3\t\t\t\t\n")
    print(f"Pastel       |\t\t15,00\t\t|\t\t\t\t\t4\t\t\t\t\n")
    print(f"Pizza pequena|\t\t28,00\t\t|\t\t\t\t\t5\t\t\t\t\n")
    print(f"Pizza média  |\t\t32,00\t\t|\t\t\t\t\t6\t\t\t\t\n")
    print(f"Pizza grande |\t\t40,00\t\t|\t\t\t\t\t7\t\t\t\t\n")
    print(f"Digite 0 para encerrar o pedido")
}

total = 0
pedido + []

def mostrar_menu():
    print(f"\t\t\tMenu\n")
    for key, value in menu.itens():
        print(f"{key}: {value[0]} * {value[1]} - RS{value[2]}")
        
def calcular_subtotal(pedido):
    subtotal = 0
    for prato in pedido:
        subtotal += menu[prato][2]
    return subtotal

def calcular_pagamento(subtotal, forma_pagamento):
    if forma_pagamento
        desconto = subtotal * 0.10
     
while TRUE:
    op = int(input("Digite o número desejado: "))
    
    if op == 0:
        break
    
    if