###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Horta Vertical
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

# Leitura da horta
horta_linhas = int(input()) # número de linhas da matriz que representa a horta
matriz_horta = [] # matriz que representa a horta
for linha in range(horta_linhas):
    matriz_horta.append(input()) # recebe as entradas ("." ou "#") da matriz_horta : "." indica uma posição livre e "# indica uma posição ocupada


# Leitura e posicionamento de cada planta
def PosicionaPlanta(tipo_planta, matriz_planta):
    quantidade_linhas_planta = len(matriz_planta)
    quantidade_colunas_planta = len(matriz_planta[0])
    quantidade_linhas_horta = len(matriz_horta)
    quantidade_colunas_horta = len(matriz_horta[0])
    matriz_provisoria = []
    for linha_horta in range(matriz_horta):
        matriz_provisoria.append(linha_horta.copy())

    if tipo_planta == "P": # "P" é a planta de solo: linha mais baixa e posição mais à esquerda
        for linha_horta in range(horta_linhas, 0, -1):
            for coluna_horta in range(len(matriz_horta[linha_horta]), 0, -1):
                if matriz_horta[linha_horta][coluna_horta] == ".":
                    linhas_provisorias = quantidade_linhas_horta - quantidade_linhas_planta
                    colunas_provisorias = quantidade_colunas_horta - quantidade_colunas_planta
                    for linhas_apagadas in range(linhas_provisorias):
                        for colunas_apagadas in range(colunas_provisorias, 0, -1):
                            del matriz_provisoria[linhas_apagadas]
                            del matriz_provisoria[linhas_apagadas][colunas_apagadas]
                    print("\n", matriz_provisoria)  
                print("\n", matriz_provisoria)
            print("\n", matriz_provisoria)
        print("\n", matriz_provisoria)   
        return

    if tipo_planta == "L": # "L" é a planta de altitude: linha mais alta e posição mais à esquerda


        return

# looping 

# leitura
planta_linhas = int(input()) #número de 'linhas' da planta, i.e. tamanho vertical da planta
matriz_planta = [] # matriz que representa o tamanho (as entradas) que a planta ocupa na horta
for linha in range(planta_linhas):
    matriz_planta.append(input()) # recebe as entradas ("." ou "#") do matriz_planta : "." indica uma posição livre e "# indica uma posição ocupada
tipo_planta = str(input()) # recebe o tipo da planta ("P" = planta de solo ou "L" = planta de altitude) 

# processamento
PosicionaPlanta(tipo_planta, matriz_planta)


# Impressão da horta
print(matriz_horta)