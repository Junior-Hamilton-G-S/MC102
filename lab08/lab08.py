###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 08 - Flush
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################


# Leitura da entrada
baralho = input()
flushes_c = 0
flushes_o = 0
flushes_e = 0
flushes_p = 0


# Processamento da entrada
for i in range(len(baralho) - 8):
    mao = baralho[i : i + 9]
    if mao.count('C') >= 5:
        flushes_c += 1
    elif mao.count('O') >= 5:
        flushes_o += 1
    elif mao.count('E') >= 5:
        flushes_e += 1
    elif mao.count('P') >= 5:
        flushes_p += 1


# Impressão da saída
print(flushes_c, flushes_o, flushes_e, flushes_p)