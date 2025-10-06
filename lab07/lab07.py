###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Conectando Picos
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################


# Leitura da cordilheira
cordilheira = list(map(int, input().split()))


# Calculo do número mínimo de cabos necessários
numero_de_cabos = 0
posicao_atual = 0
total_de_pontos = len(cordilheira)

while posicao_atual < total_de_pontos - 1:
    for posicao_candidata in range(total_de_pontos - 1, posicao_atual, -1):
        obstruido = False
        # Verifica se algum pico intermediário obstrui o caminho
        # Um pico k obstrui se a inclinação (atual -> k) >= (atual -> candidato)
        for posicao_intermediaria in range(posicao_atual + 1, posicao_candidata):
            # Coeficiente angular entre o pico atual e o candidato
            # (y2 - y1) / (x2 - x1) -> (cordilheira[j] - cordilheira[i]) / (j - i)
            # (cordilheira[k] - cordilheira[i]) / (k - i) >= (cordilheira[j] - cordilheira[i]) / (j - i)
            # (cordilheira[k] - cordilheira[i]) * (j - i) >= (cordilheira[j] - cordilheira[i]) * (k - i)
            altura_intermediaria = cordilheira[posicao_intermediaria]
            altura_atual = cordilheira[posicao_atual]
            altura_candidata = cordilheira[posicao_candidata]

            termo1 = (altura_intermediaria - altura_atual) * (posicao_candidata - posicao_atual)
            termo2 = (altura_candidata - altura_atual) * (posicao_intermediaria - posicao_atual)
            
            if termo1 >= termo2:
                obstruido = True
                break
            
        if not obstruido:
            numero_de_cabos += 1
            posicao_atual = posicao_candidata
            break


# Impressão da saída
print(numero_de_cabos)