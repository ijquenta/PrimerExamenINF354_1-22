    
import pandas as pd
from sklearn import preprocessing
import numpy
    
df = pd.read_csv (r'C:\Users\Ivan\Desktop\354\Dataset\vgsales.csv', skiprows=0, low_memory=False)
numpy.set_printoptions(precision=4, suppress=True)
df= df.dropna(thresh=len(df.index)/2,axis=1) 
# dropna: elimina filas que contiene valores NULL
# thresh: num de valores NULL necesarios para eliminar la fila
# axis: elimina columnas que contienen valores NULL

#Seleccionamos las 10 primeras filas de las Columnas NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales
x = df.iloc[:,6:24].values # especificamos la fila y columna
y = df.iloc[:, 5].values # especificamos la fila y columna

print("------------------------------------------------------------------------")    
print('Datos iniciales:')
print('Se imprimen las 20 primeras filas de Ventas de Norte America, Europa, Japon, Otros Paises y el Global\n')
print(x[0:20,:]) # Mostramos las 20 primeras filas de datos
print("------------------------------------------------------------------------")    
scale = preprocessing.StandardScaler().fit(x)
scaler = scale.transform(x)
print('\nDatos Estadarizados-StandardScaler():\nEstandarización:  o eliminación de medias y escalado de varianza\n', scaler[0:20,:],'\n\nSum:', scaler[0:20,:].sum(axis=0),'\nMedias:', scaler[0:20,:].mean(axis=0),'\nDesviación estandar:', scaler[0:10,:].std(axis=0))
print("------------------------------------------------------------------------")    
print("\nEscalar datos a un rango(0,100)-MinMaxScaler():")
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 100)) # rango desiado de datos transformados
X_train_minmax = min_max_scaler.fit_transform(x)
print(X_train_minmax[0:20,:])
print("------------------------------------------------------------------------")    
print("\nNormalizar los datos-Normalizer():")
escalador = preprocessing.Normalizer().fit(x)
normalizedX = escalador.transform(x)
print(normalizedX[0:20,:])
