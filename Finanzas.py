        ## DIC
#INGRESOS: TRABAJO, PRESTAMOS, AHORROS,OTROS
#GASTOS: RENTA, SERVICIOS, OCIO, DEVIOLUCION  

Ingresos1 = { "Trabajo": 0, "Prestamos": 0, "Ahorros": 0, "Otros": 0 }
gastos1 = { "Renta": 0, "Servicios": 0, "Ocio": 0, "Devolucion": 0 }

print("Bienvenido a tu control de gastos")

while True:
    control = input("¿Quieres registrar un INGRESO, un GASTO o SALIR?: ").strip().upper()

    if control == "SALIR":
        print("Saliendo del programa...")
        break

    elif control == "INGRESO":
        ANS1 = float(input("¿Cuánto quieres ingresar?: "))
        print("¿De dónde provienen estos ingresos?", list(Ingresos1.keys()))
        Categoria = input("Elige categoría: ").strip().capitalize()

        if Categoria in Ingresos1:
            Ingresos1[Categoria] += ANS1
        else:
            print(" Categoría no válida. Intenta de nuevo.")

    elif control == "GASTO":
        ANS2 = float(input("¿Cuánto quieres debitar?: "))
        print("¿En qué gastaste?", list(gastos1.keys()))
        categoria2 = input("Elige categoría: ").strip().capitalize()

        if categoria2 in gastos1:
            gastos1[categoria2] += ANS2
        else:
            print(" Categoría no válida. Intenta de nuevo.")

    else:
        print(" Opción no válida, intenta de nuevo.")

    # Mostrar saldo cada vez
    total_ingresos = sum(Ingresos1.values())
    total_gastos = sum(gastos1.values())
    saldo = total_ingresos - total_gastos

    print(f"\nSaldo actual: {saldo}")
    print("Resumen de ingresos:", Ingresos1)
    print("Resumen de gastos:", gastos1)
    print("-" * 40)




#### IDEAS 
## LOGRAR QUE EL PROGRAMA GURDE LA CANTIDAD INGRESADA Y DEBITADA Y NOS DE EL RESULTADO FINAL 
# SI EL NUMERO ESTA POR ARRIBA DE CIERTA CANTTIDAD MENSAJE DE PROGRESO 
## SI EL VALOR ES MENOR A CIERTA CABNTIDAD DAR MENSAJE DE ALERTA Y SUGERENCIA 



