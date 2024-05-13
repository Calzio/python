opcao = int(input("Escolha uma opcao: "))

if opcao == 1:
    print("Opção 1")
elif opcao == 2:
    print("Opção 2")
elif opcao == 3:
    print("Opção 3")
elif opcao == 4:
    print("Opção 4")
else:
    print("Opção 5")

match(opcao):
    case 1:
        print("Opção 1")
    case 2:
        print("Opção 2")
    case 3:
        print("Opção 3")
    case 4:
        print("Opção 4")

