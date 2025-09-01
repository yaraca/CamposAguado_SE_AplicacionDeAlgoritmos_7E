#Red Bayesiana 
#Es un modelo probabilistico grafico que representa un conjunto de variables aleatorias y sus relaciones condicionales mediante un grafo dirigido acíclico (DAG). 
#se compone de nodos (variables aleatorias), aristas dirigidas (dependencias condicionales), tablas de probabilidad condicional (CPT, cada nodo tiene una tabla que describe la probabilidad condicional dado sus padres en el grado) 
#Este permite la inferencia probabilistica eficiente (cuál es la probabilidad de X dado Y) 
#Permiten aprender la estructura y los parámetros de los datos #se pueden usar para tomar decisiones bajo incertidumbre 
#se puede aplicar en el diagnostico médico, reconocimiento de patrones, prediccion y clasificación, inteligencia artificial, etc.

#PROBLEMA: predecir el clima de mañana (Soleado o Lluvioso) basado en el clima de hoy y la cantidad de nubes observada.

#librerias necesarias
import random #para simular datos aleatorios

#estados posibles
weather_states = ["Soleado", "Lluvioso"] 

#probabilidad inicial P(Weather_0)
P_Weather_0 = {
    "Soleado": 0.7,
    "Lluvioso": 0.3
} #esta es la probabilidad de que hoy sea soleado o lluvioso

#probabilidad de transición P(Weather_t+1 | Weather_t)
P_Weather_next_given_current = {
    "Soleado": {"Soleado": 0.8, "Lluvioso": 0.2},
    "Lluvioso": {"Soleado": 0.3, "Lluvioso": 0.7}
} #si hoy es soleado, hay 80% de probabilidad de que mañana sea soleado y 20% de que sea lluvioso. Si hoy es lluvioso, hay 30% de probabilidad de que mañana sea soleado y 70% de que sea lluvioso.

#función de inferencia: combina transición + observación (nubes)
def inference_weather(previous_state, nubes): #función que toma el estado anterior y la cantidad de nubes observada
    """
    previous_state: estado anterior del clima (Soleado o Lluvioso)
    nubes: valor de 0 a 100 (0 = despejado, 100 = muy nublado)
    """ #nubes es un valor entre 0 y 100 que representa la cantidad de nubes observada hoy
    #Probabilidad basada en observación
    prob_lluvia_obs = nubes / 100 #si nubes es 0, prob_lluvia_obs es 0 (despejado). Si nubes es 100, prob_lluvia_obs es 1 (muy nublado)
    prob_soleado_obs = 1 - prob_lluvia_obs #complemento de prob_lluvia_obs 

    #Probabilidad de transición según el estado previo
    trans_probs = P_Weather_next_given_current[previous_state] #obtenemos las probabilidades de transición según el estado previo
    

    #Combinar transición y observación (multiplicamos)
    probs = {
        "Soleado": trans_probs["Soleado"] * prob_soleado_obs, #multiplicamos la probabilidad de transición por la probabilidad basada en la observación
        "Lluvioso": trans_probs["Lluvioso"] * prob_lluvia_obs #multiplicamos la probabilidad de transición por la probabilidad basada en la observación
    }

    #Normalizar para que sumen 1
    total = sum(probs.values()) #sumamos las probabilidades
    probs = {k: v / total for k, v in probs.items()} #normalizamos las probabilidades dividiendo cada probabilidad por el total

    return probs #devolvemos las probabilidades normalizadas

#Ejemplo de uso

#Simular la cantidad de nubes
cantidad_nubes = random.randint(0, 100) #simulamos un valor aleatorio entre 0 y 100 para la cantidad de nubes
#random.randint(a, b) devuelve un entero aleatorio N tal que a <= N <= b
print(f"Cantidad de nubes observada: {cantidad_nubes}%")  #imprimimos la cantidad de nubes observada

#Suponemos estado inicial según P(Weather_0)
estado_inicial = random.choices( #elegimos un estado inicial según las probabilidades iniciales
    population=list(P_Weather_0.keys()), #los estados posibles
    weights=list(P_Weather_0.values()) #las probabilidades asociadas a cada estado
)[0] #elegimos un estado inicial aleatoriamente según las probabilidades iniciales
print(f" Estado inicial del clima: {estado_inicial}") #imprimimos el estado inicial del clima

#Ejecutamos inferencia para el siguiente estado
resultado = inference_weather(estado_inicial, cantidad_nubes) #llamamos a la función de inferencia con el estado inicial y la cantidad de nubes observada
#la inferencia es la probabilidad estimada del clima para mañana dado el clima de hoy y la cantidad de nubes observada

# Mostrar probabilidades resultantes
print("\n Probabilidad estimada del clima para mañana:") #imprimimos las probabilidades resultantes
for estado, prob in resultado.items(): #iteramos sobre las probabilidades resultantes
    print(f"{estado}: {prob:.2f}") #imprimimos cada estado y su probabilidad con 2 decimales

# Recomendación
if resultado["Lluvioso"] > 0.5: #si la probabilidad de que mañana sea lluvioso es mayor a 50%
    print("\n Recomendación: Lleva ropa para lluvia.") #recomendamos llevar ropa para lluvia
else: #si no
    print("\n Recomendación: No es necesario llevar ropa para lluvia.") #recomendamos no llevar ropa para lluvia