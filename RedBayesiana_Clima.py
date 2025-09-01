#Red Bayesiana 
#Es un modelo probabilistico grafico que representa un conjunto de variables aleatorias y sus relaciones condicionales mediante un grafo dirigido acíclico (DAG). 
#se compone de nodos (variables aleatorias), aristas dirigidas (dependencias condicionales), tablas de probabilidad condicional (CPT, cada nodo tiene una tabla que describe la probabilidad condicional dado sus padres en el grado) 
#Este permite la inferencia probabilistica eficiente (cuál es la probabilidad de X dado Y) 
#Permiten aprender la estructura y los parámetros de los datos #se pueden usar para tomar decisiones bajo incertidumbre 
#se puede aplicar en el diagnostico médico, reconocimiento de patrones, prediccion y clasificación, inteligencia artificial, etc.


import random

# Estados posibles
weather_states = ["Soleado", "Lluvioso"]

# Probabilidad inicial P(Weather_0)
P_Weather_0 = {
    "Soleado": 0.7,
    "Lluvioso": 0.3
}

# Probabilidad de transición P(Weather_t+1 | Weather_t)
P_Weather_next_given_current = {
    "Soleado": {"Soleado": 0.8, "Lluvioso": 0.2},
    "Lluvioso": {"Soleado": 0.3, "Lluvioso": 0.7}
}

# Función de inferencia: combina transición + observación (nubes)
def inference_weather(previous_state, nubes):
    """
    previous_state: estado anterior del clima (Soleado o Lluvioso)
    nubes: valor de 0 a 100 (0 = despejado, 100 = muy nublado)
    """
    # Probabilidad basada en observación
    prob_lluvia_obs = nubes / 100
    prob_soleado_obs = 1 - prob_lluvia_obs

    # Probabilidad de transición según el estado previo
    trans_probs = P_Weather_next_given_current[previous_state]

    # Combinar transición y observación (multiplicamos)
    probs = {
        "Soleado": trans_probs["Soleado"] * prob_soleado_obs,
        "Lluvioso": trans_probs["Lluvioso"] * prob_lluvia_obs
    }

    # Normalizar para que sumen 1
    total = sum(probs.values())
    probs = {k: v / total for k, v in probs.items()}

    return probs

# ----------------- SIMULACIÓN -----------------

# Simulamos la cantidad de nubes
cantidad_nubes = random.randint(0, 100)
print(f"Cantidad de nubes observada: {cantidad_nubes}%")

# Suponemos estado inicial según P(Weather_0)
estado_inicial = random.choices(
    population=list(P_Weather_0.keys()),
    weights=list(P_Weather_0.values())
)[0]
print(f" Estado inicial del clima: {estado_inicial}")

# Ejecutamos inferencia para el siguiente estado
resultado = inference_weather(estado_inicial, cantidad_nubes)

# Mostrar probabilidades resultantes
print("\n Probabilidad estimada del clima para mañana:")
for estado, prob in resultado.items():
    print(f"{estado}: {prob:.2f}")

# Recomendación
if resultado["Lluvioso"] > 0.5:
    print("\n Recomendación: Lleva ropa para lluvia.")
else:
    print("\n Recomendación: No es necesario llevar ropa para lluvia.")