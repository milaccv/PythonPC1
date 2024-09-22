entrada= input("Ingresa las palabras separadas por comas: ")
lista=entrada.split(",")
lista_sin_duplicados = list(set(lista))
print(lista_sin_duplicados)
