def processar_agendamento():
    # Lê o número de semanas
    n = int(input())
    
    # Inicializa as filas de espera (vazias na primeira semana)
    fila_primeiro_atendimento = 0
    fila_retorno = 0
    
    # Processa cada semana
    for semana in range(1, n + 1):
        # Lê os dados da semana atual
        h = int(input())  # horários disponíveis
        p = int(input())  # pacientes novos que procuram agendamento
        r = int(input())  # pacientes de retorno que procuram agendamento
        
        # Horários restantes para alocar
        horarios_restantes = h
        
        # Contadores de pacientes agendados
        primeiro_atendimento_agendados = 0
        retorno_agendados = 0
        
        # PRIORIDADE 1: Pacientes de primeiro atendimento da fila de espera
        if fila_primeiro_atendimento > 0 and horarios_restantes > 0:
            agendados = min(fila_primeiro_atendimento, horarios_restantes)
            primeiro_atendimento_agendados += agendados
            fila_primeiro_atendimento -= agendados
            horarios_restantes -= agendados
        
        # PRIORIDADE 2: Pacientes de retorno da fila de espera
        if fila_retorno > 0 and horarios_restantes > 0:
            agendados = min(fila_retorno, horarios_restantes)
            retorno_agendados += agendados
            fila_retorno -= agendados
            horarios_restantes -= agendados
        
        # PRIORIDADE 3: Pacientes de primeiro atendimento da semana atual
        pacientes_novos_restantes = p
        if pacientes_novos_restantes > 0 and horarios_restantes > 0:
            agendados = min(pacientes_novos_restantes, horarios_restantes)
            primeiro_atendimento_agendados += agendados
            pacientes_novos_restantes -= agendados
            horarios_restantes -= agendados
        
        # PRIORIDADE 4: Pacientes de retorno da semana atual
        pacientes_retorno_restantes = r
        if pacientes_retorno_restantes > 0 and horarios_restantes > 0:
            agendados = min(pacientes_retorno_restantes, horarios_restantes)
            retorno_agendados += agendados
            pacientes_retorno_restantes -= agendados
            horarios_restantes -= agendados
        
        # Atualiza as filas de espera com pacientes não agendados
        fila_primeiro_atendimento += pacientes_novos_restantes  # pacientes novos não agendados
        fila_retorno += pacientes_retorno_restantes  # pacientes de retorno não agendados
        
        # Exibe o resultado da semana
        print(f"Semana: {semana}")
        print(f"Pacientes de primeiro atendimento agendados: {primeiro_atendimento_agendados}")
        print(f"Pacientes de retorno agendados: {retorno_agendados}")

# Executa o sistema
processar_agendamento()