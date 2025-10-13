###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 08 - Flush
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################


# Regras do jogo: constantes para a análise
TAMANHO_JANELA = 9
CARTAS_PARA_FLUSH = 5
NAIPES = ['C', 'O', 'E', 'P']


# Leitura da entrada
baralho = input()


# Contagem de flushes para cada naipe
contagem_flushes = {'C': 0, 'O': 0, 'E': 0, 'P': 0}


# Analisa cada janela de 9 cartas
for i in range(len(baralho) - TAMANHO_JANELA + 1):
    mao = baralho[i : i + TAMANHO_JANELA]

    # Verifica se há um flush na mão atual
    for naipe in NAIPES:
        if mao.count(naipe) >= CARTAS_PARA_FLUSH:
            contagem_flushes[naipe] += 1
            # Encontrou um flush, avança para a próxima janela
            break


# Impressão da saída
print(f"{contagem_flushes['C']} {contagem_flushes['O']} {contagem_flushes['E']} {contagem_flushes['P']}")