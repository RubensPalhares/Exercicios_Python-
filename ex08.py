# 8) Escreva uma função que recebe como entrada uma lista de números
# e retorna True se um número passado como parâmetro está presente na lista.

def pesquisa_elemento1(numeros, numero_procurado):
    for numero in numeros:
      if numero == numero_procurado:
          return True
    return False

print(pesquisa_elemento1([1, 10, 20, 30, 50, 100], 30))