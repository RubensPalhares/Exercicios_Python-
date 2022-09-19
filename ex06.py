# Escreva uma função que recebe um número como parâmetro e para
# cada número menor que o parâmetro, a função imprime "MENOR" 
# se o número for múltiplo de três, imprime "MULTIPLO" se o número 
# for múltiplo de cinco, e imprime "MULTIPLO 5" se o número for
#  múltiplo de três e cinco. Caso o número não seja múltiplo 
# nem de três nem de cinco, ele deve ser impresso. Note que, 
# ao contrário das funções anteriores, sua função não deve retornar nada. 
# Ela precisa simplesmente imprimir o que foi pedido.
def fizz_buzz(n):
    for num in range(n):
        if num % 3 == 0 and num % 5 == 0:
            print('MULTIPLO 5')
        elif num % 3 == 0:
            print('MENOR')
        elif num % 5 == 0:
            print('MULTIPLO')
        else:
            print(num)

print(fizz_buzz(16))