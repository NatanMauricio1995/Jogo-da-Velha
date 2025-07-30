tabuleiro = []

def zerando_tabuleiro():
    
    #Limpa o tabuleiro para um novo jogo
    
    global tabuleiro
    
    for linha in range(3):
        for coluna in range(3):
            tabuleiro[linha][coluna] = "-"