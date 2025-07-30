tabuleiro = []

jogadores = {}

def zerando_tabuleiro():
    # Limpa o tabuleiro para um novo jogo
    global tabuleiro
    tabuleiro.clear()
    
    for linhas in range(3):
        linha = []
        for colunas in range(3):
            linha.append("-")
        tabuleiro.append(linha)

def menu():
    # Exibe as opções do programa
    titulo("jogo da velha")
    print("Opções:")
    print("  1 - Novo jogo")
    print("  2 - Placar")
    print("  3 - Sair")

def definindo_escolha():
    # Faz leitura da escolha do usuário no menu principal
    escolha = 0
    while (escolha < 1) or (escolha > 3):
        try:
            escolha = int(input("Insira a opção desejada: "))
            if((escolha < 1) or (escolha > 3)):
                print("Insira um valor numérico válido!\n")
        except ValueError:
            print("Insira um valor numérico válido!\n")
    print()
    print("-" * 40)
    print()
    return escolha

def nomes():
    # Faz a leitura dos nomes dos jogadores
    global jogadores
    
    nome1 = input("Insira o nome do primeiro jogador: ")
    nome2 = input("Insira o nome do segundo jogador: ")
    
    peca1, peca2 = escolha_marcador(nome1)
    
    jogadores = {
        "jogador1": {
            "nome": nome1,
            "peca": peca1
        },
        "jogador2": {
            "nome": nome2,
            "peca": peca2
        }
    }

def titulo(sessao):
    # Faz um padrão de título
    tamanho = len(sessao)
    qtd_tracos = 50
    qtd_espacos = (qtd_tracos - tamanho) // 2
    sessao = sessao.upper()
    
    print("-" * qtd_tracos)
    print(" " * qtd_espacos + sessao)
    print("-" * qtd_tracos)
    print()

def escolha_marcador(jogador1):
    # O jogador 1 escolhe qual peça irá usar
    print(f"{jogador1}, escolha seu marcador:")
    print("  1 - ❌")
    print("  2 - ⭕")
    
    escolha = 0
    while (escolha < 1) or (escolha > 2):
        try:
            escolha = int(input("Insira a opção desejada: "))
            if((escolha < 1) or (escolha > 2)):
                print("Insira um valor numérico válido!\n")
        except ValueError:
            print("Insira um valor numérico válido!\n")
    
    if escolha == 1:
        peca1 = "❌"
        peca2 = "⭕"
    else:
        peca1 = "⭕"
        peca2 = "❌"
        
    return peca1, peca2

def novo_jogo():
    zerando_tabuleiro()
    titulo("novo jogo")
    nomes()
    jogo()

def placar():
    # Função placeholder para evitar erro
    print("Placar ainda não implementado.\n")

def main():
    escolha = 0
    while (escolha != 3):
        menu()
        escolha = definindo_escolha()
        
        if(escolha == 1):
            novo_jogo()
        elif(escolha == 2):
            placar()
        elif(escolha == 3):
            print("Muito Obrigado por jogar! Até mais!")
            
def teste_linha(tabuleiro):
    #Verifica se o jogo terminou e qual peça ganhadora em linha
    for linha in range(3):         
        if((tabuleiro[linha][0] == "❌") and (tabuleiro[linha][1] == "❌") and (tabuleiro[linha][2] == "❌")):
            status = "❌"
            
        elif((tabuleiro[linha][0] == "⭕") and (tabuleiro[linha][1] == "⭕") and (tabuleiro[linha][2] == "⭕")):
            status = "⭕"
            
        else:
            status = 0
            
    return status

def teste_coluna(tabuleiro):
    #Verifica se o jogo terminou e qual peça ganhadora em coluna
    for coluna in range(3):
        if((tabuleiro[0][coluna] == "❌") and (tabuleiro[1][coluna] == "❌") and (tabuleiro[2][coluna] == "❌")):
            status = "❌"
            
        elif((tabuleiro[0][coluna] == "⭕") and (tabuleiro[1][coluna] == "⭕") and (tabuleiro[2][coluna] == "⭕")):
            status = "⭕"
            
        else:
            status = 0
            
    return status
                
def teste_diagonal_principal(tabuleiro):
    #Verifica se o jogo terminou e qual peça ganhadora na diagonal principal
    if((tabuleiro[0][0] == "❌") and (tabuleiro[1][1] == "❌") and (tabuleiro[2][2] == "❌")):
        status = "❌"
            
    elif((tabuleiro[0][0] == "⭕") and (tabuleiro[1][1] == "⭕") and (tabuleiro[2][2] == "⭕")):
        status = "⭕"
    
    else:
        status = 0

    return status
     
def teste_diagonal_secundária(tabuleiro):
    #Verifica se o jogo terminou e qual peça ganhadora na diagonal secundária
    if((tabuleiro[0][2] == "❌") and (tabuleiro[1][1] == "❌") and (tabuleiro[2][0] == "❌")):
        status = "❌"
            
    elif((tabuleiro[0][2] == "⭕") and (tabuleiro[1][1] == "⭕") and (tabuleiro[2][0] == "⭕")):
        status = "⭕"
    
    else:
        status = 0
    
    return status
     
     
def jogo():
    global jogadores
    global tabuleiro
    

    
    
    
    
    
    

main()
