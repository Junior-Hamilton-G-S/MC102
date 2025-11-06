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

def ProcuraPonto(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == ".":
                return [linha, coluna]

def VerificaSeAPlantaCabe(matriz_horta, linha, coluna, matriz_planta):
    for linha_planta in range(plantas_linhas): 
        for coluna_planta in range(matriz_planta[linha_planta]):
            matriz_horta[linha][coluna] 

def PosicionaPlanta(tipo_planta, matriz_planta):
    if tipo_planta == "P": # "P" é a planta de solo: Sempre tentar posicionar na linha mais baixa possível e, dentro dessa linha, na posição mais à esquerda possível
        
        return

    if tipo_planta == "L": # "L" é a planta de altitude: Sempre tentar posicionar na linha mais alta possível e, dentro dessa linha, na posição mais à esquerda possível
        linha_horta, coluna_horta = ProcuraPonto(matriz_horta)
                    
                    

        return

# looping 

# leitura
planta_linhas = int(input()) #número de 'linhas' da planta, i.e. tamanho vertical da planta
matriz_planta = [] # matriz que representa o tamanho (as entradas) que a planta ocupa na horta
for linha in range(planta_linhas):
    matriz_planta.append(input()) # recebe as entradas ("." ou "#") do matriz_planta : "." indica uma posição livre e "# indica uma posição ocupada
tipo_planta = str() # recebe o tipo da planta ("P" = planta de solo ou "L" = planta de altitude) 

# processamento


# Impressão da horta
print(matriz_horta)