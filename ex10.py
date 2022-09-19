# Um exemplo interessante de uso de laços for
# é a busca por um elemento em uma lista:
elemento = 10
estah_presente = False
lista = [1, 2, 7, 10, 15, 20, 50]
for item in lista:
  if item == elemento:
    estah_presente = True

if estah_presente:
  print("Elemento está na lista!")
else:
  print("Elemento não está na lista!")

  