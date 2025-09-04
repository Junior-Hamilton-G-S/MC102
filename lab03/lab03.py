###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Controle de Reabastecimento de Estoque
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

estoque_atual = int(input())
itens_encomendados = int(input())
tempo_entrega = int(input())
alta_prioridade = input() == "True"
categoria = str(input())
alta_temporada = input() == "True"

# leitura de dados

# Verificação e impressão da atividade

if estoque_atual < 20:
    if alta_prioridade:
        if tempo_entrega <= 5:
            print("Reabastecimento necessário, mas pode aguardar")
        else:
            if alta_temporada or categoria == "Alimentos":
                print("Reabastecimento urgente")
            else:
                print("Reabastecimento necessário, mas pode aguardar")
    else:
        if itens_encomendados < 10:
            print("Reabastecimento urgente, pedidos insuficientes")
        else:
            print("Reabastecimento necessário, mas pode aguardar")

if estoque_atual >= 20 and estoque_atual < 50:
    if alta_prioridade and tempo_entrega > 5:
        print("Reabastecimento urgente")
    else:
        if categoria == "Eletrônicos" or categoria == "Roupas":
            print("Reabastecimento necessário, mas pode aguardar")
        else:
            print("Estoque adequado")

if estoque_atual >= 50 and estoque_atual < 200:
    if itens_encomendados > (0.2 * estoque_atual) and tempo_entrega <= 7:
        if alta_temporada:
            print("Reabastecimento necessário, mas pode aguardar")
        else:
            print("Estoque adequado, mas monitorar pedidos")
    else:
        print("Estoque adequado")

if estoque_atual >= 200:
    if itens_encomendados > 0 and tempo_entrega <= 10:
        print("Excesso de estoque, suspender pedidos futuros")
    else:
        print("Estoque adequado")
