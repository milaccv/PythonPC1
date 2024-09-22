entrada= input("Ingresa las palabras separadas por comas: ")
lista=entrada.split(",")
nueva_lista = [lista[i] for i in range(len(lista)) if i not in [0, 4, 5]]
print(nueva_lista)