import random
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez",
"Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",  "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []

def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados aleatoriamente.")

def calcular_sueldo_liquido(sueldo_bruto):
    descuento_salud = sueldo_bruto * 0.07
    descuento_afp = sueldo_bruto * 0.12
    sueldo_liquido = sueldo_bruto - descuento_salud - descuento_afp
    return sueldo_liquido

def clasificar_sueldos():
    global sueldos
    sueldos_ordenados = sorted(sueldos)
    print("Clasificación de sueldos de menor a mayor:")
    for i, sueldo in enumerate(sueldos_ordenados):
        print(f"{i+1}. {sueldo}")

def ver_estadisticas():
    global sueldos
    promedio = sum(sueldos) / len(sueldos)
    minimo = min(sueldos)
    maximo = max(sueldos)
    print(f"Estadísticas de sueldos:")
    print(f"Promedio: ${promedio:.2f}")
    print(f"Mínimo: ${minimo}")
    print(f"Máximo: ${maximo}")

def reporte_sueldos():
    global sueldos, trabajadores
    print("Reporte de sueldos:")
    for i in range(len(trabajadores)):
        sueldo_bruto = sueldos[i]
        sueldo_liquido = calcular_sueldo_liquido(sueldo_bruto)
        print(f"{trabajadores[i]} - Sueldo bruto: ${sueldo_bruto}, Sueldo líquido: ${sueldo_liquido:.2f}")

def main():
    while True:
        print("\nMenú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            asignar_sueldos()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            reporte_sueldos()
        elif opcion == "5":
            print("Saliendo del programa...","desarrollado por Francis moya ","RUT 21.886.861-4")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()




