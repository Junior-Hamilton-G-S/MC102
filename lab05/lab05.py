###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Gestão de Pacientes
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

numero_de_semanas = int(input())
retornos_pendentes = 0

# Leitura das semanas

for semana_atual in range(1, numero_de_semanas + 1):
    horarios_disponiveis = int(input())
    primeiros_atendimentos = int(input())
    retornos = int(input())

    # Cálculos e impressão da saída por semana
    
    primeiros_agendados = min(primeiros_atendimentos, horarios_disponiveis)
    horarios_restantes = horarios_disponiveis - primeiros_agendados

    total_retornos_a_agendar = retornos + retornos_pendentes
    retornos_agendados = min(total_retornos_a_agendar, horarios_restantes)

    retornos_pendentes = total_retornos_a_agendar - retornos_agendados

  
    print('Semana:', semana_atual)
    print('Pacientes de primeiro atendimento agendados:', primeiros_agendados)
    print('Pacientes de retorno agendados:', retornos_agendados)