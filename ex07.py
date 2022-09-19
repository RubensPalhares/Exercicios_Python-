# 7) Escreva uma função que, dado um número nota representando 
# a nota de um estudante, converte o valor de nota para um 
# conceito (A, B, C, D, E e F).

def converte_nota_em_conceito(nota):
    if nota >= 60:
      return "A"
    elif nota >= 80:
      return "B"
    elif nota >= 70:
      return "C"
    elif nota >= 60:
      return "D"
    elif nota >= 40:
      return "E"
    else:
      return "F"

print(converte_nota_em_conceito(65))