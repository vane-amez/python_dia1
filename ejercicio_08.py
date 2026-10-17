#Solicita una nota de 0 a 100 e indica si el estudiante está aprobado (70 o más) o reprobado. Valida la nota.

nota = int(input("Ingrese su nota (0-100): "))

if nota >= 70:
    print("Aprobado")
elif nota < 70 and nota >= 0:
    print("Reprobado")