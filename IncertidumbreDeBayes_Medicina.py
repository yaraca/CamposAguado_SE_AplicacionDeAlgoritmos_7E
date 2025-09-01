#La regla de Bayes es un método probabilístico que permite actualizar la probabilidad de una hipótesis (por ejemplo, estar enfermo) 
# cuando obtenemos nueva evidencia (por ejemplo, resultado positivo en una prueba).
#Este tipo de razonamiento es muy utilizado en sistemas expertos, diagnóstico médico, inteligencia artificial y machine learning.
#Sirve para manejar la incertidumbre en situaciones donde no se tiene información completa.
#Para tomar decisiones más confiables con base en la combinación de datos previos (prevalencia) y evidencia observada (resultado de una prueba).
#Para estimar probabilidades condicionales, es decir, la probabilidad de que ocurra un evento dado que tenemos cierta evidencia.
#El algoritmo bayesiano nos permite actualizar creencias iniciales (prevalencia) con nueva información (prueba positiva), 
# manejando la incertidumbre de manera matemática y fundamentada.

#PROBLEMA: determinar la probabilidad de que una persona esté enferma dado que ha obtenido un resultado positivo en una prueba médica.

#Probabilidades base
P_enfermo = 0.01 # P(E) este es el valor de prevalencia, es decir, la probabilidad de que una persona esté enferma en la población general
P_no_enfermo = 1 - P_enfermo # P(¬E) es el complemento de P(E), es decir, la probabilidad de no estar enfermo

#Sensibilidad y especificidad
P_positivo_dado_enfermo = 0.99 # P(Pos | E) sensibilidad: probabilidad de obtener un resultado positivo si la persona está enferma
P_positivo_dado_no_enfermo = 0.05 # P(Pos | ¬E) tasa de falsos positivos: probabilidad de obtener un resultado positivo si la persona no está enferma

#Probabilidad total de positivo (teorema de la probabilidad total)
P_positivo = (
    P_enfermo * P_positivo_dado_enfermo +
    P_no_enfermo * P_positivo_dado_no_enfermo
) # P(Pos) es la probabilidad total de obtener un resultado positivo, considerando ambos casos (estar enfermo y no estar enfermo)
#la probabilidad total de positivo se calcula sumando la probabilidad de estar enfermo y obtener un positivo,
#más la probabilidad de no estar enfermo y obtener un positivo (falso positivo).

#Regla de Bayes: P(E | Pos) = (P(E) * P(Pos | E)) / P(Pos)
P_enfermo_dado_positivo = (
    P_enfermo * P_positivo_dado_enfermo
) / P_positivo # P(E | Pos) es la probabilidad de estar enfermo dado un resultado positivo
#la probabilidad de estar enfermo dado un resultado positivo se calcula multiplicando la probabilidad de estar enfermo
#por la probabilidad de obtener un positivo si está enfermo, y dividiendo entre la probabilidad total de obtener un positivo.

# Imprimir resultado
print("Probabilidad de estar enfermo dado un resultado positivo:") #imprimimos el resultado
print(f"P(E | Positivo) = {P_enfermo_dado_positivo:.4f}") #mostramos la probabilidad con 4 decimales

#Interpretación del resultado
if P_enfermo_dado_positivo > 0.5: #si la probabilidad de estar enfermo dado un positivo es mayor a 50%
    print("Interpretación: Es más probable que la persona esté enferma.") #interpretamos que es más probable que la persona esté enferma
else: #si no
    print("Interpretación: Es más probable que la persona no esté enferma.") #interpretamos que es más probable que la persona no esté enferma  
#Esto ilustra cómo la regla de Bayes nos ayuda a actualizar nuestras creencias sobre la probabilidad de estar enfermo
#basándonos en la evidencia del resultado de la prueba, manejando la incertidumbre de manera efectiva.