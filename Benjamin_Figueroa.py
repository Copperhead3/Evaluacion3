import csv
import random
import os
os.system('cls')

def registrar(cliente):
    ide=random
    nombre=input("Ingrese nombre y apellido: ")
    os.system("cls")
    direccion=input("Ingrese la direccion: ")
    os.system("cls")
    comuna=input("Ingrese comuna: ")
    os.system("cls")
    print("Ingrese el detalle del pedido")
    total=0
    while total<1:
        seis=int(input("Cuantos dispensadores de 6 lts. desea: "))
        diez=int(input("Cuantos dispensadores de 10 lts. desea: "))
        veinte=int(input("Cuantos dispensadores de 20 lts. desea: "))
        os.system("cls")
        total=seis+diez+veinte
        if (total<1):
            print("Vuelva a ingresar su pedido por favor")
    cliente={ide,nombre,direccion,comuna,seis,diez,veinte}
    contenido=cliente
    with('contenido.csv','w') as file:
        contenido.write
    return 

def listar_pedidos(cliente):
    print("ID pedido   Cliente   Direccion | Sector     Disp.6lts   Disp.10lts  Disp.20lts")
    print(cliente)

def main():
    while True:
        print("1. Registrar pedido\n2. Listar los todos los pedidos\n3. Imprimir hoja de ruta\n4. Buscar un pedido por ID\n5. Salir del programa")
        choice=int(input())
        os.system("cls")
        cliente={}
        match choice:
            case 1:
                registrar(cliente)
                os.system("cls")
            case 2:
                listar_pedidos(cliente)
                os.system("cls")
            case 5:
                os.system("cls")
                pass
        False
        return

main()
