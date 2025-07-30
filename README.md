# Jogo da Velha (Tic-Tac-Toe)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

Sistema completo de Jogo da Velha desenvolvido em Python com interface em linha de comando, oferecendo experiência interativa para dois jogadores com sistema de placar integrado.

## Descrição do Projeto

Este projeto foi desenvolvido como parte dos estudos em **estruturas de dados** e **lógica de programação** em Python. O sistema implementa o clássico jogo da velha com funcionalidades avançadas de validação, controle de turnos e registro de estatísticas.

### Problema Resolvido
- **Cenário:** Necessidade de entretenimento digital simples para dois jogadores
- **Solução:** Interface intuitiva com validações robustas e sistema de pontuação
- **Resultado:** Jogo funcional com experiência de usuário otimizada

## Funcionalidades

- **Jogo para Dois Jogadores:** Sistema completo de turnos alternados
- **Escolha de Marcadores:** Jogadores podem escolher entre X e O
- **Sistema de Placar:** Registro de vitórias, derrotas e empates
- **Validação Robusta:** Tratamento de entradas inválidas e posições ocupadas
- **Interface Visual:** Tabuleiro organizado com coordenadas claras
- **Detecção Automática:** Identificação de vitórias (linhas, colunas, diagonais) e empates
- **Menu Interativo:** Navegação simples entre partidas e visualização de estatísticas

## Tecnologias

- **Python 3.x**
- **Estruturas de Dados:** Matrizes (listas bidimensionais)
- **Programação Procedural**
- **Tratamento de Exceções**
- **Manipulação de Strings**

## Como Executar

### Pré-requisitos
- Python 3.6 ou superior instalado

### Passos
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/jogo-da-velha-python.git
   cd jogo-da-velha-python
   ```

2. **Execute o programa:**
   ```bash
   python jogo_da_velha.py
   ```

3. **Interaja com o menu:**
   - Digite `1` para iniciar novo jogo
   - Digite `2` para ver placar atual
   - Digite `3` para sair do programa

## Preview do Sistema

```
--------------------------------------------------
                  JOGO DA VELHA
--------------------------------------------------

Opções:
  1 - Novo jogo
  2 - Ver placar  
  3 - Sair

    0   1   2
  -----------
0 | X | O | - |
  -----------
1 | X | X | O |
  -----------
2 | O | X | X |
  -----------

JOGADOR VENCEU com X!
```

## Estrutura do Código

### Arquivos Principais
- **`jogo_da_velha.py`** - Sistema completo do jogo

### Principais Funções
```python
def zerando_tabuleiro()           # Inicializa matriz 3x3
def definir_nomes_jogadores()     # Configuração dos participantes  
def mostrar_tabuleiro()           # Renderização visual do estado atual
def obter_jogada()                # Captura e validação de movimentos
def verificar_status_jogo()       # Análise de condições de vitória/empate
def executar_jogo()               # Loop principal do jogo
def exibir_placar()               # Visualização de estatísticas
```

## Conceitos Aplicados

### Estruturas de Dados
- **Matrizes (Listas 2D):** Representação do tabuleiro como matriz 3x3
- **Dicionários:** Armazenamento de informações dos jogadores e placar
- **Manipulação de Índices:** Validação de coordenadas (0-2)

### Programação Procedural
- **Modularização:** Divisão em funções específicas
- **Separação de Responsabilidades:** Cada função tem propósito claro
- **Controle de Fluxo:** Loops e condicionais para lógica do jogo

### Tratamento de Erros
- **Try/Except:** Captura de entradas inválidas
- **Validação de Range:** Verificação de limites das coordenadas
- **Prevenção de Conflitos:** Impedimento de jogadas em posições ocupadas

### Experiência do Usuário
- **Interface Organizada:** Menus formatados e títulos centralizados
- **Feedback Claro:** Mensagens informativas sobre operações
- **Validação Amigável:** Orientações específicas para correção de erros

## Evolução do Projeto

| Funcionalidade | Status |
|----------------|--------|
| **Lógica Básica** | Implementada |
| **Sistema de Placar** | Implementada |
| **Validações Robustas** | Implementada |
| **Interface Melhorada** | Implementada |

### Próximas Melhorias Planejadas
- [ ] Modo contra IA com diferentes níveis de dificuldade
- [ ] Interface gráfica com Tkinter
- [ ] Persistência de dados (salvar placar em arquivo)
- [ ] Diferentes tamanhos de tabuleiro (4x4, 5x5)
- [ ] Modo online multiplayer
- [ ] Temas visuais personalizáveis

## Aprendizados

Este projeto consolidou conhecimentos em:
- **Estruturas de dados bidimensionais**
- **Algoritmos de verificação de padrões**
- **Validação robusta de entrada do usuário**
- **Design de interface de usuário em terminal**
- **Gestão de estado global em aplicações**
- **Organização e documentação de código**

## Especificações Técnicas

- **Tabuleiro:** Matriz 3x3 (9 posições)
- **Jogadores:** Sistema para 2 players simultâneos
- **Marcadores:** X e O (escolha do primeiro jogador)
- **Condições de Vitória:** 3 em linha (horizontal, vertical, diagonal)
- **Sistema de Pontuação:** Contador de vitórias e empates
- **Compatibilidade:** Multiplataforma (Windows, Linux, macOS)

## Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Contato

**[Seu Nome]**
- Email: seu.email@exemplo.com
- LinkedIn: [linkedin.com/in/seu-perfil](https://linkedin.com/in/seu-perfil)
- GitHub: [github.com/seu-usuario](https://github.com/seu-usuario)

---

Se este projeto te ajudou, deixe uma estrela!

*Desenvolvido durante os estudos de Programação em Python*
