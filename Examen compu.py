Tarifa_base = 5.00
Tarifa_por_km = 2.50
Tarifa_por_minuto = 0.50
Recargo = 0
print("Bienvenid@ al Cálculo de tarifa de viaje en Uber Guatemala")
Tarifa_por_km = float(input("Ingrese los km recorridos: "))
if Tarifa_por_km >= 21:
     print("limite de la aplicacion excedido por favor reinicie")

if Tarifa_por_km == 1:
    print("la tarifa por km es de 2.50")
elif Tarifa_por_km == 2:
    print("la tarifa por km es de Q5")
elif Tarifa_por_km ==3:
    print("la tarifa por km es de Q7.50")
elif Tarifa_por_km == 4:
    print("la tarifa por km es de Q10")
elif Tarifa_por_km == 5:
    print("la tarifa por km es de Q12.50")
elif Tarifa_por_km == 6:
    print("la tarifa por km es de Q15")
elif Tarifa_por_km == 7:
    print("la tarifa por km es de Q17.5")
elif Tarifa_por_km == 8:
    print("la tarifa por km es de Q20")
elif Tarifa_por_km == 9:
    print("la tarifa por km es de Q22.5")
elif Tarifa_por_km == 10:
    print("la tarifa por km es de Q25")
if Tarifa_por_km == 11:
    print("la tarifa por km es de Q27.5")
elif Tarifa_por_km == 12:
    print("la tarifa por km es de Q30")
elif Tarifa_por_km ==13:
    print("la tarifa por km es de Q32.5")
elif Tarifa_por_km == 14:
    print("la tarifa por km es de Q35")
elif Tarifa_por_km == 15:
    print("la tarifa por km es de Q37.5")
elif Tarifa_por_km == 16:
    print("la tarifa por km es de Q40")
elif Tarifa_por_km == 17:
    print("la tarifa por km es de Q42.5")
elif Tarifa_por_km == 18:
    print("la tarifa por km es de Q45")
elif Tarifa_por_km == 19:
    print("la tarifa por km es de Q47.5")
elif Tarifa_por_km == 20:
    print("la tarifa por km es de Q50")

Tarifa_por_minuto = float(input("ingrese los minutos que tomo llegar al destino: "))
if Tarifa_por_minuto >= 31:
    print("los minutos se sales del limite establecido por la aplicacion")

if Tarifa_por_minuto == 1:
    print("la tarifa por min es de 0.50")
elif Tarifa_por_minuto ==2:
    print("l  a tarifa por min es igual a 1")
elif Tarifa_por_minuto == 3:
    print("la tarifa por min es de 1.50")
elif Tarifa_por_minuto == 4:
    print("la tarifa por min es de 2")
elif Tarifa_por_minuto == 5:
    print("la tarifa por min es de 2.50")
elif Tarifa_por_minuto == 6:
    print("la tarifa por min es de 3")
elif Tarifa_por_minuto == 7:
    print("la tarifa por min es de 3.50")
elif Tarifa_por_minuto == 8:
    print("la tarifa por min es de 4")
elif Tarifa_por_minuto == 9:
    print("la tarifa por min es de 4.50")
elif Tarifa_por_minuto == 10:
    print("la tarifa por min es de 5")
elif Tarifa_por_minuto == 11:
    print("la tarifa por min es de 5.50")
elif Tarifa_por_minuto ==12:
    print("l  a tarifa por min es igual a 6")
elif Tarifa_por_minuto == 13:
    print("la tarifa por min es de 6.50")
elif Tarifa_por_minuto == 14:
    print("la tarifa por min es de 7")
elif Tarifa_por_minuto == 15:
    print("la tarifa por min es de 7.50")
elif Tarifa_por_minuto == 16:
    print("la tarifa por min es de 8")
elif Tarifa_por_minuto == 17:
    print("la tarifa por min es de 8.50")
elif Tarifa_por_minuto == 18:
    print("la tarifa por min es de 9")
elif Tarifa_por_minuto == 19:
    print("la tarifa por min es de 9.50")
elif Tarifa_por_minuto == 20:
    print("la tarifa por min es de 10")
elif Tarifa_por_minuto == 21:
    print("la tarifa por min es de 10.50")
elif Tarifa_por_minuto ==22:
    print("l  a tarifa por min es igual a 11")
elif Tarifa_por_minuto == 23:
    print("la tarifa por min es de 11.50")
elif Tarifa_por_minuto == 24:
    print("la tarifa por min es de 12")
elif Tarifa_por_minuto == 25:
    print("la tarifa por min es de 12.50")
elif Tarifa_por_minuto == 26:
    print("la tarifa por min es de 13")
elif Tarifa_por_minuto == 27:
    print("la tarifa por min es de 13.50")
elif Tarifa_por_minuto == 28:
    print("la tarifa por min es de 14")
elif Tarifa_por_minuto == 29:
    print("la tarifa por min es de 14.50")
elif Tarifa_por_minuto == 30:
    print("la tarifa por min es de 15")

tarifa_total = Tarifa_base * Tarifa_por_minuto * Tarifa_por_km

Recargo = float(input("ingrese la hora del recorrido: "))
tarifa_con_horas = tarifa_total * 20
if Recargo == 7 or 9:
    tarifa_total * 20
    print(tarifa_con_horas)