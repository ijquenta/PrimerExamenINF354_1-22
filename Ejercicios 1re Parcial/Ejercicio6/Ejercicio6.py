import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\Ivan\Documents\Ejercicio6\tic-tac-toe-endgame.csv')
data.head()
print(data.head())
data.isnull().sum()
for i in data.columns:
  print(data[i].value_counts())
  print()
print(data.columns)
#Para convertir datos categóricos en datos numéricos Podemos usar cualquier uso pandas.get_dummies() or sklearn.preprocessing.OneHotEncoder()
x_num = pd.get_dummies(data[['V1','V2','V3','V4','V5','V6','V7','V8','V9']],drop_first = True)

data.replace('negative',0,inplace=True)
data.replace('positive',1,inplace=True)

x_num.columns

y = data.iloc[:,9].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_num,y,test_size = 0.33, random_state = 42)
# Escalado de características: para escalar los valores, de lo contrario, la computadora considera los valores más altos como los más grandes y los valores más bajos como los más pequeños sin considerar su unidad
from sklearn.preprocessing import StandardScaler
st = StandardScaler()
x_train = st.fit_transform(x_train)
x_test = st.fit_transform(x_test)
#Ajuste del árbol de decisión al conjunto de datos de entrenamiento
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state =  42)
classifier.fit(x_train,y_train)

y_pred= classifier.predict(x_test)
print(y_pred)
#Matriz de confusión
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)

#Predicciones incorrectas
incorrect_pred = (y_test != y_pred).sum()
print(incorrect_pred)

#Puntuación de precisión
from sklearn import metrics
from sklearn.metrics import classification_report
print(metrics.accuracy_score(y_test,y_pred))

#Informe de clasificación
print(classification_report(y_test, y_pred))

import matplotlib.pyplot as plt
from sklearn import tree
plt.figure(figsize=(50,30))
tree.plot_tree(classifier,filled=True)
plt.show()

#Conclusión: Por lo tanto, hemos aplicado el Algoritmo del Árbol de Decisión en Tic Tac Toe Endgame y obtuvimos una precisión del 95%