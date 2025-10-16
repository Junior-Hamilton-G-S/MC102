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
print("modificador =", modificador)
operacoes = input()


# Alteração do alfabeto (modificador)
def alteracao_do_alfabeto ():
  novo_alfabeto = []
  original = dict.values(alfabeto) 
  print("original =", original)
  novo = list(zip(original, modificador))
  print("novo =", novo)

  for i, j in novo:
    mult = i * j
    print("mult =", mult)
    novo_alfabeto.append(mult)
    print("novo_alfabeto =", novo_alfabeto)
    
  letras = list(dict(alfabeto).keys())
  print("letras =", letras)
  valores = list(novo_alfabeto)
  print("valores =", valores)

  for k, n in letras and valores:
    novo_alfabeto = zip(list({letras : valores}))
    print("novo_alfabeto =", novo_alfabeto)

alteracao_do_alfabeto()


# Processamento das equações


# Saída 