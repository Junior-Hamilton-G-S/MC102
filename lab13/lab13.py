###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Recomendação de Locais
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

# Leitura dos locais
dados_dos_locais = [] # dados_dos_locais (matriz): uma atriz que armazenará as informações dos locais em cada informacoes_local
while True:
    informacoes_local = input()
    if informacoes_local == "FIM":
        break

    else:
        dados_dos_locais.append(informacoes_local.split(' '))


# Leitura dos parâmetros do usuário
# Variaveis
    # x_usuario y_usuario (float): a posição atual do usuário em um mapa 2D;
    # numero_de_recomendacoes (int): o número de recomendações que o usuário deseja ver;
    # categoria_usuario (str): para filtrar os resultados por uma categoria específica (como "museu", "parque", "restaurante", etc). Se "Nenhuma", todos os locais devem ser considerados.
informacoes_do_usuario = input().split(' ')
x_usuario = float(informacoes_do_usuario[0])
y_usuario = float(informacoes_do_usuario[1])
numero_de_recomendacoes = int(informacoes_do_usuario[2])
categoria_usuario = str(informacoes_do_usuario[3])


# Calcular distância euclidiana e pontuação
def CalculaDistancia(x_usuario, y_usuario, x_local, y_local):
    # distancia = √((x_usuario - x_local)² + (y_usuario - y_local)²)
    distancia_ao_quadrado = (x_usuario - x_local)**2 + (y_usuario - y_local)**2
    distancia = distancia_ao_quadrado**0.5 # Calcula a raiz quadrada da distância_ao_quadrado
    return distancia

def CalculaPontuacao(popularidade_local, distancia): 
    pontuacao = popularidade_local / (distancia + 1)
    return pontuacao


# Ordenação por pontuação
def OrdenaLocais():
    lista_de_recomendacoes = []
    for informacoes_local in dados_dos_locais: # varre as linhas da matriz
        # Variaveis
            # nome_local (str): o nome do ponto turístico;
            # x_local, y_local (float): as coordenadas do local em um mapa 2D;
            # categoria (str): o tipo de local ("praia", "parque", "cultural", etc);
            # popularidade (int): uma nota de 1 a 10 que representa o quão famoso ou bem avaliado é o local (quanto maior, melhor).
        nome_local = str(informacoes_local[0])
        x_local = float(informacoes_local[1])
        y_local = float(informacoes_local[2])
        categoria_local = str(informacoes_local[3])
        popularidade_local = int(informacoes_local[4])

        if categoria_usuario != "Nenhuma" and categoria_local != categoria_usuario:
            continue

        distancia = CalculaDistancia(x_usuario, y_usuario, x_local, y_local)
        pontuacao = CalculaPontuacao(popularidade_local, distancia)

        lista_de_recomendacoes.append([nome_local, categoria_local, distancia, pontuacao])

    return lista_de_recomendacoes

def ArrumaLista(lista):
    for _ in range(len(lista)): # percorre denovo para casos de 2 trocas
        for linha in range(len(lista) - 1): # varre as linhas da lista

            pontuacao_linha_atual = lista[linha][3]
            pontuacao_linha_seguinte = lista[linha + 1][3]

            if pontuacao_linha_atual < pontuacao_linha_seguinte:   # se a pontuação da linha atual for menor que a de baixo... 
                lista[linha], lista[linha + 1] = lista[linha + 1], lista[linha]

    return lista

# Exibir resultados
def ExibeResultado(numero_de_recomendacoes, categoria_usuario):
    lista = ArrumaLista(OrdenaLocais())
    print("Recomendações:")

    recomendacoes = min(numero_de_recomendacoes, len(lista))
    for numero in range(recomendacoes):

        nome_local = str(lista[numero][0])
        categoria_local = str(lista[numero][1])
        distancia = float(lista[numero][2])
        pontuacao = float(lista[numero][3])

        print(f"{nome_local} {categoria_local} {round(distancia, 2)} {round(pontuacao, 2)}")

ExibeResultado(numero_de_recomendacoes, categoria_usuario)