tabuleiro = []

def zerando_tabuleiro():
    
    #Limpa o tabuleiro para um novo jogo
    
    global tabuleiro
    tabuleiro.clear()
    
    for linhas in range(3):
        linha = []
        for colunas in range(3):
            linha.append("-")
        tabuleiro.append(linhas)

            
def menu():
    #Exibe as opções do programa
    
    titulo("jogo da velha")
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

def nomes():
    #Faz a leitura dos nomes dos jogadores
    jogador1 = input("Insira o nome do primeiro jogador: ")
    jogador2 = input("Insira o nome do segundo jogador: ")
    return [jogador1, jogador2]

def titulo(sessao):
    #Faz um padrão de título
    tamanho = len(sessao)
    qtd_tracos = 50
    qtd_espacos = (qtd_tracos - tamanho) // 2
    sessao = sessao.upper()
    
    print("-" * qtd_tracos)
    print(" " * qtd_espacos, sessao)
    print("-" * qtd_tracos)
    print()
    
def novo_jogo():
    zerando_tabuleiro()
    titulo("novo jogo")

    
    

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

main()