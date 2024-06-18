# Inicialização do sistema bancário
saldo = 0.0
depositos = []
saques = []
saques_diarios = 0

while True:
    print("Sistema Bancário")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            depositos.append(f"Depósito de R$ {valor:.2f}")
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {
                  saldo:.2f}")
        else:
            print("Valor de depósito inválido. Por favor, tente novamente.")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        if saques_diarios < 3 and valor <= 500.0 and valor <= saldo:
            saldo -= valor
            saques.append(f"Saque de R$ {valor:.2f}")
            saques_diarios += 1
            print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        elif saques_diarios >= 3:
            print("Você já realizou 3 saques diários. Por favor, tente novamente amanhã.")
        elif valor > saldo:
            print("Saldo insuficiente. Por favor, tente novamente.")
        else:
            print("Valor de saque inválido. Por favor, tente novamente.")

    elif opcao == "3":
        if not depositos and not saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato da conta:")
            for movimento in depositos + saques:
                print(movimento)
            print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Sistema finalizado.")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")
