calificacion = float(input("Ingrese la calificación: "))
if calificacion >= 8 and calificacion <= 10:
    print("Aprobado")
elif 5 <= calificacion < 8:
    print("Regular")
elif 1 <= calificacion < 5:
    print("Reprobado")
else:
    print("Calificación no válida")