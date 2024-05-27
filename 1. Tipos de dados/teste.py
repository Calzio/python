def cabecalho():
    print("----- Menu -----")
    print("Cód |   Pratos     | valor(R$) |")
    print(" 01 | Batata frita |   11,00   |")
    print(" 02 |  Hambúrguer  |   19,00   |")
    print(" 03 |    X-tudo    |   22,00   |")
    print(" 04 |    Pastel    |   18,00   |")
    print(" 05 | Pizza pequena|   28,00   |")
    print(" 06 | Pizza média  |   32,00   |")
    print(" 07 | Pizza grande |   40,00   |")
    print("Digite 0 para finalizar o pedido.")

def iguaria(opcao):
    match opcao:
        case 1:
            return "Batata frita", 11.00
        case 2:
            return "Hambúrguer", 19.00
        case 3:
            return "X-tudo", 22.00
        case 4:
            return "Pastel", 18.00
        case 5:
            return "Pizza pequena", 28.00
        case 6:
            return "Pizza média", 32.00
        case 7:
            return "Pizza grande", 40.00
        case _:
            return None, 0.00

def calcular_valor_final(total, pagamento_avista):
    if pagamento_avista:
        desconto = total * 0.10
        total_com_desconto = total - desconto
        return total_com_desconto, desconto
    else:
        acrescimo = total * 0.10
        total_com_acrescimo = total + acrescimo
        return total_com_acrescimo, acrescimo

def main():
    total = 0
    pedidos = []

    while True:
        cabecalho()
        opcoes = int(input("Digite o código do prato desejado: "))
        
        if opcoes == 0:
            break

        nomePrato, precoPrato = iguaria(opcoes)
        
        if nomePrato:
            pedidos.append((opcoes, nomePrato, precoPrato))
            total += precoPrato
            print(f"Adicionado: {nomePrato} - R$ {precoPrato:.2f}")
        else:
            print("Código inválido.")

        adicionarOutroPrato = input("Deseja adicionar mais um prato? (s/n): ").lower()
        if adicionarOutroPrato != 's':
            break

    if total == 0:
        print("Nenhum pedido.")
        return

    print("\nResumo do Pedido:")
    for pedido in pedidos:
        opcoes, nomePrato, precoPrato = pedido
        print(f"Código: {opcoes} - {nomePrato} - R$ {precoPrato:.2f}")

    formaPagamento = input("Escolha a forma de pagamento (à vista/à prazo): ").lower()
    pagamentoAvista = (formaPagamento == 'à vista')

    valorFinal, desconto_ou_acrescimo = calcular_valor_final(total, pagamentoAvista)

    print(f"\nSubtotal: R$ {total:.2f}")
    if pagamentoAvista:
        print(f"Desconto: R$ {desconto_ou_acrescimo:.2f}")
    else:
        print(f"Acréscimo: R$ {desconto_ou_acrescimo:.2f}")
    print(f"Total a pagar: R$ {valorFinal:.2f}")

main()
