"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                 COMO CRIAR UM JOGO DA VELHA - AULA COMPLETA              ║
║                         Aprendizado Passo a Passo                        ║
╚═══════════════════════════════════════════════════════════════════════════╝

ÍNDICE:
1. O QUE VOCÊ PRECISA SABER
2. ESTRUTURA DO CÓDIGO
3. COMPONENTES PRINCIPAIS
4. COMO TUDO FUNCIONA JUNTO
"""

# ============================================================================
# 1. O QUE VOCÊ PRECISA SABER
# ============================================================================

"""
Um jogo da velha tem 3 partes principais:

1️⃣  DADOS (O Tabuleiro)
    - Uma matriz 3x3 (um grid 3 linhas × 3 colunas)
    - Cada posição pode ter: vazio " ", X ou O

2️⃣  FUNÇÕES (As Ações)
    - Mostrar o tabuleiro
    - Verificar vitória
    - Fazer movimentos
    - Trocar de jogador

3️⃣  LÓGICA (O Fluxo)
    - O jogo rodar em um loop (enquanto não terminar)
    - Jogador faz movimento
    - Verifica se venceu
    - Passa a vez pro próximo

VAMOS CONSTRUIR TUDO ISSO:
"""

# ============================================================================
# 2. PASSO 1: CRIAR O TABULEIRO (A ESTRUTURA DOS DADOS)
# ============================================================================

print("╔════════════════════════════════════════════════════════════╗")
print("║ PASSO 1: Criando o Tabuleiro                             ║")
print("╚════════════════════════════════════════════════════════════╝\n")

# Um tabuleiro é uma lista dentro de outra lista (matriz 2D)
tabuleiro = [
    [" ", " ", " "],  # Linha 0 (posições 1, 2, 3)
    [" ", " ", " "],  # Linha 1 (posições 4, 5, 6)
    [" ", " ", " "]   # Linha 2 (posições 7, 8, 9)
]

print("Tabuleiro vazio:")
print(f"{tabuleiro}\n")

# Como acessar cada posição:
print("Como acessar as posições:")
print(f"Posição [0][0] (canto superior esquerdo): {tabuleiro[0][0]}")
print(f"Posição [1][1] (centro): {tabuleiro[1][1]}")
print(f"Posição [2][2] (canto inferior direito): {tabuleiro[2][2]}\n")

# Como colocar X ou O:
tabuleiro[0][0] = "X"  # Coloca X no canto superior esquerdo
tabuleiro[1][1] = "O"  # Coloca O no centro

print("Tabuleiro após colocar X no [0][0] e O no [1][1]:")
print(f"{tabuleiro}\n")


# ============================================================================
# PASSO 2: CONVERTER POSIÇÃO (1-9) PARA COORDENADAS (linha, coluna)
# ============================================================================

print("╔════════════════════════════════════════════════════════════╗")
print("║ PASSO 2: Converter Posição (1-9) para Coordenadas         ║")
print("╚════════════════════════════════════════════════════════════╝\n")

"""
O USUÁRIO PENSA EM NÚMEROS 1-9:
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

MAS PROGRAMAMOS COM ÍNDICES [linha][coluna]:
[0][0] | [0][1] | [0][2]
  1   |   2   |   3
[1][0] | [1][1] | [1][2]
  4   |   5   |   6
[2][0] | [2][1] | [2][2]
  7   |   8   |   9

FÓRMULA DE CONVERSÃO:
linha = (posicao - 1) // 3     (divisão inteira)
coluna = (posicao - 1) % 3     (resto da divisão)
"""

print("Exemplos de conversão:")
for posicao in [1, 2, 5, 9]:
    linha = (posicao - 1) // 3
    coluna = (posicao - 1) % 3
    print(f"Posição {posicao} → linha {linha}, coluna {coluna}")

print()

# ============================================================================
# PASSO 3: EXIBIR O TABULEIRO VISUALMENTE
# ============================================================================

print("╔════════════════════════════════════════════════════════════╗")
print("║ PASSO 3: Função para Exibir o Tabuleiro                  ║")
print("╚════════════════════════════════════════════════════════════╝\n")

def exibir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro de forma bonita"""
    print("\n")
    for i in range(3):
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")

# Vamos criar um tabuleiro de exemplo
tabuleiro_exemplo = [
    ["X", "O", " "],
    [" ", "X", " "],
    ["O", " ", "X"]
]

print("Outputdafunção exibir_tabuleiro():")
exibir_tabuleiro(tabuleiro_exemplo)

