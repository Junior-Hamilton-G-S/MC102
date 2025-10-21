###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Bingo
# Nome:
# RA:
###################################################

# Leitura da cartela
cartela = [list(map(int, input().split())) for _ in range(5)]
print("cartela =", cartela)

def CartelaHozizontal(cartela, posicao_linha):
    for i in range(posicao_linha - 1, posicao_linha):
        horizontal = cartela[i]
    print("horizontal =", horizontal)

def CartelaVertical(cartela, posicao_coluna):
    vertical = []
    for j in range(posicao_coluna - 1, posicao_coluna):  
        for i in range(5):
            vertical.append(cartela[i][j])
    print("vertical =", vertical)

def CartelaDiagonal(cartela):
    diagonalPrincipal = []
    for i in range(5):
        for j in range(5):
            if i == j:
                diagonalPrincipal.append(cartela[i][j])
    print("diagonal Principal =", diagonalPrincipal)

    diagonalSecundaria = []
    for i in range(5):
        for j in range(5):
            if i + j == 4:
                diagonalSecundaria.append(cartela[i][j])
    print("diagonal Secundária=", diagonalSecundaria)


CartelaHozizontal(cartela, numero)
CartelaVertical(cartela, numero)
CartelaDiagonal(cartela)

# Processamento do Bingo

#Prioridade:
#1° horizontal
#2° vertical
#3° diagonal

numeros_sorteados = 0
while numeros_sorteados <= 75:
    sorteio = int(input())
    print("sorteio =", sorteio)

    cartela[sorteio]
    numeros_sorteados += 1

# Saída do programa