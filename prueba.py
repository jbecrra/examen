#aleatorio=random.randit(menor,mayor)
import random

sueldos=[]
trabajadores=["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
while True:
    print("MENU DE EMPRESA")
    print("1. SUELDOS ALEATORIOS")
    print("2. CLASIFICAR SUELDOS")
    print("3. VER ESTADISTICA")
    print("4. REPORTE DE SUELDOS")
    print("5. SALIR DEL PROGRAMA")
    opc=int(input("ingrese opcion: "))
    if opc==1:
        for x in range(10):
            aleatorio=random.randint(300000,2500000)
            sueldos.append(aleatorio)
            print(sueldos)
    elif opc==2:
        sueldos.sort
        print(sueldos)
        print(f"sueldo mas alto: {sueldos[-1]}")
        print(f"sueldo mas bajo: {sueldos[0]}")
        print(f"promedio de sueldos: {sum(sueldos)/10}")
    elif opc==3:
        pass
    elif opc==4:
        pass
    else:
        print("adios")
        print("")