print("COMO FUNCIONA:")
print("- Usa um loop for para percorrer as 3 linhas")
print("- Imprime cada célula: tabuleiro[i][0], tabuleiro[i][1], tabuleiro[i][2]")
print("- Desenha linhas (-------) entre as linhas do jogo\n")


# ============================================================================
# PASSO 4: VERIFICAR VITÓRIA
# ============================================================================

print("╔════════════════════════════════════════════════════════════╗")
print("║ PASSO 4: Função para Verificar Vitória                   ║")
print("╚════════════════════════════════════════════════════════════╝\n")

"""
PARA VENCER, PRECISA DE 3 EM UMA LINHA:
- 3 LINHAS HORIZONTAIS
  [X][X][X] [ ][ ][ ] [ ][ ][ ]
  
- 3 COLUNAS VERTICAIS
  [X][ ][ ]  [X][ ][ ]  [X][ ][ ]
  [X][ ][ ]  [X][ ][ ]  [X][ ][ ]
  [X][ ][ ]  [X][ ][ ]  [X][ ][ ]
  
- 2 DIAGONAIS
  [X][ ][ ]  [ ][ ][X]
  [ ][X][ ]  [ ][X][ ]
  [ ][ ][X]  [X][ ][ ]
"""

def verificar_vitoria(tabuleiro, jogador):
    """
    Verifica se o jogador (X ou O) venceu.
    Retorna True se venceu, False caso contrário.
    """
    
    # VERIFICAR LINHAS
    # Se encontrar uma linha inteira do jogador, ele venceu!
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            print(f"✓ Vitória encontrada em linha!")
            return True
    
    # VERIFICAR COLUNAS
    # Se uma coluna inteira é do jogador, ele venceu!
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            print(f"✓ Vitória encontrada em coluna!")
            return True
    
    # VERIFICAR DIAGONAL PRINCIPAL (↘)
    # [0][0], [1][1], [2][2]
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        print(f"✓ Vitória encontrada na diagonal principal (↘)!")
        return True
    
    # VERIFICAR DIAGONAL SECUNDÁRIA (↙)
    # [0][2], [1][1], [2][0]
    if all(tabuleiro[i][2-i] == jogador for i in range(3)):
        print(f"✓ Vitória encontrada na diagonal secundária (↙)!")
        return True
    
    # Nenhuma vitória encontrada
    return False

# Testando a função
print("Testando com X em uma linha:")
teste1 = [
    ["X", "X", "X"],
    ["O", " ", " "],
    ["O", " ", " "]
]
resultado = verificar_vitoria(teste1, "X")
print(f"X venceu? {resultado}\n")

print("Testando com O em uma coluna:")
teste2 = [
    ["X", "O", " "],
    ["X", "O", " "],
    [" ", "O", " "]
]
resultado = verificar_vitoria(teste2, "O")
print(f"O venceu? {resultado}\n")

print("Testando sem vitória:")
teste3 = [
    ["X", "O", " "],
    [" ", "X", " "],
    ["O", " ", " "]
]
resultado = verificar_vitoria(teste3, "X")
print(f"X venceu? {resultado}\n")


# ============================================================================
# PASSO 5: VERIFICAR EMPATE
# ============================================================================

print("╔════════════════════════════════════════════════════════════╗")
print("║ PASSO 5: Função para Verificar Empate                    ║")
print("╚════════════════════════════════════════════════════════════╝\n")

def verificar_empate(tabuleiro):
    """
    Verifica se o jogo empatou.
    Empate = tabuleiro cheio e ninguém venceu
    """
    for linha in tabuleiro:
        if " " in linha:
            return False  # Ainda existem espaços vazios, não é empate
    
    return True  # Tabuleiro inteiro preenchido = empate

print("Testando empate com tabuleiro cheio:")
teste_empate = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]
resultado = verificar_empate(teste_empate)
print(f"É empate? {resultado}\n")

print("Testando com espaço vazio:")
teste_nao_empate = [
    ["X", "O", "X"],
    ["O", "X", " "],
    ["O", "X", "X"]
]
resultado = verificar_empate(teste_nao_empate)
print(f"É empate? {resultado}\n")


# ============================================================================
# PASSO 6: PEGAR MOVIMENTO DO JOGADOR
# ============================================================================

print("╔════════════════════════════════════════════════════════════╗")
print("║ PASSO 6: Função para Pegar Movimento do Jogador           ║")
print("╚════════════════════════════════════════════════════════════╝\n")

