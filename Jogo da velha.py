tabuleiro = []
jogadores = {}
placares = {"jogador1": 0, "jogador2": 0, "empate": 0}

def zerando_tabuleiro():
    global tabuleiro
    tabuleiro.clear()
    for linhas in range(3):
        linha = []
        for colunas in range(3):
            linha.append("-")
        tabuleiro.append(linha)

def menu():
    titulo("jogo da velha")
    print("Opções:")
    print("  1 - Novo jogo")
    print("  2 - Placar")
    print("  3 - Sair")

def definindo_escolha():
    escolha = 0
    while (escolha < 1) or (escolha > 3):
        try:
            escolha = int(input("Insira a opção desejada: "))
            if ((escolha < 1) or (escolha > 3)):
                print("Insira um valor numérico válido!\n")
        except ValueError:
            print("Insira um valor numérico válido!\n")
    print()
    print("-" * 40)
    print()
    return escolha

def nomes():
    global jogadores
    nome1 = input("Insira o nome do primeiro jogador: ")
    nome2 = input("Insira o nome do segundo jogador: ")
    peca1, peca2 = escolha_marcador(nome1)
    jogadores = {
        "jogador1": {"nome": nome1, "peca": peca1},
        "jogador2": {"nome": nome2, "peca": peca2}
    }

def titulo(sessao):
    tamanho = len(sessao)
    qtd_tracos = 50
    qtd_espacos = (qtd_tracos - tamanho) // 2
    sessao = sessao.upper()
    print("-" * qtd_tracos)
    print(" " * qtd_espacos + sessao)
    print("-" * qtd_tracos)
    print()

def escolha_marcador(jogador1):
    print(f"{jogador1}, escolha seu marcador:")
    print("  1 - ❌")
    print("  2 - ⭕")
    escolha = 0
    while (escolha < 1) or (escolha > 2):
        try:
            escolha = int(input("Insira a opção desejada: "))
            if ((escolha < 1) or (escolha > 2)):
                print("Insira um valor numérico válido!\n")
        except ValueError:
            print("Insira um valor numérico válido!\n")
    if escolha == 1:
        return "❌", "⭕"
    else:
        return "⭕", "❌"

def mostrar_tabuleiro():
    print("\n  0   1   2")
    for i in range(3):
        linha = " | ".join(tabuleiro[i])
        print(f"{i} {linha}")
        if i < 2:
            print("  ---------")
    print()

def novo_jogo():
    zerando_tabuleiro()
    titulo("novo jogo")
    nomes()
    mostrar_tabuleiro()
    jogo()

def placar():
    print()
    titulo("placar")
    print(f'{jogadores.get("jogador1", {}).get("nome", "Jogador 1")}: {placares["jogador1"]} vitória(s)')
    print(f'{jogadores.get("jogador2", {}).get("nome", "Jogador 2")}: {placares["jogador2"]} vitória(s)')
    print(f'Empates: {placares["empate"]}\n')

def teste_linha(tabuleiro):
    for linha in range(3):         
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] != "-":
            return tabuleiro[linha][0]
    return 0

def teste_coluna(tabuleiro):
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != "-":
            return tabuleiro[0][coluna]
    return 0

def teste_diagonal_principal(tabuleiro):
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "-":
        return tabuleiro[0][0]
    return 0

def teste_diagonal_secundária(tabuleiro):
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "-":
        return tabuleiro[0][2]
    return 0

def teste_ganhador():
    global tabuleiro
    for teste in [teste_coluna, teste_linha, teste_diagonal_principal, teste_diagonal_secundária]:
        resultado = teste(tabuleiro)
        if resultado != 0:
            return resultado
    if sum(linha.count("-") for linha in tabuleiro) == 0:
        return -1
    return 0

def jogo():
    global jogadores
    global tabuleiro
    global placares

    turno = 0
    while True:
        status = teste_ganhador()
        if status == -1:
            print("Empate! O tabuleiro está cheio.\n")
            placares["empate"] += 1
            break
        elif status in ["❌", "⭕"]:
            for j in jogadores:
                if jogadores[j]["peca"] == status:
                    print(f'{jogadores[j]["nome"]} venceu com {status}!\n')
                    placares[j] += 1
            break

        jogador_atual = "jogador1" if turno % 2 == 0 else "jogador2"
        nome = jogadores[jogador_atual]["nome"]
        peca = jogadores[jogador_atual]["peca"]

        x = y = -1
        while (x < 0) or (x > 2):
            try:
                x = int(input(f"{nome}, selecione a LINHA (0-2): "))
                if (x < 0) or (x > 2):
                    print("Insira um valor numérico válido!\n")
            except ValueError:
                print("Insira um valor numérico válido!\n")

        while (y < 0) or (y > 2):
            try:
                y = int(input(f"{nome}, selecione a COLUNA (0-2): "))
                if (y < 0) or (y > 2):
                    print("Insira um valor numérico válido!\n")
            except ValueError:
                print("Insira um valor numérico válido!\n")

        if tabuleiro[x][y] == "-":
            tabuleiro[x][y] = peca
            mostrar_tabuleiro()
            turno += 1
        else:
            print("Essa posição já está ocupada. Tente novamente.")

def main():
    escolha = 0
    while escolha != 3:
        menu()
        escolha = definindo_escolha()
        if escolha == 1:
            novo_jogo()
        elif escolha == 2:
            placar()
        elif escolha == 3:
            print("Muito Obrigado por jogar! Até mais!")

main()
