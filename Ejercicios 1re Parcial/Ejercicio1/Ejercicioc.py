# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 18:00:18 2021
@author: hp
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv (r'C:\Users\Ivan\Desktop\354\Dataset\vgsales.csv')

pd.options.display.max_rows = 30
print('30 juegos mas vendidos'.center(50,' '))
print(df['Name'][:30])


x_values = df['Name']


# Ventas de Juegos Global
plt.title('Ventas de VideoJuegos:\n Los 30 más vendidos GLOBALMENTE')
plt.xlabel('Titulo del VideoJuego')
plt.ylabel("Juegos Vendidos (millones)")
y_values = df['Global_Sales']
plt.bar(x_values, y_values)
plt.xticks(x_values, rotation='vertical')
plt.xlim(0, 30)
plt.ylim(0, 85)
plt.show()


# Ventas de Juegos Norte America
plt.title('Ventas de VideoJuegos:\n Los 30 más vendidos en NORTE AMERICA')
plt.xlabel('Titulo del VideoJuego')
plt.ylabel("Juegos Vendidos (millones)")
y_values = df['NA_Sales']
plt.bar(x_values, y_values)
plt.xticks(x_values, rotation='vertical')
plt.xlim(0, 30)
plt.ylim(0, 45)
plt.show()


# Ventas de Juegos Europa
plt.title('Ventas de VideoJuegos:\n Los 30 más vendidos en EUROPA')
plt.xlabel('Titulo del VideoJuego')
plt.ylabel("Juegos Vendidos (millones)")
y_values = df['EU_Sales']
plt.bar(x_values, y_values)
plt.xticks(x_values, rotation='vertical')
plt.xlim(0, 30)
plt.ylim(0, 30)
plt.show()


# Ventas de Juegos Japon
plt.title('Ventas de VideoJuegos:\n Los 30 más vendidos en JAPON')
plt.xlabel('Titulo del VideoJuego')
plt.ylabel("Juegos Vendidos (millones)")
y_values = df['JP_Sales']
plt.bar(x_values, y_values)
plt.xticks(x_values, rotation='vertical')
plt.xlim(0, 30)
plt.ylim(0, 12)
plt.show()



# Ventas de Juegos Resto del Mundo
plt.title('Ventas de VideoJuegos:\n Los 30 más vendidos en el RESTO DEL MUNDO')
plt.xlabel('Titulo del VideoJuego')
plt.ylabel("Juegos Vendidos (millones)")
y_values = df['Other_Sales']
plt.bar(x_values, y_values)
plt.xticks(x_values, rotation='vertical')
plt.xlim(0, 30)
plt.ylim(0, 12)
plt.show()

