# ==============================
# Sistema Bancário - Versão 2.0
# ==============================

from datetime import datetime
import textwrap

MENU = """\n
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nu]\tNovo usuário
[nc]\tNova conta
[lc]\tListar contas
[q]\tSair
=> """

# Variáveis globais para o sistema
LIMITE = 500
LIMITE_SAQUES = 3
AGENCIA = "0001"
LIMITE_TRANSACOES_DIARIAS = 10


# --- Funções de Ajuda ---
def log_transacao(transacoes, tipo, valor, data=None):
    """Adiciona uma transação ao histórico com data e hora."""
    if data is None:
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    transacoes.append({"tipo": tipo, "valor": valor, "data": data})

def formatar_cpf(cpf):
    """Remove caracteres especiais de uma string de CPF."""
    return "".join(filter(str.isdigit, cpf))


# --- Funções de Operações Bancárias (refatoradas) ---
def depositar(saldo, valor, /, *, extrato):
    """
    Recebe os argumentos por POSIÇÃO (positional only) e NOME.
    Realiza um depósito se o valor for válido.
    """
    if valor > 0:
        saldo += valor
        log_transacao(extrato, "Depósito", valor)
        print("\n✅ Depósito realizado com sucesso!")
    else:
        print("\n❌ Falha na operação! O valor informado é inválido.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Recebe os argumentos por NOME (keyword only).
    Realiza um saque com base nas regras do sistema.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n❌ Falha na operação! Saldo insuficiente.")
    elif excedeu_limite:
        print("\n❌ Falha na operação! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("\n❌ Falha na operação! Limite de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        log_transacao(extrato, "Saque", valor)
        print("\n✅ Saque realizado com sucesso!")
        return saldo, numero_saques, extrato
    else:
        print("\n❌ Falha na operação! O valor informado é inválido.")
        return saldo, numero_saques, extrato


def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.
    Recebe saldo por posição e extrato por nome.
    """
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in extrato:
            tipo = transacao['tipo']
            valor = transacao['valor']
            data = transacao['data']
            print(f"{tipo.ljust(10)}:\tR$ {valor:.2f}\t\t({data})")

    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


# --- Funções de Usuário e Conta ---
def buscar_usuario(cpf, usuarios):
    """Busca um usuário na lista por CPF."""
    cpf_formatado = formatar_cpf(cpf)
    for usuario in usuarios:
        if usuario["cpf"] == cpf_formatado:
            return usuario
    return None


def criar_usuario(usuarios):
    """
    Cria um novo usuário, com validação de CPF.
    Armazena o usuário em uma lista de dicionários.
    """
    cpf = input("Informe o CPF (somente números): ")
    if buscar_usuario(cpf, usuarios):
        print("\n❌ Erro! Já existe um usuário com este CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": formatar_cpf(cpf),
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    print("\n✅ Usuário cadastrado com sucesso!")


def criar_conta_corrente(agencia, numero_conta, usuarios, contas):
    """Cria uma nova conta e a vincula a um usuário existente."""
    cpf = input("Informe o CPF do titular da conta: ")
    usuario = buscar_usuario(cpf, usuarios)

    if not usuario:
        print("\n❌ Erro! Usuário não encontrado, crie o usuário primeiro.")
        return None

    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(nova_conta)
    print("\n✅ Conta corrente criada com sucesso!")
    return nova_conta


def listar_contas(contas):
    """Exibe todas as contas e seus titulares."""
    print("\n============== LISTA DE CONTAS ==============")
    if not contas:
        print("\nNão há contas cadastradas.")
    else:
        for conta in contas:
            usuario = conta['usuario']
            print(textwrap.dedent(f"""\
                Agência:\t{conta['agencia']}
                Conta:\t\t{conta['numero_conta']}
                Titular:\t{usuario['nome']}
                CPF:\t\t{usuario['cpf']}
            """))
    print("============================================")


# --- Programa Principal ---
def main():
    """Função principal do sistema bancário."""
    # Listas para armazenar dados do sistema
    usuarios = []
    contas = []
    numero_conta = 1

    # Variáveis de sessão
    saldo = 0
    extrato = []
    numero_saques = 0

    while True:
        if len(extrato) >= LIMITE_TRANSACOES_DIARIAS:
            print("⚠️ Limite diário de 10 transações atingido! Tente novamente amanhã.")
            break

        opcao = input(MENU).strip().lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
            except ValueError:
                print("\n❌ Entrada inválida. Digite um número.")
                continue
            saldo, extrato = depositar(saldo, valor, extrato=extrato)

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
            except ValueError:
                print("\n❌ Entrada inválida. Digite um número.")
                continue
            saldo, numero_saques, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            criar_conta_corrente(AGENCIA, numero_conta, usuarios, contas)
            if contas:
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nSaindo do sistema. Obrigado por usar nosso serviço!")
            break

        else:
            print("\n❌ Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()


