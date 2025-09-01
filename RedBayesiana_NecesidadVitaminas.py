#Red Bayesiana 
#Es un modelo probabilistico grafico que representa un conjunto de variables aleatorias y sus relaciones condicionales mediante un grafo dirigido acíclico (DAG). 
#se compone de nodos (variables aleatorias), aristas dirigidas (dependencias condicionales), tablas de probabilidad condicional (CPT, cada nodo tiene una tabla que describe la probabilidad condicional dado sus padres en el grado) 
#Este permite la inferencia probabilistica eficiente (cuál es la probabilidad de X dado Y) 
#Permiten aprender la estructura y los parámetros de los datos #se pueden usar para tomar decisiones bajo incertidumbre 
#se puede aplicar en el diagnostico médico, reconocimiento de patrones, prediccion y clasificación, inteligencia artificial, etc.

#PROBLEMA: Determinar la probabilidad de que una persona necesite vitaminas adicionales basándose en factores como la dieta, el ejercicio y el estado de salud.

#librerias necesarias
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la red bayesiana
modelo = DiscreteBayesianNetwork([
    ('DormirBien', 'CansancioTarde'),
    ('NadandoMañana', 'CansancioTarde'),
    ('CansancioTarde', 'NecesitaSuplemento')
]) #Definición de la estructura de la red bayesiana con nodos y aristas

#Proabilidades iniciales
cpd_dormir = TabularCPD('DormirBien', 2, [[0.6], [0.4]])  
# 60% dormir bien, 40% dormir mal

cpd_natacion = TabularCPD('NadandoMañana', 2, [[0.7], [0.3]])  
# 70% no entrenas (ej. descanso), 30% sí entrenas

#Cansansio depende de dormir y entrenar
cpd_cansancio = TabularCPD(
    variable='CansancioTarde', variable_card=2, 
    values=[
        [0.9, 0.6, 0.5, 0.2],  # No cansado
        [0.1, 0.4, 0.5, 0.8]   # Sí cansado
    ],
    evidence=['DormirBien', 'NadandoMañana'], 
    evidence_card=[2, 2]
) #Tabla de probabilidad condicional para CansancioTarde
#Si duerme bien y no entrena, 90% no cansado, 10% cansado
#Si duerme bien y entrena, 60% no cansado, 40% cansado
#Si no duerme bien y no entrena, 50% no cansado, 50% cansado
#Si no duerme bien y entrena, 20% no cansado, 80% cansado

#Necesita suplemento depende de cansancio
cpd_suplemento = TabularCPD(
    variable='NecesitaSuplemento', variable_card=2,
    values=[
        [0.8, 0.2],  # No suplemento
        [0.2, 0.8]   # Sí suplemento
    ],
    evidence=['CansancioTarde'],
    evidence_card=[2]
) #Tabla de probabilidad condicional para NecesitaSuplemento
#Si no está cansado, 80% no necesita suplemento, 20% necesita suplemento
#Si está cansado, 20% no necesita suplemento, 80% necesita suplemento

# Añadir las CPDs al modelo
modelo.add_cpds(cpd_dormir, cpd_natacion, cpd_cansancio, cpd_suplemento)
#los cpd se añaden al modelo bayesiano
#los cpd definen las probabilidades condicionales de cada nodo dado sus padres
#Cpd son estructuras que almacenan las probabilidades

# Verificar que el modelo es correcto
print("¿El modelo es válido?", modelo.check_model())

# Realizar inferencia
inferencia = VariableElimination(modelo) #Crear un objeto de inferencia usando eliminación de variables

# Ejemplo: Dormiste mal y entrenaste natación, ¿necesitas suplemento?
resultado = inferencia.query(
    variables=['NecesitaSuplemento'], 
    evidence={'DormirBien': 0, 'NadandoMañana': 1}
)

print("Ejecutando este archivo:", __file__)
print("\nProbabilidad de necesitar suplemento si dormiste mal y entrenaste natación:")
print(resultado)