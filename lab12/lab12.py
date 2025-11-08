###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Horta Vertical
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

# Leitura da horta
altura_horta = int(input()) # número de linhas da matriz que representa a horta
matriz_horta = [] # matriz que representa a horta
for linha in range(altura_horta):
    matriz_horta.append(list(input())) # recebe as entradas ("." ou "#") da matriz_horta : "." indica uma posição livre e "# indica uma posição ocupada

altura_horta = len(matriz_horta)
largura_horta = len(matriz_horta[0])

# Leitura e posicionamento de cada planta
def VerificaSeCabe(matriz_horta, matriz_planta, linha_ancora, coluna_ancora, altura_planta, largura_planta):

    for linha_planta in range(altura_planta):
        for coluna_planta in range(largura_planta):
            linha_na_horta = linha_ancora + linha_planta
            coluna_na_horta = coluna_ancora + coluna_planta

            if "#" == matriz_planta[linha_planta][coluna_planta]:
                if not (0 <= linha_na_horta < altura_horta and 0 <= coluna_na_horta < largura_horta):
                    return False
                    
                if "#" == matriz_horta[linha_na_horta][coluna_na_horta]:
                    return False

    return True

def PlantaNaHorta(matriz_horta, matriz_planta, linha_ancora, coluna_ancora, altura_planta, largura_planta):

    for linha_planta in range(altura_planta):
        for coluna_planta in range(largura_planta):
            if "#" == matriz_planta[linha_planta][coluna_planta]:
                linha_na_horta = linha_ancora + linha_planta
                coluna_na_horta = coluna_ancora + coluna_planta
                if (0 <= linha_na_horta < altura_horta and 0 <= coluna_na_horta < largura_horta):
                    matriz_horta[linha_na_horta][coluna_na_horta] = "#"
    
    return matriz_horta

def PosicionaPlanta(matriz_horta, matriz_planta, tipo_planta, altura_planta, largura_planta):

    if "P" == tipo_planta:
        varia_range = range(altura_horta - 1, -1, -1)
    else: # "L"
        varia_range = range(altura_horta)

    for linha_ancora in varia_range:
        for coluna_ancora in range(largura_horta):
            if VerificaSeCabe(matriz_horta, matriz_planta, linha_ancora, coluna_ancora, altura_planta, largura_planta):
                matriz_horta = PlantaNaHorta(matriz_horta, matriz_planta, linha_ancora, coluna_ancora, altura_planta, largura_planta)
                return matriz_horta 

    return matriz_horta

quantidade_plantas = int(input())# número de plantas que irão ser colocadas na horta
for planta in range(quantidade_plantas):
    planta_linhas = int(input()) # número de 'linhas' da planta, i.e. tamanho vertical da planta
    matriz_planta = [] # matriz que representa o tamanho (as entradas) que a planta ocupa na horta
    for linha in range(planta_linhas):
        matriz_planta.append(list(input())) # recebe as entradas ("." ou "#") do matriz_planta : "." indica uma posição livre e "# indica uma posição ocupada
    
    altura_planta = len(matriz_planta)
    largura_planta = len(matriz_planta[0])

    tipo_planta = str(input()) # recebe o tipo da planta ("P" = planta de solo ou "L" = planta de altitude)
    matriz_horta = PosicionaPlanta(matriz_horta, matriz_planta, tipo_planta, altura_planta, largura_planta)


# Impressão da horta
for linha in matriz_horta:
    print("".join(linha))