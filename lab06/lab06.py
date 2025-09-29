###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Alerta Sísmico
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

# Esse programa deve ser capaz de analisar uma sequência de leituras de amplitude do movimento do solo

# Leitura da entrada
lista_numeros = input()
leituras = [float(numero.strip()) for numero in lista_numeros.split(',')]
print(leituras)
tamanho_janela = int(input())
limite = float(input())

# Variáveis para rastrear a maior sequência de alertas
maior_sequencia_tamanho = 0
maior_sequencia_inicio = 0

# Variáveis para rastrear a sequência de alertas atual
sequencia_atual_tamanho = 0
sequencia_atual_inicio = 0

# Análise das janelas deslizantes
numero_de_janelas = len(leituras) - tamanho_janela + 1

for inicio_da_janela in range(numero_de_janelas):
    numero_da_janela = inicio_da_janela + 1
    janela_atual = leituras[inicio_da_janela : inicio_da_janela + tamanho_janela]

    max_leitura = max(janela_atual)
    min_leitura = min(janela_atual)
    oscilacao = abs(max_leitura - min_leitura)

    if oscilacao > limite:
        mensagem = "Janela " + str(numero_da_janela) + ": emitir alerta"
        print(mensagem)
        if sequencia_atual_tamanho == 0:
            sequencia_atual_inicio = numero_da_janela
        sequencia_atual_tamanho += 1
    else:
        mensagem = "Janela " + str(numero_da_janela) + ": normal"
        print(mensagem)
        if sequencia_atual_tamanho > maior_sequencia_tamanho:
            maior_sequencia_tamanho = sequencia_atual_tamanho
            maior_sequencia_inicio = sequencia_atual_inicio
        sequencia_atual_tamanho = 0

if sequencia_atual_tamanho > maior_sequencia_tamanho:
    maior_sequencia_tamanho = sequencia_atual_tamanho
    maior_sequencia_inicio = sequencia_atual_inicio

if maior_sequencia_tamanho > 0:
    maior_sequencia_fim = maior_sequencia_inicio + maior_sequencia_tamanho - 1
    mensagem_final = "Maior sequência de alertas: Janela " + str(maior_sequencia_inicio) + " até Janela " + str(maior_sequencia_fim) + " (tamanho " + str(maior_sequencia_tamanho) + ")"
    print(mensagem_final)
else:
    print("Nenhuma sequência de alertas consecutivos detectada")