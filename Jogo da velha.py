"""
Jogo da Velha (Tic-Tac-Toe)
Sistema completo com dois jogadores, placar e interface amigável.
Demonstra uso de matrizes, validação de entrada e lógica de jogos.
"""

# Variáveis globais para estado do jogo
tabuleiro = []
jogadores = {}
placares = {"jogador1": 0, "jogador2": 0, "empate": 0}

def zerando_tabuleiro():
    """
    Inicializa o tabuleiro 3x3 com posições vazias.
    Limpa o tabuleiro atual e cria uma nova matriz.
    """
    global tabuleiro
    tabuleiro.clear()
    
    for linha in range(3):
        linha_tabuleiro = []
        for coluna in range(3):
            linha_tabuleiro.append("-")
        tabuleiro.append(linha_tabuleiro)

def titulo(sessao):
    """
    Exibe um título formatado e centralizado.
    
    Args:
        sessao (str): Texto do título a ser exibido
    """
    tamanho = len(sessao)
    qtd_tracos = 50
    qtd_espacos = (qtd_tracos - tamanho) // 2
    sessao = sessao.upper()
    
    print("-" * qtd_tracos)
    print(" " * qtd_espacos + sessao)
    print("-" * qtd_tracos)
    print()

def menu():
    """Exibe o menu principal do jogo."""
    titulo("jogo da velha")
    print("Opções:")
    print("  1 - Novo jogo")
    print("  2 - Ver placar")
    print("  3 - Sair")
    print()

def definindo_escolha():
    """
    Obtém e valida a escolha do usuário no menu principal.
    
    Returns:
        int: Opção escolhida pelo usuário (1-3)
    """
    escolha = 0
    
    while (escolha < 1) or (escolha > 3):
        try:
            escolha = int(input("Insira a opção desejada: "))
            if (escolha < 1) or (escolha > 3):
                print("❌ Insira um valor entre 1 e 3!\n")
        except ValueError:
            print("❌ Insira apenas números!\n")
    
    print()
    print("-" * 40)
    print()
    return escolha

def escolha_marcador(nome_jogador):
    """
    Permite ao primeiro jogador escolher seu marcador (❌ ou ⭕).
    
    Args:
        nome_jogador (str): Nome do jogador que vai escolher
        
    Returns:
        tuple: (marcador_jogador1, marcador_jogador2)
    """
    print(f"{nome_jogador}, escolha seu marcador:")
    print("  1 - ❌ (X)")
    print("  2 - ⭕ (O)")
    
    escolha = 0
    while (escolha < 1) or (escolha > 2):
        try:
            escolha = int(input("Insira a opção desejada: "))
            if (escolha < 1) or (escolha > 2):
                print("❌ Escolha 1 ou 2!\n")
        except ValueError:
            print("❌ Insira apenas números!\n")
    
    if escolha == 1:
        return "❌", "⭕"
    else:
        return "⭕", "❌"

def definir_nomes_jogadores():
    """
    Obtém os nomes dos jogadores e define seus marcadores.
    Atualiza o dicionário global 'jogadores'.
    """
    global jogadores
    
    print("--- CONFIGURAÇÃO DOS JOGADORES ---")
    nome1 = input("Nome do primeiro jogador: ").strip()
    nome2 = input("Nome do segundo jogador: ").strip()
    
    # Garantir que os nomes não sejam vazios
    if not nome1:
        nome1 = "Jogador 1"
    if not nome2:
        nome2 = "Jogador 2"
    
    print()
    peca1, peca2 = escolha_marcador(nome1)
    
    jogadores = {
        "jogador1": {"nome": nome1, "peca": peca1},
        "jogador2": {"nome": nome2, "peca": peca2}
    }
    print()

def mostrar_tabuleiro():
    """
    Exibe o tabuleiro atual de forma organizada.
    Mostra coordenadas para facilitar a jogada.
    """
    print("\n    0   1   2")
    print("  -----------")
    
    for linha in range(3):
        linha_formatada = " | ".join(tabuleiro[linha])
        print(f"{linha} | {linha_formatada} |")
        if linha < 2:
            print("  -----------")
    
    print("  -----------")
    print()

def obter_jogada(nome_jogador):
    """
    Obtém e valida as coordenadas da jogada do jogador.
    
    Args:
        nome_jogador (str): Nome do jogador atual
        
    Returns:
        tuple: (linha, coluna) escolhidas pelo jogador
    """
    print(f"--- VEZ DE {nome_jogador.upper()} ---")
    
    # Obter linha
    linha = -1
    while (linha < 0) or (linha > 2):
        try:
            linha = int(input(f"{nome_jogador}, escolha a LINHA (0-2): "))
            if (linha < 0) or (linha > 2):
                print("❌ Linha deve ser 0, 1 ou 2!")
        except ValueError:
            print("❌ Insira apenas números!")
    
    # Obter coluna
    coluna = -1
    while (coluna < 0) or (coluna > 2):
        try:
            coluna = int(input(f"{nome_jogador}, escolha a COLUNA (0-2): "))
            if (coluna < 0) or (coluna > 2):
                print("❌ Coluna deve ser 0, 1 ou 2!")
        except ValueError:
            print("❌ Insira apenas números!")
    
    return linha, coluna

