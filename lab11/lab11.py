###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Joomba I
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

# Leitura dos valores de A (andares) e J (janelas)
quantidade_andares, quantidade_janelas = input().split(' ')

def DesenhaPredio(quantidade_andares, quantidade_janelas):
    face_do_predio = []
    janelas_no_andar = ["#"] * int(quantidade_janelas)
    for andar in range(int(quantidade_andares)):
        face_do_predio.append(janelas_no_andar.copy())
    
    face_norte = face_do_predio.copy()
    face_oeste = face_do_predio.copy()
    face_sul = face_do_predio.copy() 
    face_leste = face_do_predio.copy()
    face_norte[int(quantidade_andares) - 1][0] = "R"

    return [face_norte, face_oeste, face_sul, face_leste]

predio_inteiro = DesenhaPredio(quantidade_andares, quantidade_janelas)

matriz_atual = predio_inteiro[0]

# Leitura e processamento dos comandos
def PosicaoJoomba(matriz_joomba):
    posicao_joomba = []
    for linha, andar in enumerate(matriz_joomba):
        for coluna, letra in enumerate(andar):
            if "R" == letra:
                posicao_joomba.append(linha)
                posicao_joomba.append(coluna)
                return (matriz_joomba, posicao_joomba)

def MudaFace(matriz_joomba, posicao_joomba, direcao):
    if direcao == "D":
        matriz_joomba = predio_inteiro[matriz_joomba.index(matriz_joomba) + 1 % 4]
        posicao_joomba[1] = 0
        matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "R"
        return PosicaoJoomba(matriz_joomba)

    elif direcao == "E":
        matriz_joomba = predio_inteiro[matriz_joomba.index(matriz_joomba) - 1 % 4]
        posicao_joomba[1] = int(quantidade_janelas) - 1
        matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "R"
        return PosicaoJoomba(matriz_joomba) 

while True:
    direcao, janelas_percorridas = input().split(' ')
    matriz_joomba, posicao_joomba = PosicaoJoomba(matriz_atual)

    if direcao == "D":
        for janela in range(int(janelas_percorridas)):
            if not posicao_joomba[1] == int(quantidade_janelas) - 1:
                matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "."
                posicao_joomba[1] += 1
                matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "R"


            elif posicao_joomba[1] == int(quantidade_janelas) - 1:
                matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "."
                matriz_atual = MudaFace(matriz_joomba, posicao_joomba, direcao)
                continue

    if direcao == "E":
        for janela in range(int(janelas_percorridas)):
            if not posicao_joomba[1] == int(quantidade_janelas) - 1:
                matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "."
                posicao_joomba[1] -= 1
                matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "R"

            elif posicao_joomba[1] == int(quantidade_janelas) - 1:
                matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "."
                matriz_atual = MudaFace(matriz_joomba, posicao_joomba, direcao)
                continue

    if direcao == "C":
        for janela in range(int(janelas_percorridas)):
            if not posicao_joomba[0] == 0:
                matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "."
                posicao_joomba[0] -= 1
                matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "R"

            if posicao_joomba[0] == 0:
                matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "."
                continue

    if direcao == "B":
        for janela in range(int(janelas_percorridas)):
            if not posicao_joomba[0] == int(quantidade_andares) - 1:
                matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "."
                posicao_joomba[0] += 1
                matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "R"

            elif posicao_joomba[0] == int(quantidade_andares) - 1:
                matriz_joomba[posicao_joomba[0]][posicao_joomba[1]] = "."
                continue

    if direcao == "F" and janelas_percorridas == "0":
        break

# Impressão do resultado final
def ImprimePredio(nome_da_face, face_do_predio):
    print(nome_da_face)
    for andar in face_do_predio:
        print("".join(andar))
        
    print("-" * int(quantidade_janelas))

ImprimePredio("Face N", face_norte)
ImprimePredio("Face O", face_oeste)
ImprimePredio("Face S", face_sul)
ImprimePredio("Face L", face_leste)