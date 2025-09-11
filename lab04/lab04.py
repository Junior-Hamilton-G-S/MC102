# ###################################################
# # MC102 - Algoritmos e Programação de Computadores
# # Laboratório 4 - Aplicativo de Treino
# # Nome: Hamilton Guimarães da Silva Junior
# # RA: 292623
# ###################################################

t = float(input()) #Tempo total disponível para treino (em horas)
T = (t * 60) #Tempo total disponível para treino (em minutos)

treino_pernas = 0
treino_peito = 0
treino_costas = 0
treino_braços = 0
descanso = 0

# Leitura do tempo total



# Sequência de exercícios 

while T > 0 :
    G = input()
    E = float(input()) #tempo de exercicio

    if T >= E:
        if G == "pernas":
            treino_pernas += E
        if G == "peito":
            treino_peito += E
        if G == "costas":
            treino_costas += E
        if G == "bracos":
            treino_braços += E
        if G == "descanso":
            descanso += E
        T -= E  

    else:

        if G == "pernas":
            treino_pernas += T
        if G == "peito":
            treino_peito += T
        if G == "costas":
            treino_costas += T
        if G == "bracos":
            treino_braços += T
        if G == "descanso":
            descanso += T
        T = 0

# Saída do programa

if T == 0:
    print("Resumo do Treino:")
    print("Costas:", format(treino_costas, ".1f").replace(".", ",") + " min")
    print("Pernas:", format(treino_pernas, ".1f").replace(".", ",") + " min")
    print("Peito:", format(treino_peito, ".1f").replace(".", ",") + " min")
    print("Braços:", format(treino_braços, ".1f").replace(".", ",") + " min")