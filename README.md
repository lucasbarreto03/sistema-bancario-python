# 🏦 Sistema Bancário em Python

Projeto prático desenvolvido como exercício do Bootcamp da **DIO** (Suzano - Python Developer #2) e adaptado/aperfeiçoado por **Lucas Eduardo Barreto de Oliveira**.

Esse repositório contém uma versão do *Sistema Bancário* com:
- código orientado a objetos (POO);
- classes modeladas para representar usuários, contas e transações;
- métodos encapsulados para depósito, saque e extrato;
- validação de entrada (tratamento de `ValueError`);
- mensagens claras após cada ação (confirmando depósito/saque/extrato);
- limite por saque e limite diário de saques configuráveis;
- limite de 10 transações diárias;
- registro de data e hora em todas as transações.

---

## ▶️ Funcionalidades
- **Depositar valores**
- **Sacar valores** (com verificação de saldo, limite por saque e limite diário de saques)
- **Exibir extrato** (histórico de movimentações)
- **Criar usuário** (cliente do banco)
- **Criar conta corrente** (vinculando-a a um usuário existente)
- Controle de até **10 transações diárias** (depósitos + saques)
- Registro de **data e hora** no extrato
- Mensagens informativas após cada operação

---

## 🛠️ Requisitos
- Python 3.8+ (recomendado 3.10)
- Não há dependências externas (somente stdlib).

---

## 📊 Diagrama UML

📊 Diagrama UML

```mermaid
classDiagram
    class Usuario {
        - nome: str
        - cpf: str
        - data_nascimento: str
        - endereco: str
        + criar_conta(): Conta
    }

    class Conta {
        - numero: int
        - agencia: str
        - saldo: float
        - usuario: Usuario
        + depositar(valor: float)
        + sacar(valor: float)
        + exibir_extrato()
    }

    class Transacao {
        - valor: float
        - data_hora: datetime
        - tipo: str
    }

    Usuario "1" --> "0..*" Conta : possui
    Conta "1" --> "0..*" Transacao : registra

```


### 🔧 O que eu modifiquei / adicionei
Este projeto não é apenas uma cópia — é uma evolução do desafio da DIO. As principais melhorias implementadas foram:

* **Estrutura modular em funções** (depositar, sacar, exibir_extrato, criar_usuario, criar_conta_corrente);
* **Implementação das novas funções `criar_usuario` e `criar_conta_corrente`** com suas respectivas regras de negócio;
* **Regras de passagem de argumentos** (`positional only` e `keyword only`) aplicadas nas funções de saque, depósito e extrato;
* **Validação robusta de entrada** (tratamento com `try/except` para evitar que entradas inválidas quebrem o programa);
* **Mensagens de confirmação** ao final de cada ação (ex.: ✅ Depósito de R$ 100.00 realizado com sucesso!);
* **Controle de até 10 transações diárias**;
* **Registro de data e hora** em cada transação do extrato;
* **Organização do código** para facilitar futuras melhorias (POO, múltiplas contas, persistência de dados).

---

### 🤝 Créditos
Este projeto foi inspirado no desafio **"Criando um Sistema Bancário com Python"** da Digital Innovation One (DIO).

O código aqui apresentado foi adaptado e aprimorado por **Lucas Eduardo Barreto de Oliveira**, com melhorias em:

* **Estrutura modular** (funções);
* **Novas funcionalidades** de criação de usuários e contas;
* **Mensagens claras de feedback** ao usuário;
* **Validações adicionais** de entrada e limites;
* **Novas funcionalidades** de limite diário de transações e registro de data/hora.


