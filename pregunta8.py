hora = input("Ingrese la hora en formato ##:##: ")
horas, minutos = hora.split(":")
horas = float(horas)
minutos = float(minutos) / 60  
hora_float = horas + minutos
if 7 <= hora_float <= 8:
    print("Es la hora del desayuno")
elif 12 <= hora_float <= 13:
        print("Es la hora del almuerzo")
elif 18 <= hora_float <= 19:
        print("Es la hora de la cena")
else:
        print("No es hora de comer")