def verificar_linha():
    """
    Verifica se há três marcadores iguais em alguma linha.
    
    Returns:
        str or int: Marcador vencedor ou 0 se não houver vencedor
    """
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] != "-":
            return tabuleiro[linha][0]
    return 0

def verificar_coluna():
    """
    Verifica se há três marcadores iguais em alguma coluna.
    
    Returns:
        str or int: Marcador vencedor ou 0 se não houver vencedor
    """
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != "-":
            return tabuleiro[0][coluna]
    return 0

def verificar_diagonal_principal():
    """
    Verifica se há três marcadores iguais na diagonal principal.
    
    Returns:
        str or int: Marcador vencedor ou 0 se não houver vencedor
    """
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "-":
        return tabuleiro[0][0]
    return 0

def verificar_diagonal_secundaria():
    """
    Verifica se há três marcadores iguais na diagonal secundária.
    
    Returns:
        str or int: Marcador vencedor ou 0 se não houver vencedor
    """
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "-":
        return tabuleiro[0][2]
    return 0

def verificar_status_jogo():
    """
    Verifica o status atual do jogo (vitória, empate ou continua).
    
    Returns:
        str or int: Marcador vencedor, -1 para empate, ou 0 para continuar
    """
    # Lista de funções de verificação
    verificacoes = [
        verificar_linha, 
        verificar_coluna, 
        verificar_diagonal_principal, 
        verificar_diagonal_secundaria
    ]
    
    # Verifica todas as condições de vitória
    for verificacao in verificacoes:
        resultado = verificacao()
        if resultado != 0:
            return resultado
    
    # Verifica empate (tabuleiro cheio)
    espacos_vazios = sum(linha.count("-") for linha in tabuleiro)
    if espacos_vazios == 0:
        return -1
    
    # Jogo continua
    return 0

def executar_jogo():
    """
    Loop principal do jogo que gerencia as jogadas e verifica vitórias.
    """
    turno = 0
    
    while True:
        # Verifica status do jogo
        status = verificar_status_jogo()
        
        if status == -1:
            print("🤝 EMPATE! O tabuleiro está completamente preenchido.")
            placares["empate"] += 1
            break
            
        elif status in ["❌", "⭕"]:
            # Encontra o vencedor
            for chave_jogador in jogadores:
                if jogadores[chave_jogador]["peca"] == status:
                    nome_vencedor = jogadores[chave_jogador]["nome"]
                    print(f"🎉 {nome_vencedor.upper()} VENCEU com {status}!")
                    placares[chave_jogador] += 1
                    break
            break
        
        # Determina jogador atual
        jogador_atual = "jogador1" if turno % 2 == 0 else "jogador2"
        nome_atual = jogadores[jogador_atual]["nome"]
        peca_atual = jogadores[jogador_atual]["peca"]
        
        # Obter jogada
        linha, coluna = obter_jogada(nome_atual)
        
        # Verificar se posição está livre
        if tabuleiro[linha][coluna] == "-":
            tabuleiro[linha][coluna] = peca_atual
            mostrar_tabuleiro()
            turno += 1
        else:
            print("❌ Essa posição já está ocupada! Tente novamente.\n")

def novo_jogo():
    """Inicia um novo jogo completo."""
    zerando_tabuleiro()
    titulo("novo jogo")
    definir_nomes_jogadores()
    
    print("🎮 Vamos começar!")
    mostrar_tabuleiro()
    executar_jogo()

def exibir_placar():
    """Exibe o placar atual dos jogadores."""
    print()
    titulo("placar atual")
    
    # Obter nomes dos jogadores ou usar padrão
    nome1 = jogadores.get("jogador1", {}).get("nome", "Jogador 1")
    nome2 = jogadores.get("jogador2", {}).get("nome", "Jogador 2")
    
    print(f"🏆 {nome1}: {placares['jogador1']} vitória(s)")
    print(f"🏆 {nome2}: {placares['jogador2']} vitória(s)")
    print(f"🤝 Empates: {placares['empate']}")
    print()

def main():
    """Função principal que gerencia o menu e fluxo do programa."""
    print("🎮 Bem-vindo ao Jogo da Velha! 🎮\n")
    
    escolha = 0
    while escolha != 3:
        menu()
        escolha = definindo_escolha()
        
        if escolha == 1:
            novo_jogo()
            
        elif escolha == 2:
            exibir_placar()
            
        elif escolha == 3:
            print("🎮 Obrigado por jogar!")
            print("Até a próxima! 👋")
        
        # Pausa para visualizar resultado
        if escolha != 3:
            input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    main()