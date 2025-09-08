# ###################################################
# # MC102 - Algoritmos e Programação de Computadores
# # Laboratório 4 - Aplicativo de Treino
# # Nome: Hamilton Guimarães da Silva Junior
# # RA: 292623
# ###################################################

t = (float(input())) #Tempo total disponível para treino (em horas)
T = (t * 60) #Tempo total disponível para treino (em minutos)

treino_pernas = float()
treino_peito = float()
treino_costas = float()
treino_braços = float()
descanso = float()

# Leitura do tempo total

if T < 0
    D -= T
    T -= D
    

# Sequência de exercícios 

while T > 0
    G = str(input())
    E = float(input()) 

    if G == "pernas":
        treino_pernas += E
        T -= E
    if G == "peito":
        treino_peito += E
        T -= E
    if G == "costas":
        treino_costas += E
        T -= E
    if G == "bracos":
        treino_braços += E
        T -= E
    if G == "descanso":
        descanso += E
        T -= E



# Saída do programa

print("Resumo do Treino:")
print("Costas:", format(treino_costas, ".1f").replace(".", ",") + " min")
print("Pernas:", format(treino_pernas, ".1f").replace(".", ",") + " min")
print("Peito:", format(treino_peito, ".1f").replace(".", ",") + " min")
print("Braços:", format(treino_braços, ".1f").replace(".", ",") + " min")