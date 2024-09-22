num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Opciones: ")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    print(f"El resultado de la suma es: {num1 + num2}")
elif opcion == 2:
    print(f"El resultado de la resta es: {num1 - num2}")
elif opcion == 3:
    print(f"El resultado de la multiplicación es: {num1 * num2}")
else:
    print("Opción no válida")