tabuleiro = []

def zerando_tabuleiro():
    
    #Limpa o tabuleiro para um novo jogo
    
    global tabuleiro
    
    for linha in range(3):
        for coluna in range(3):
            tabuleiro[linha][coluna] = "-"
            
def menu():
    #Exibe as opções do programa
    
    print("-" * 40)
    print(" " * 13,"JOGO DA VELHA")
    print("-" * 40)
    print()
    print("Opções:")
    print("  1 - Novo jogo")
    print("  2 - Placar")
    print("  3 - Sair")
    
def definindo_escolha():
    #Faz leitura da escolha do usuário no menu principal
    
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

