# 🎮 Jogo da Velha (Tic-Tac-Toe)

Um jogo da velha completo e interativo desenvolvido em Python, com sistema de placar e interface amigável no terminal.

## 📋 Descrição

Este projeto implementa o clássico jogo da velha para dois jogadores, com um sistema completo que inclui:
- Tabuleiro 3x3 interativo
- Sistema de turnos alternados
- Detecção automática de vitórias e empates
- Placar acumulativo de partidas
- Interface visual organizada no terminal

## ✨ Funcionalidades

- **Jogo completo**: Sistema de turnos com validação de jogadas
- **Personalização**: Jogadores escolhem nomes e marcadores (❌ ou ⭕)
- **Detecção inteligente**: Verifica vitórias em linhas, colunas e diagonais
- **Placar persistente**: Mantém registro de vitórias e empates durante a sessão
- **Interface amigável**: Tabuleiro visual com coordenadas numeradas
- **Validação robusta**: Impede jogadas inválidas e entradas incorretas
- **Menu interativo**: Navegação fácil entre jogos e visualização do placar

## 🚀 Como executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/jogo-da-velha.git
   cd jogo-da-velha
   ```

2. **Execute o jogo:**
   ```bash
   python jogo_velha.py
   ```

3. **Siga as instruções do menu:**
   - Digite `1` para iniciar um novo jogo
   - Digite `2` para ver o placar atual
   - Digite `3` para sair

## 🎯 Como jogar

### Iniciando um novo jogo
1. Escolha a opção "Novo jogo" no menu
2. Digite os nomes dos dois jogadores
3. O primeiro jogador escolhe seu marcador (❌ ou ⭕)
4. Os jogadores alternam turnos até que alguém vença ou dê empate

### Fazendo uma jogada
1. Quando for sua vez, digite o número da **linha** (0, 1 ou 2)
2. Digite o número da **coluna** (0, 1 ou 2)
3. Sua peça será colocada na posição escolhida
4. O tabuleiro será atualizado automaticamente

### Condições de vitória
- **Vitória**: Três marcadores iguais em linha, coluna ou diagonal
- **Empate**: Tabuleiro completamente preenchido sem vencedor

## 🔧 Requisitos

- **Python 3.6+**
- Nenhuma biblioteca externa necessária

## 📊 Estrutura do Projeto

```
jogo-da-velha/
│
├── jogo_velha.py      # Código principal do jogo
├── README.md          # Este arquivo
└── .gitignore         # Arquivos ignorados pelo Git
```

## 🎨 Interface

O jogo apresenta:
- **Menu principal** com opções numeradas e título formatado
- **Tabuleiro visual** com coordenadas para facilitar as jogadas:
  ```
      0   1   2
    -----------
  0 | - | - | - |
    -----------
  1 | - | ❌ | - |
    -----------
  2 | ⭕ | - | - |
    -----------
  ```
- **Placar acumulativo** mostrando vitórias de cada jogador e empates
- **Mensagens de feedback** com emojis para melhor experiência

## 🛠️ Principais recursos técnicos

Este projeto demonstra:

- **Estruturas de dados**: Uso de matrizes (listas bidimensionais) para o tabuleiro
- **Algoritmos de verificação**: Lógica para detectar vitórias em todas as direções
- **Validação de entrada**: Tratamento robusto de erros de input do usuário
- **Organização de código**: Funções bem estruturadas e documentadas
- **Controle de fluxo**: Loops e condicionais para gerenciar o estado do jogo
- **Variáveis globais**: Uso adequado para manter estado entre funções
- **Interface de usuário**: Sistema de menus e feedback visual

## 🎯 Conceitos de programação demonstrados

- Matrizes e manipulação de dados bidimensionais
- Algoritmos de busca em padrões (linhas, colunas, diagonais)
- Validação e sanitização de entrada do usuário
- Estruturação de código em funções especializadas
- Gerenciamento de estado global do programa
- Lógica de jogos e sistemas de turnos
- Tratamento de exceções com try/except

## 🤝 Como contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Possíveis melhorias futuras

- [ ] Modo contra computador (IA)
- [ ] Diferentes tamanhos de tabuleiro (4x4, 5x5)
- [ ] Interface gráfica com Tkinter
- [ ] Salvamento de placar em arquivo
- [ ] Sistema de ranking de jogadores
- [ ] Modo online para dois jogadores remotos
- [ ] Diferentes níveis de dificuldade da IA

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido como projeto educacional, demonstrando competências em:
- Lógica de programação avançada
- Estruturas de dados complexas
- Desenvolvimento de jogos simples
- Interface de linha de comando
- Organização e documentação de código

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
