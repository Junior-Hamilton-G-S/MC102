###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Joomba I
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

# Leitura dos valores de A (andares) e J (janelas)
quantidade_andares, quantidade_janelas = input().split(' ')

def DesenhaPredio(quantidade_andares, quantidade_janelas):
    def criar_face():
        face = []
        for andar in range(int(quantidade_andares)):
            janelas_no_andar = ["#"] * int(quantidade_janelas)
            face.append(janelas_no_andar)
        return face

    face_norte = criar_face()
    face_oeste = criar_face()
    face_sul = criar_face()
    face_leste = criar_face()
    face_norte[0][0] = "R"

    return [face_norte, face_oeste, face_sul, face_leste]

predio_inteiro = DesenhaPredio(quantidade_andares, quantidade_janelas)
face_atual = 0

# Leitura e processamento dos comandos
def PosicaoJoomba(face_index):
    matriz = predio_inteiro[face_index]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == "R":
                return [linha, coluna]
    return None

def MudaFace(face_atual, posicao_joomba, direcao):
    matriz_atual = predio_inteiro[face_atual]
    matriz_atual[posicao_joomba[0]][posicao_joomba[1]] = "."

    if direcao == "D":
        face_atual = (face_atual + 1) % 4
        posicao_joomba[1] = 0
    elif direcao == "E":
        face_atual = (face_atual - 1) % 4
        posicao_joomba[1] = int(quantidade_janelas) - 1

    matriz_nova = predio_inteiro[face_atual]
    matriz_nova[posicao_joomba[0]][posicao_joomba[1]] = "R"

    return face_atual

while True:
    direcao, janelas_percorridas = input().split(' ')
    posicao_joomba = PosicaoJoomba(face_atual)

    if direcao == "F" and janelas_percorridas == "0":
        break

    matriz_atual = predio_inteiro[face_atual]

    if direcao == "D":
        for janela in range(int(janelas_percorridas)):
            if posicao_joomba[1] < int(quantidade_janelas) - 1:
                matriz_atual[posicao_joomba[0]][posicao_joomba[1]] = "."
                posicao_joomba[1] = posicao_joomba[1] + 1
                matriz_atual[posicao_joomba[0]][posicao_joomba[1]] = "R"
            else:
                face_atual = MudaFace(face_atual, posicao_joomba, direcao)
                matriz_atual = predio_inteiro[face_atual]

    elif direcao == "E":
        for janela in range(int(janelas_percorridas)):
            if posicao_joomba[1] > 0:
                matriz_atual[posicao_joomba[0]][posicao_joomba[1]] = "."
                posicao_joomba[1] = posicao_joomba[1] - 1
                matriz_atual[posicao_joomba[0]][posicao_joomba[1]] = "R"
            else:
                face_atual = MudaFace(face_atual, posicao_joomba, direcao)
                matriz_atual = predio_inteiro[face_atual]

    elif direcao == "C":
        for janela in range(int(janelas_percorridas)):
            if posicao_joomba[0] < int(quantidade_andares) - 1:
                matriz_atual[posicao_joomba[0]][posicao_joomba[1]] = "."
                posicao_joomba[0] = posicao_joomba[0] + 1
                matriz_atual[posicao_joomba[0]][posicao_joomba[1]] = "R"

    elif direcao == "B":
        for janela in range(int(janelas_percorridas)):
            if posicao_joomba[0] > 0:
                matriz_atual[posicao_joomba[0]][posicao_joomba[1]] = "."
                posicao_joomba[0] = posicao_joomba[0] - 1
                matriz_atual[posicao_joomba[0]][posicao_joomba[1]] = "R"

face_norte, face_oeste, face_sul, face_leste = predio_inteiro

# Impressão do resultado final
def ImprimePredio(nome_da_face, face_do_predio):
    print(nome_da_face)
    ultimo_andar = int(quantidade_andares) - 1
    for i in range(ultimo_andar, -1, -1):
        print("".join(face_do_predio[i]))
    print("-" * int(quantidade_janelas))

ImprimePredio("Face N", face_norte)
ImprimePredio("Face O", face_oeste)
ImprimePredio("Face S", face_sul)
ImprimePredio("Face L", face_leste)