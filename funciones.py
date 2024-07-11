
import random
sueldos=[]
trabajadores=["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def media_geometrica():
    for x in range(10):
        media=sueldos[x]*sueldos[x]
        print(media)
def opc_1():
    for x in range(10):
            aleatorio=random.randint(300000,2500000)
            sueldos.append(aleatorio)
            print(sueldos)

def opc_3():
    sueldos.sort
    print(sueldos)
    print(f"sueldo mas alto: {sueldos[-1]}")
    print(f"sueldo mas bajo: {sueldos[0]}")
    print(f"promedio de sueldos: {sum(sueldos)/10}")

def opc_4():
     for x in range(10):
            print("nombre del empleado\t\tsueldo base\tdescuento salud\t\tdescuento AFP\t\tsueldo liquido")
            print(f"{trabajadores[x]}\t\t\t{sueldos[x]}\t\t{sueldos[x]/0.3}\t{sueldos[x]/0.88}\t\t{sueldos[x]/0.3-sueldos[x]/0.88-sueldos[x]}")