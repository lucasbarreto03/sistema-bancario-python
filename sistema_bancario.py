# ==============================
# Sistema Bancário - Versão Melhorada com Data e Hora
# Autor: Lucas Eduardo Barreto de Oliveira
# ==============================

from datetime import datetime

MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Configurações
LIMITE = 500
LIMITE_SAQUES = 3
LIMITE_TRANSACOES_DIARIAS = 10


# ------------------------------
# Funções
# ------------------------------
def registrar_transacao(transacoes, tipo, valor):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    transacoes.append(f"{tipo}: R$ {valor:.2f} | {agora}")


def depositar(saldo, transacoes, valor):
    if valor > 0:
        saldo += valor
        registrar_transacao(transacoes, "Depósito", valor)
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("❌ Operação falhou! O valor informado é inválido.")
    return saldo


def sacar(saldo, transacoes, valor, limite, numero_saques, limite_saques):
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
        numero_saques += 1
        registrar_transacao(transacoes, "Saque", valor)
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("❌ Operação falhou! O valor informado é inválido.")

    return saldo, numero_saques


def exibir_extrato(saldo, transacoes):
    print("\n================ EXTRATO ================")
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for t in transacoes:
            print(t)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    print("📄 Extrato exibido com sucesso!")


# ------------------------------
# Programa Principal
# ------------------------------
def main():
    saldo = 0
    transacoes = []
    numero_saques = 0

    while True:
        if len(transacoes) >= LIMITE_TRANSACOES_DIARIAS:
            print("⚠️ Limite diário de 10 transações atingido! Tente novamente amanhã.")
            break

        opcao = input(MENU)

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
            except ValueError:
                print("❌ Entrada inválida. Digite um número.")
                continue
            saldo = depositar(saldo, transacoes, valor)

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
            except ValueError:
                print("❌ Entrada inválida. Digite um número.")
                continue
            saldo, numero_saques = sacar(
                saldo, transacoes, valor, LIMITE, numero_saques, LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, transacoes)

        elif opcao == "q":
            print("👋 Saindo do sistema bancário. Obrigado por utilizar nossos serviços!")
            break

        else:
            print("❌ Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()