print("""
Um bom movimento do jogador deve:
1. Pedir um número entre 1 e 9
2. Validar se é um número válido
3. Checar se a posição já está ocupada
4. Retornar as coordenadas (linha, coluna)

Usamos LOOPS e TRATAMENTO DE ERROS para isso!
""")

def movimento_valido(posicao, tabuleiro):
    """Verifica se um movimento é válido"""
    
    # Verificar se está no intervalo 1-9
    if posicao < 1 or posicao > 9:
        print("❌ Número deve estar entre 1 e 9!")
        return False
    
    # Converter para coordenadas
    linha = (posicao - 1) // 3
    coluna = (posicao - 1) % 3
    
    # Verificar se a posição está vazia
    if tabuleiro[linha][coluna] != " ":
        print("❌ Essa posição já está ocupada!")
        return False
    
    print("✓ Movimento válido!")
    return True

# Testando
tabuleiro_teste = [
    [" ", "X", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print("Teste 1: Posição 1 (vazia):")
movimento_valido(1, tabuleiro_teste)

print("\nTeste 2: Posição 2 (já ocupada):")
movimento_valido(2, tabuleiro_teste)

print("\nTeste 3: Posição 10 (fora do intervalo):")
movimento_valido(10, tabuleiro_teste)


# ============================================================================
# PASSO 7: TROCAR DE JOGADOR
# ============================================================================

print("\n╔════════════════════════════════════════════════════════════╗")
print("║ PASSO 7: Função para Trocar de Jogador                   ║")
print("╚════════════════════════════════════════════════════════════╝\n")

def trocar_jogador(jogador):
    """Alterna entre X e O"""
    if jogador == "X":
        return "O"
    else:
        return "X"

# Testando
jogador = "X"
print(f"Jogador atual: {jogador}")
jogador = trocar_jogador(jogador)
print(f"Próximo jogador: {jogador}")
jogador = trocar_jogador(jogador)
print(f"Próximo jogador: {jogador}\n")


# ============================================================================
# PASSO 8: COLOCAR TUDO JUNTO - O JOGO COMPLETO
# ============================================================================

print("╔════════════════════════════════════════════════════════════╗")
print("║ PASSO 8: Colocando Tudo Junto - Loop Principal do Jogo   ║")
print("╚════════════════════════════════════════════════════════════╝\n")

print("""
O FLUXO DO JOGO:

1. Criar um tabuleiro vazio
2. Definir jogador como X
3. ENQUANTO o jogo não terminou:
   a. Mostrar o tabuleiro
   b. Pedir movimento para o jogador
   c. Colocar X ou O no tabuleiro
   d. Verificar se o jogador venceu → terminar
   e. Verificar se é empate → terminar
   f. Trocar de jogador
   g. Voltar ao passo 3a

CÓDIGO:
""")

print("""
# Inicializar
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador = "X"

# Loop principal
while True:
    exibir_tabuleiro(tabuleiro)
    
    # Pedir movimento
    movimento = pedir_movimento(jogador, tabuleiro)
    linha, coluna = movimento
    tabuleiro[linha][coluna] = jogador
    
    # Verificar vitória
    if verificar_vitoria(tabuleiro, jogador):
        exibir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador} VENCEU!")
        break
    
    # Verificar empate
    if verificar_empate(tabuleiro):
        exibir_tabuleiro(tabuleiro)
        print("EMPATE!")
        break
    
    # Trocar jogador
    jogador = trocar_jogador(jogador)
""")

print("\n" + "="*60)
print("RESUMO: TUDO QUE VOCÊ PRECISA PARA FAZER UM JOGO DA VELHA")
print("="*60 + "\n")

print("""
✓ Dados:
  - Um tabuleiro 3x3 (lista dentro de lista)
  
✓ Funções Básicas:
  1. exibir_tabuleiro()      → mostra visual do jogo
  2. verificar_vitoria()     → checa se alguém venceu
  3. verificar_empate()      → checa se tabuleiro está cheio
  4. movimento_jogador()     → pega a jogada do usuário
  5. trocar_jogador()        → alterna entre X e O
  
✓ Lógica Principal:
  - Um loop "while True" que roda até terminar
  - Dentro do loop: mostrar → jogar → verificar → trocar
  - Quando alguém vencer ou empatar → quebrar o loop

✓ Extras para melhorar:
  - Tratamento de erros (try/except)
  - IA do computador
  - Menu para jogar novamente
  - Emojis e cores para deixar mais legal

AGORA VOCÊ SABE COMO UM JOGO DA VELHA FUNCIONA! 🎉
""")
