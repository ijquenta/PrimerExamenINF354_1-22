import csv
import numpy
with open(r'C:\Users\Ivan\Desktop\354\Dataset\vgsales.csv', newline='') as f:
    reader = csv.reader(f)
    tabla = list(reader)


def Enlistar(tabla, num):
    cantidad = len(tabla)
    lista = list()
    for i in range(1, cantidad):
        lista.append(float(tabla[i][num]))  # agregamos cada elemento
    lista.sort() # Ordenando
    return lista



print("CON LIBRERIAS Realice lo mismo del inciso (a) con el uso de numpy y pandas Primer Cuartil - Percentil 90 y 95")
print("--------------------------")
# Ventas en Norte America
list1 = []
print("Ventas de EEUU")
list1 = Enlistar(tabla, 6)
#print(list1)
print("Primer Cuartil:",numpy.quantile(list1, 0.25))
print("Percentil 90:",numpy.percentile(list1, 90))
print("Percentil 95:",numpy.percentile(list1, 95))
print("--------------------------")
# Ventas en Europa
print("Ventas de EUROPA")
list2 = []
list2 = Enlistar(tabla, 7)
#print(list2)
print("Primer Cuartil:",numpy.quantile(list2, 0.25))
print("Percentil 90:",numpy.percentile(list2, 90))
print("Percentil 95:",numpy.percentile(list2, 95))
print("--------------------------")
# Ventas en Japón
print("Ventas de JAPON")
list3 = []
list3 = Enlistar(tabla, 8)
#print(list3)
print("Primer Cuartil:",numpy.quantile(list3, 0.25))
print("Percentil 90:",numpy.percentile(list3, 90))
print("Percentil 95:",numpy.percentile(list3, 95))
print("--------------------------")
# Ventas en Resto del Mundo
print("Ventas de Resto del mundo")
list4 = []
list4 = Enlistar(tabla, 9)
#print(list4)
print("Primer Cuartil:",numpy.quantile(list4, 0.25))
print("Percentil 90:",numpy.percentile(list4, 90))
print("Percentil 95:",numpy.percentile(list4, 95))
print("--------------------------")
# Ventas en Resto del Mundo
print("Ventas Globales")
list5 = []
list5 = Enlistar(tabla, 10)
#print(list5)
print("Primer Cuartil:",numpy.quantile(list5, 0.25))
print("Percentil 90:",numpy.percentile(list5, 90))
print("Percentil 95:",numpy.percentile(list5, 95))
print("--------------------------")


