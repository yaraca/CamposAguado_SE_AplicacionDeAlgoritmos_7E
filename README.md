# CamposAguado_SE_AplicacionDeAlgoritmos_7E

#  Aplicación de Algoritmos de Inteligencia Artificial

Este repositorio contiene implementaciones prácticas de tres algoritmos de **Inteligencia Artificial (IA)**, aplicados a problemas reales y cotidianos.  
El objetivo es demostrar cómo distintos enfoques de la IA (grafos, probabilidad y redes bayesianas) permiten resolver problemas de **búsqueda, inferencia y predicción**.

---

## ¿Qué son los algoritmos de Inteligencia Artificial?

Los algoritmos de IA son **procedimientos computacionales** que permiten a las máquinas imitar aspectos de la inteligencia humana como:  
- **Buscar soluciones óptimas** en un espacio de posibilidades.  
- **Razonar bajo incertidumbre**.  
- **Predecir eventos futuros** basados en datos.  

Se clasifican en distintos **enfoques**:
- **Grafos**: exploran nodos y rutas en problemas de búsqueda.  
- **Probabilidad**: manejan incertidumbre con base en el Teorema de Bayes.  
- **Redes Bayesianas**: modelan dependencias entre variables y realizan inferencia probabilística.

---

## Algoritmos implementados en este repositorio

### 1.  Algoritmo A* (Búsqueda en Grafos)
- **Archivo**: `A_Star_RutaOptima.py`  
- **Enfoque**: Grafos  
- **Problema**: Encontrar la mejor ruta caminando desde tu casa hasta una cafetería.  
- **Funcionamiento**: Combina el costo real recorrido y una **heurística** (distancia estimada al destino).  
- **Aplicaciones**:  
  - Navegación en mapas (GPS).  
  - Planeación de rutas en robótica.  
  - Inteligencia en videojuegos.  

---

### 2.  Regla de Bayes (Inferencia con Incertidumbre)
- **Archivo**: `IncertidumbreDeBayes_Medicina.py`  
- **Enfoque**: Probabilidad  
- **Problema**: Determinar la probabilidad de que una persona esté enferma dado que su prueba médica salió positiva.  
- **Funcionamiento**: Usa el **Teorema de Bayes** para actualizar la probabilidad de un evento con base en la evidencia.  
- **Aplicaciones**:  
  - Diagnóstico médico.  
  - Clasificación de correos (spam / no spam).  
  - Sistemas de recomendación.  

---

### 3.  Red Bayesiana Simplificada (Predicción del Clima)
- **Archivo**: `RedBayesiana_Clima.py`  
- **Enfoque**: Redes Bayesianas (Probabilidad + lógica)  
- **Problema**: Predecir si mañana estará **soleado o lluvioso** con base en el clima de hoy y la cantidad de nubes observadas.  
- **Funcionamiento**: Usa probabilidades iniciales, transiciones de estado y observaciones (nubes) para calcular predicciones.  
- **Aplicaciones**:  
  - Predicción meteorológica.  
  - Análisis de riesgos.  
  - Sistemas expertos.  

---

##  Librerías utilizadas

Este proyecto utiliza principalmente librerías estándar de Python:

- **heapq** → Implementación de colas de prioridad (usado en A*).  
- **random** → Generación de valores aleatorios (simulación en la Red Bayesiana).  

 *Nota:* Los ejemplos están diseñados para ser simples y no requieren librerías externas como `numpy`, `pandas` o `pgmpy`, lo cual los hace fáciles de ejecutar en cualquier entorno Python.

---

##  ¿Por qué estos algoritmos?

- **A\***: Demuestra cómo buscar rutas óptimas en un grafo.  
- **Bayes**: Ejemplo claro de cómo manejar incertidumbre en decisiones.  
- **Red Bayesiana**: Predicción realista basada en múltiples factores interdependientes.  

Estos algoritmos representan **tres enfoques fundamentales de la IA**: búsqueda, probabilidad e inferencia.

---