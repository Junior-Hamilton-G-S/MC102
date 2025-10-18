###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 09 - Senhas Codificadas
# Nome: Hamilton Guimarães da Silva Junior
# RA: 292623
###################################################

#Esse programa deve ser capaz de atribuir valores as letras do alfabeto (cíclico) e realizar operações entre as letras de mesma posição das palavras

# Alfabeto cíclico
alfabeto = {
  'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 1,
  'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9, 's': 1,
  't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8
}

# Leitura de entradas
N = input() #Número de operações a serem processadas;
modificador = list(map(int, input().split())) #0 ou 1 (0 => valor_letra = 0; 1 => valor_letra = alfabeto)

# Alteração do alfabeto (modificador)
def alteracao_do_alfabeto (alfabeto, modificador):
  novo_alfabeto = []
  valores_originais = dict.values(alfabeto)
  combina_valor = list(zip(valores_originais, modificador))

  for i, j in combina_valor:
    mult = i * j
    novo_alfabeto.append(mult)
    
  letras = list(dict(alfabeto).keys())
  novos_valores = list(novo_alfabeto)

  novo_alfabeto = dict(zip(letras, novos_valores))
  return novo_alfabeto

novo_alfabeto = alteracao_do_alfabeto(alfabeto, modificador)

# Processamento das equações:
def valor_palavra (palavra):
  valor_palavra = ""
  palavra = palavra.lower()
  
  for letra in palavra:
    valor_letra = novo_alfabeto[letra]
    valor_palavra += str(valor_letra)

  return int(valor_palavra)

def operacao (valor, simbolo, a):
  if simbolo == '+':
    return valor + valor_palavra(a)
  elif simbolo == '-':
    return valor - valor_palavra(a)

# Saída
for string in range(1, int(N) + 1):
  operacoes = input()
  string = operacoes.split(' ')
  valor = valor_palavra(string[0])

  for i in range(1, len(string), 2):
    if i + 1 <= len(string):
      valor = operacao(valor, string[i], string[i + 1])

  print(valor)