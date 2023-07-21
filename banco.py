import os

def LimparTela():
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)


def ExcecaoNumero():
    msg_ex = """
        Apenas números e ponto flutuante.
        Ex1.: 100
        Ex2.: 999.99
        """
    print(msg_ex)


def MenuPrincipal(usuario: dict):
    menu = f"""
    Olá, {usuario["nome_usuario"]}!                saldo: {usuario["saldo"]}
    O que deseja fazer?

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    LimparTela()
    print(menu, end="")


def Saldo(usuario: dict):
    menu = f"""

    Saldo atual: R${usuario["saldo"]}

    """
    print(menu)


def Extrato(usuario: dict):
    LimparTela()
    if len(usuario["extrato"]) > 0:
        for mov in usuario["extrato"]:
            print(mov)
    else:
        print("Não há movimentações nesta conta.\n")

    input(MSG_CONTINUAR)


def MenuDeposito(usuario: dict):
    try:
        menu = f"Informe o valor para depósito em R$ (apenas números): "

        LimparTela()
        valor_deposito = float(input(menu))

        usuario["saldo"] += valor_deposito
        usuario["extrato"].append(f"{valor_deposito} C")

        print("Depósito efetuado com sucesso!")
    except:
        ExcecaoNumero()

    input(MSG_CONTINUAR)


def MenuSaque(usuario: dict):
    try:
        if usuario["numero_saques"] < 3:
            menu = "Informe valor para saque em R$ (apenas números): "

            LimparTela()
            Saldo(usuario)
            valor_saque = float(input(menu))

            if valor_saque > usuario["saldo"]:
                print("Saldo insuficiente.\n")
            else:
                usuario["saldo"] -= valor_saque
                usuario["extrato"].append(f"{valor_saque} D")
                usuario["numero_saques"] += 1
                print("Saque efetuado com sucesso!")
        else:
            print("Limite de saque diário atingido.")
    except:
        ExcecaoNumero()

    input(MSG_CONTINUAR)


NUMERO_LIMITE_SAQUES_DIA = 3
MSG_CONTINUAR = "Tecle [Enter] para continuar..."

usuario = {
    "nome_usuario": "",
    "saldo": 0,
    "limite_saque_diario": 500,
    "numero_saques": 0,
    "extrato": []
}

print("Por favor, identifique-se com um nome:")
nome_usuario = input()

usuario["nome_usuario"] = nome_usuario

while True:
    MenuPrincipal(usuario)

    opcao = input().lower()

    if opcao == "d":
        MenuDeposito(usuario)
    if opcao == "s":
        MenuSaque(usuario)
    if opcao == "e":
        Extrato(usuario)
    if opcao == "q":
        break
