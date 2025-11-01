###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Joomba I
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

# Leitura dos valores de A (andares) e J (janelas)
quantidade_andares, quantidade_janelas = input().split(' ')
print("quantidade de andares =", quantidade_andares, "\nquantidade de janelas =", quantidade_janelas)

def DesenhaPredio(quantidade_andares, quantidade_janelas):
    face_do_predio = []
    janelas_no_andar = ["#"] * int(quantidade_janelas)
    for andar in range(int(quantidade_andares)):
        face_do_predio.append(janelas_no_andar.copy())
    
    face_norte = []
    face_oeste = []
    face_sul = []
    face_leste = []
    for andar in face_do_predio:  
        face_norte.append(andar.copy())
        face_oeste.append(andar.copy())
        face_sul.append(andar.copy())
        face_leste.append(andar.copy())
    
    face_norte[int(quantidade_andares) - 1][0] = "R"

    return [face_norte, face_oeste, face_sul, face_leste]

face_norte, face_oeste, face_sul, face_leste = DesenhaPredio(quantidade_andares, quantidade_janelas)

# Leitura e processamento dos comandos
def PosicaoJoomba(face_do_predio):
    posicao_joomba = []
    for linha, andar in enumerate(face_do_predio):
        for coluna, letra in enumerate(andar):
            if "R" == letra:
                posicao_joomba.append(linha)
                posicao_joomba.append(coluna)
                return (face_do_predio, posicao_joomba)
            else:
                break

ordem_esquerda = [face_norte, face_leste, face_sul, face_oeste]
ordem_direita = [face_norte, face_oeste, face_sul, face_leste]
while :
    direcao, janelas_percorridas = input().split(' ')
    matriz_joomba, posicao_joomba = PosicaoJoomba(face_norte) 

    if direcao == "E":
        for janela in janelas_percorridas:
            if posicao_joomba[1] == 0
                matriz_joomba[posicao_joomba] = "."
                ordem_esquerda[matriz_joomba + 1][posicao_joomba[0]][posicao_joomba[1] + (posicao_joomba[1] - 1)] = "R"
            if posicao_joomba[1] != 0:
                matriz_joomba[(posicao_joomba[0]-1)][posicao_joomba[1]] = "R"
                matriz_joomba[posicao_joomba] = "."

    if direcao == "D":
        for janela in janelas_percorridas:
            if posicao_joomba[1] == int(quantidade_janelas) - 1:
                matriz_joomba[posicao_joomba] = "."
                ordem_direita[matriz_joomba + 1][posicao_joomba[0]][posicao_joomba[1] + (posicao_joomba[1] - 1)] = "R"
            if posicao_joomba[1] != int(quantidade_janelas) - 1:
                matriz_joomba[posicao_joomba[0]][(posicao_joomba[1] + 1)] = "R"
                matriz_joomba[posicao_joomba] = "."

    if direcao == "C":
        for janela in janelas_percorridas:
            if posicao_joomba[0] == 0:
                continue
            if posicao_joomba[0] != 0:
                matriz_joomba[(posicao_joomba[0] - 1)][posicao_joomba[1]] = "R"
                matriz_joomba[posicao_joomba] = "."

    if direcao == "B":
        for janela in janelas_percorridas:
            if posicao_joomba[0] == int(quantidade_andares) - 1:
                continue
            if posicao_joomba[0] != int(quantidade_andares) - 1:
                matriz_joomba[(posicao_joomba[0] + 1)][posicao_joomba[1]] = "R"
                matriz_joomba[posicao_joomba] = "."

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
