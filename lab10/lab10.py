###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Bingo
# Nome:
# RA:
###################################################

# Leitura da cartela
cartela = [list(map(int, input().split())) for _ in range(5)]

def CartelaHozizontal(cartela, posicao_linha):
    return cartela[posicao_linha]

def CartelaVertical(cartela, posicao_coluna):
    vertical = []
    for i in range(5):
        vertical.append(cartela[i][posicao_coluna])
    return vertical

def CartelaDiagonal(cartela):
    diagonalPrincipal = []
    diagonalSecundaria = []
    for i in range(5):
        for j in range(5):
            if i == j:
                diagonalPrincipal.append(cartela[i][j])

            if i + j == 4:
                diagonalSecundaria.append(cartela[i][j])

    return(diagonalPrincipal, diagonalSecundaria)

def PosicaoSorteio(cartela, sorteio):
    for posicao_linha, linha in enumerate(cartela):
        for posicao_coluna, numero in enumerate(linha):
            if numero == sorteio:
                cartela_apos_sorteio[posicao_linha][posicao_coluna] = 0
                return(posicao_linha, posicao_coluna)
    return None

# Processamento do Bingo

#Prioridade:
#1° horizontal
#2° vertical
#3° diagonal

def VerificaBingo(cartela_apos_sorteio, sorteio):
    posicoes_do_sorteio = PosicaoSorteio(cartela_apos_sorteio, sorteio)
    
    if posicoes_do_sorteio is None:
        return None

    diagonalPrincipal, diagonalSecundaria = CartelaDiagonal(cartela_apos_sorteio)
    posicao_linha, posicao_coluna = posicoes_do_sorteio
    horizontal = CartelaHozizontal(cartela_apos_sorteio, posicao_linha)
    vertical = CartelaVertical(cartela_apos_sorteio, posicao_coluna)

    if sum(horizontal) == 0:
        return CartelaHozizontal(cartela, posicao_linha)

    if sum(vertical) == 0:
        return CartelaVertical(cartela, posicao_coluna)

    if sum(diagonalPrincipal) == 0 or sum(diagonalSecundaria) == 0:
        diagonalPrincipal_da_sorte, diagonalSecundaria_da_sorte = CartelaDiagonal(cartela)

        if sum(diagonalPrincipal) == 0:
            return(diagonalPrincipal_da_sorte)

        if sum(diagonalSecundaria) == 0:
            return(diagonalSecundaria_da_sorte)

    return(None)

numeros_sorteados = 0
cartela_apos_sorteio = []
for linha in cartela:
    cartela_apos_sorteio.append(linha.copy())

# Saída do programa
while numeros_sorteados <= 75:
    sorteio = int(input())

    numeros_da_sorte = VerificaBingo(cartela_apos_sorteio, sorteio)
    if numeros_da_sorte is not None:
        print("Os números da sorte foram:", ", ".join(map(str, numeros_da_sorte)))
        break

    else:
        numeros_sorteados += 1
        continue