###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Gestão de Pacientes
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

# Esse sistema deve ser capaz de organiar agendamentos de consultas de uma clínicas


numero_de_semanas = int(input()) # Lê o número de semanas

# Filas de espera
fila_novos = 0
fila_antigos = 0

# Leitura das semanas

for semana in range(1, numero_de_semanas + 1):
    horarios_disponiveis = int(input())  # horários disponíveis
    pacientes_novos = int(input())  # pacientes novos que procuram agendamento
    pacientes_antigos = int(input())  # pacientes antigos que procuram agendamento
    
    # Horários restantes para alocar
    horarios_restantes = horarios_disponiveis
    
    # Pacientes agendados
    novos_agendados = 0
    antigos_agendados = 0

    # Cálculos e impressão da saída por semana

# Ordem de Prioridade:
    # 1° Pacientes em espera (fila_novos)
    # 2° Pacientes em espera (fila_antigos)
    # 3° Novos agendamentos (pacientes_novos)
    # 4° Novos agendamentos (pacientes_antigos)
    
    # Prioridade 1°
    if fila_novos > 0 and horarios_restantes > 0:
        agendados = min(fila_novos, horarios_restantes)
        novos_agendados += agendados
        fila_novos -= agendados
        horarios_restantes -= agendados
    
    # Prioridade 2°
    if fila_antigos > 0 and horarios_restantes > 0:
        agendados = min(fila_antigos, horarios_restantes)
        antigos_agendados += agendados
        fila_antigos -= agendados
        horarios_restantes -= agendados
    
    # Prioridade 3°
    pacientes_novos_restantes = pacientes_novos
    if pacientes_novos_restantes > 0 and horarios_restantes > 0:
        agendados = min(pacientes_novos_restantes, horarios_restantes)
        novos_agendados += agendados
        pacientes_novos_restantes -= agendados
        horarios_restantes -= agendados
    
    # Prioridade 4°
    pacientes_antigos_restantes = pacientes_antigos
    if pacientes_antigos_restantes > 0 and horarios_restantes > 0:
        agendados = min(pacientes_antigos_restantes, horarios_restantes)
        antigos_agendados += agendados
        pacientes_antigos_restantes -= agendados
        horarios_restantes -= agendados
    
    # Atualiza as filas de espera com pacientes não agendados
    fila_novos += pacientes_novos_restantes  # pacientes novos não agendados
    fila_antigos += pacientes_antigos_restantes  # pacientes antigos não agendados
    
    print(f"Semana: {semana}")
    print(f"Pacientes de primeiro atendimento agendados: {novos_agendados}")
    print(f"Pacientes de retorno agendados: {antigos_agendados}")