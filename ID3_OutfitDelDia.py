#ID3 es un algoritmo de aprendizaje automático utilizado para crear árboles de decisión a partir de datos etiquetados.
#Se utiliza en clasificación y minería de datos, ayudando a tomar decisiones basadas en atributos de entrada.
#El árbol de decisión resultante puede usarse para predecir la clase de nuevas instancias basándose en sus atributos.

#PROBLEMA: decidir si llevar abrigo a la escuela en la tarde.
#Factores:
#Clima (Soleado, Nublado, Lluvioso)
#Hora (Temprano / Tarde)
#Temperatura (Alta / Baja)
#Resultado: Llevar abrigo o no.

#librerias necesarias
from sklearn import tree #importa la biblioteca sklearn para usar el algoritmo de árbol de decisión
import pandas as pd #importa la biblioteca pandas para manejar datos en formato de tabla

# Datos de ejemplo: Clima, Hora, Temperatura, Abrigo
# 0 = No, 1 = Sí
data = {
    'Clima':     ['Soleado','Soleado','Nublado','Lluvioso','Lluvioso','Nublado','Soleado','Lluvioso'],
    'Hora':      ['Temprano','Tarde','Tarde','Temprano','Tarde','Temprano','Tarde','Tarde'],
    'Temp':      ['Alta','Alta','Baja','Baja','Baja','Alta','Baja','Alta'],
    'Abrigo':    [0, 1, 1, 1, 1, 0, 1, 1]  # 0=No, 1=Sí
} #datos de ejemplo con atributos y la decisión de llevar abrigo o no

# Convertir a DataFrame
df = pd.DataFrame(data) #convierte los datos a un DataFrame de pandas
#los DataFrame son estructuras de datos tabulares similares a hojas de cálculo o tablas SQL

# Variables independientes (X) y dependiente (y)
X = pd.get_dummies(df[['Clima','Hora','Temp']])  #convierte las variables categóricas en variables dummy (0/1)
#la función get_dummies crea columnas binarias para cada categoría en las variables categóricas
#por ejemplo, la columna 'Clima' se convierte en tres columnas: 'Clima_Soleado', 'Clima_Nublado', 'Clima_Lluvioso'
y = df['Abrigo'] #variable dependiente (etiqueta) que indica si se lleva abrigo o no

# Crear y entrenar el modelo ID3 (árbol de decisión)
modelo = tree.DecisionTreeClassifier(criterion='entropy') #crea un clasificador de árbol de decisión usando el criterio de entropía (ID3)
modelo = modelo.fit(X, y) #entrena el modelo con los datos de entrada X y las etiquetas y

# Visualizar el árbol
import matplotlib.pyplot as plt #importa la biblioteca matplotlib para visualización
plt.figure(figsize=(10,6)) #define el tamaño de la figura
tree.plot_tree(modelo, feature_names=X.columns, class_names=["No Abrigo","Sí Abrigo"], filled=True) #dibuja el árbol de decisión con nombres de características y clases
plt.show() #muestra la figura del árbol de decisión

# Ejemplo de predicción:
# Caso: Está nublado, en la tarde, y la temperatura es baja
ejemplo = pd.DataFrame({'Clima_Nublado':[1], 'Clima_Lluvioso':[0], 'Clima_Soleado':[0],
                        'Hora_Tarde':[1], 'Hora_Temprano':[0],
                        'Temp_Alta':[0], 'Temp_Baja':[1]}) #crea un DataFrame para el ejemplo de predicción con las variables dummy correspondientes
#la fila representa las condiciones: Nublado, Tarde, Baja temperatura
# Predecir si llevar abrigo
prediccion = modelo.predict(ejemplo)
print("¿Llevar abrigo?", "Sí" if prediccion[0]==1 else "No") #imprime la predicción de si se debe llevar abrigo o no basado en el modelo entrenado