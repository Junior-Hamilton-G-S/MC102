###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Gestão de Pacientes
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

numero_de_semanas = int(input()) #Quantidade de Semanas para gendamento
espera_novos = int() #Novos pacientes na fila de espera
espera_antigos = int() #Antigos pacientes na fila de espera

# Leitura das semanas

for semana in range(1, numero_de_semanas + 1):
    horarios_disponiveis = int(input())
    pacientes_novos = int(input())
    pacientes_antigos = int(input())

    # Cálculos e impressão da saída por semana
    
# Ordem de Prioridade:
    # 1° Pacientes em espera (espera_novos)
    # 2° Pacientes em espera (espera_antigos)
    # 3° Novos agendamentos (pacientes_novos)
    # 4° Novos agendamentos (pacientes_antigos)

    if espera_novos > 0 and espera_antigos > 0 and horarios_disponiveis > 0 and horarios_restantes > 0:
        a = min(horarios_disponiveis, espera_novos)
        horarios_restantes = abs(horarios_disponiveis - a)
        if horarios_restantes < a:
            espera_novos = abs(espera_novos + abs(horarios_restantes - a))
            horarios_disponiveis = 0
            horarios_restantes = 0
        else:
            espera_novos = 0
        b = min(horarios_restantes, espera_antigos)
        if horarios_restantes < b:
            espera_antigos = abs(espera_antigos + abs(horarios_restantes - b))
            horarios_disponiveis = 0
            horarios_restantes = 0
        else:
            espera_antigos = 0       

    if espera_novos > 0 and espera_antigos == 0 and horarios_disponiveis > 0 and horarios_restantes > 0:
        a = min(horarios_disponiveis, espera_novos)
        horarios_restantes = abs(horarios_disponiveis - a)
        if horarios_restantes < a:
            espera_novos = abs(espera_novos + abs(horarios_restantes - a))
            horarios_disponiveis = 0
            horarios_restantes = 0
        else:
            espera_novos = 0
        b = min(horarios_restantes, pacientes_novos)
        if horarios_restantes < b:
            espera_novos = abs(espera_novos + abs(horarios_restantes - b))
            horarios_disponiveis = 0
            horarios_restantes = 0
        else:
            espera_novos = 0

    if espera_antigos > 0 and espera_novos == 0 and horarios_disponiveis > 0 and horarios_restantes > 0:
        a = min(horarios_disponiveis, espera_antigos)
        horarios_restantes = abs(horarios_disponiveis - a)
        if horarios_restantes < a:
            espera_antigos = abs(espera_antigos + abs(horarios_restantes - a))
            horarios_disponiveis = 0
            horarios_restantes = 0
        else:
            espera_antigos = 0
        b = min(horarios_restantes, pacientes_novos)
        if horarios_restantes < b:
            espera_novos = abs(espera_novos + abs(horarios_restantes - b))
            horarios_disponiveis = 0
            horarios_restantes = 0
        else:
            espera_novos = 0

    if espera_novos == 0 and espera_antigos == 0 and horarios_disponiveis > 0 and horarios_restantes > 0:
        a = min(horarios_disponiveis, pacientes_novos)
        horarios_restantes = abs(horarios_disponiveis - a)
        if horarios_restantes < a:
            espera_novos = abs(horarios_restantes - a)
        else:
            espera_novos = 0
        b = min(horarios_restantes, pacientes_antigos)
        if horarios_restantes < b:
            espera_antigos = abs(horarios_restantes - b)
            horarios_disponiveis = 0
            horarios_restantes = 0
        else:
            espera_antigos = 0

    retorno = espera_antigos + espera_novos
  
    print('Semana:', semana)
    print('Pacientes de primeiro atendimento agendados:', primeiro_atendimento)
    print('Pacientes de retorno agendados:', retorno)

    
#        pacientes_novos = abs(a + b)
#        horarios_restantes = abs(horarios_restantes - b)
#        retorno = min(horarios_restantes, pacientes_antigos)

#        if horarios_restantes < pacientes_antigos:
#            espera_antigos = abs(espera_antigos + abs(pacientes_antigos - retorno))
#        else:
#            espera_antigos = abs(espera_antigos - retorno)
    
    
#    if espera_antigos > 0:
#        a = min()
#        b = min()
    