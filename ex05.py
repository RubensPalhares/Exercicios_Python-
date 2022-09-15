# Escreva uma função que recebe dois números (a e b) como parâmetro
# e retorna a quantidade (0, 1 ou 2) deles que é maior que um 
# terceiro parâmetro, chamado limite.

def num_parametros_maior_que_limite(a, b, limite):
    if a > limite and b > limite:
      return 2
    elif a > limite or b > limite:
      return 1
    else:
      return 0

print(num_parametros_maior_que_limite(50, 7, 30))