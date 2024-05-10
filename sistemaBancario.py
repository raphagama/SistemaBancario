menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor para inserção na conta: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depositado: R$ {valor:.2f}\n"

        else:
            print("Fom! Operação não deu certoi, o valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Fom! Não deu certo pois você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Fom! Não deu certo pois o valor do saque excede o limite.")

        elif excedeu_saques:
            print("Fom! Não deu certo pois o número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Fom! Não deu certo pois o valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Sem movimentações até o momento." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Fom! Não deu certo, por favor selecione novamente a operação desejada.")