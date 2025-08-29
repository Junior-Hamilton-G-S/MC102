###################################################
# MC102 - Algoritmos e Programação de Computadores
# # Laboratório 2 - Próxima Aula
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
d = float(input())
v = float(input())

# Leitura da entrada

deltah = ((h2 - h1) * 60)
deltam = (m2 - m1)
tempo_disponivel = (deltah + deltam)
tempo_previsto = ((d / 1000 / v) * 60)

# Cálculos e impressão da saída

if tempo_previsto <= tempo_disponivel:
    print("True")
else:
    print("False")

