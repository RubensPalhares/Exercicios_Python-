#1) Escreva uma função que recebe dois parâmetros e imprime o menor dos dois.
# Se eles forem iguais, imprima que eles são iguais.

def imprime_menor(a, b):
    if a < b:
      print(a)
    elif a > b:
      print(b)
    else:
      print("Os números são iguais.")
      
imprime_menor(0, 5)
imprime_menor(10, 3)
imprime_menor(42, 42)