import os
import time
from funciones import*

while True:
    os.system('cls')
    print("MENU DE EMPRESA")
    print("1. SUELDOS ALEATORIOS")
    print("2. CLASIFICAR SUELDOS")
    print("3. VER ESTADISTICA")
    print("4. REPORTE DE SUELDOS")
    print("5. SALIR DEL PROGRAMA")
    opc=int(input("ingrese opcion: "))
    if opc==1:
        os.system('cls')
        opc_1()
    elif opc==2:
        os.system('cls')
        print("sueldos menores a $800000 total",)
    elif opc==3:
        os.system('cls')
        opc_3()
        media_geometrica()
    elif opc==4:
        os.system('cls')
        opc_4()
    else:    
        print("adios")
        break
    time.sleep(3)