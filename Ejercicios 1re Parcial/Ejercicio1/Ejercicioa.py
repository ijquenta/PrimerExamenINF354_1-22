import csv
import numpy
with open(r'C:\Users\Ivan\Desktop\354\Dataset\vgsales.csv', newline='') as f:
    reader = csv.reader(f)
    tabla = list(reader)


def PrimerCuartil(tabla, num):
    cantidad = len(tabla)
    lista = list()
    for i in range(1, cantidad):
        lista.append(float(tabla[i][num]))  # agregamos cada elemento
    #print("Tabla No Ordenada - ")
    #print(lista)
    lista.sort() # Ordenando
    #print("Tabla Ordenada - ")
    #print(lista)
    if cantidad % 2 == 1: # verificar si la cantidad de la lista es Impar o Par
        #print("Es Impar", cantidad)
        posicionA = int(1 * (cantidad + 1) / 4)
        #print("Posición:", posicionA)
        print("Primer Cuartil:", lista[int(posicionA) - 1])
    else:
        #print("Es par")
        posicionB = 1 * cantidad / 4
        #print("Posición")
        print("Primer Cuartil Par", lista[int(posicionB) - 1])
    pass

def Percentil(tabla, num1, num2):
    cantidad = len(tabla)
    lista = list()
    for i in range(1, cantidad):
        lista.append(float(tabla[i][num1]))  # agregamos cada elemento
    #print("Tabla No Ordenada - ")
    #print(lista)
    lista.sort() # Ordenando
    #print("Tabla Ordenada - ")
    #print(lista)
    i = (num2 / 100) * cantidad
    #print("indice", i)
    mod = i % 10
    #print("mod", mod)
    if isinstance(i, int):
        #print("no es entero, se va a la siguiente posición")
        pos1 = int(i) + 1
        #print("Poscion ->", pos1)
        print("Percentil",num2,"->", lista[pos1])
    else:
        #print("es entero")
        #print(cantidad)
        posa = int(i)
        posb = posa + 1
        #print("Poscición", (posa + posb) / 2)
        print("Percentil",num2,"->", (lista[posa - 1] + lista[posb - 1]) / 2)
    pass

print("SIN LIBRERIAS El calculo del 1er cuartil de datos, el percentil 90, 95 por columna; explique qué significa en cada caso mediante Python sin uso de librerías")
print("Primer Cuartil - Percentil 90 y 95")
print("--------------------------")
# Ventas en Norte America
print("Ventas de EEUU")
PrimerCuartil(tabla, 6)
Percentil(tabla, 6 ,90)
Percentil(tabla, 6 ,95)
print("--------------------------")
# Ventas en Europa
print("Ventas de EUROPA")
PrimerCuartil(tabla, 7)
Percentil(tabla, 7 ,90)
Percentil(tabla, 7 ,95)
print("--------------------------")
# Ventas en Japón
print("Ventas de JAPON")
PrimerCuartil(tabla, 8)
Percentil(tabla, 8 ,90)
Percentil(tabla, 8 ,95)
print("--------------------------")
# Ventas en Resto del Mundo
print("Ventas de Resto del mundo")
PrimerCuartil(tabla, 9)
Percentil(tabla, 9 ,90)
Percentil(tabla, 9 ,95)
print("--------------------------")
# Ventas en Resto del Mundo
print("Ventas Globales")
PrimerCuartil(tabla, 10)
Percentil(tabla, 10 ,90)
Percentil(tabla, 10 ,95)
print("--------------------------")


