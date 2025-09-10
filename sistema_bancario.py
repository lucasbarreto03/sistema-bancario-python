# ==============================
# Sistema Bancário - Versão Melhorada
# Autor: Lucas Eduardo Barreto de Oliveira
# ==============================

MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Configurações
LIMITE = 500
LIMITE_SAQUES = 3


# ------------------------------
# Funções
# ------------------------------
def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("❌ Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(saldo, extrato, valor, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("❌ Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("❌ Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("❌ Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("❌ Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    print("📄 Extrato exibido com sucesso!")


# ------------------------------
# Programa Principal
# ------------------------------
def main():
    saldo = 0
    extrato = ""
    numero_saques = 0

    while True:
        opcao = input(MENU)

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
            except ValueError:
                print("❌ Entrada inválida. Digite um número.")
                continue
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
            except ValueError:
                print("❌ Entrada inválida. Digite um número.")
                continue
            saldo, extrato, numero_saques = sacar(
                saldo, extrato, valor, LIMITE, numero_saques, LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("👋 Saindo do sistema bancário. Obrigado por utilizar nossos serviços!")
            break

        else:
            print("❌ Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
