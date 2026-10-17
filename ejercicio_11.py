# Solicita una temperatura y clasifícala: Menos de 10 °C: frío. De 10 a menos de 25 °C: templado. De 25 a menos de 35 °C: caluroso. 35 °C o más: muy caluroso.

temperatura = input("Ingrese la temperatura en grados Celsius: ")

if temperatura <= "10":  
    print("Hace frio")
elif temperatura > "10" and temperatura <= "25":
    print("Templado")
elif temperatura > "25" and temperatura <= "35":
    print("Caluroso")  
elif temperatura > "35":    
    print("Muy caluroso")
    