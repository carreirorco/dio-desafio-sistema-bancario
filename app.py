menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
            print("Você depositou R$ {:.2f}".format(valor))
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print("Você escolheu a opção de saque.")
        pass

    elif opcao == "e":
        print("Você escolheu a opção de extrato.")
        pass

    elif opcao == "q":
        print("Você escolheu a opção de sair.")
        pass
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        print("Encerrando o programa...")