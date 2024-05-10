def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    # Aqui você pode adicionar mais informações do usuário, se desejar
    return {"nome": nome, "cpf": cpf}

def criar_conta():
    usuario = criar_usuario()
    saldo = float(input("Informe o saldo inicial da conta: "))
    limite = float(input("Informe o limite da conta: "))
    return {"usuario": usuario, "saldo": saldo, "limite": limite, "extrato": "", "numero_saques": 0}

def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        return True
    else:
        print("Operação falhou! O valor informado é inválido.")
        return False

def sacar(conta):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > conta["limite"]
    excedeu_saques = conta["numero_saques"] >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return False
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return False
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return False
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1
        return True
    else:
        print("Operação falhou! O valor informado é inválido.")
        return False

def extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

def menu():
    return """
    [c] Criar Conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

LIMITE_SAQUES = 3

def main():
    contas = []
    while True:
        opcao = input(menu())
        if opcao == "c":
            conta = criar_conta()
            contas.append(conta)
            print("Conta criada com sucesso!")
        elif opcao == "d":
            conta_index = int(input("Digite o número da conta: "))
            if conta_index < len(contas):
                depositar(contas[conta_index])
            else:
                print("Conta não encontrada.")
        elif opcao == "s":
            conta_index = int(input("Digite o número da conta: "))
            if conta_index < len(contas):
                sacar(contas[conta_index])
            else:
                print("Conta não encontrada.")
        elif opcao == "e":
            conta_index = int(input("Digite o número da conta: "))
            if conta_index < len(contas):
                extrato(contas[conta_index])
            else:
                print("Conta não encontrada.")
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
