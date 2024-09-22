peso_payaso = 112  # gramos
peso_muneca = 75  
cantidad_payasos = int(input("Ingrese la cantidad de payasos: "))
cantidad_munecas = int(input("Ingrese la cantidad de muñecas: "))
peso_total = (cantidad_payasos * peso_payaso) + (cantidad_munecas * peso_muneca)
print(f"El peso total del paquete es: {peso_total} gramos")