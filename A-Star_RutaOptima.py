#A Star 
#Este algoritmo encuentra la ruta óptima entre dos puntos en un grafo ponderado utilizando una heurística para estimar el costo restante hasta el objetivo.
#La función a_star toma un grafo, un nodo inicial, un nodo objetivo y una función heurística como entrada, y devuelve la ruta óptima y su costo total.
#Se utiliza una cola de prioridad para explorar los nodos con el menor costo estimado primero, y se mantiene un registro de los nodos visitados para evitar ciclos.
#Se utiliza en planificación de rutas, juegos y problemas de búsqueda en inteligencia artificial.

#PROBLEMA: Encontrar la mejor ruta caminando desde tu casa hasta la cafetería de tu preferencia, pasando por calles que pueden tener diferentes distancias (costos) 
# y usando una heurística de “distancia recta al destino”.

import heapq #importa la biblioteca heapq para usar una cola de prioridad

# Función A*
def a_estrella(grafo, inicio, objetivo, heuristica): #definición de la función a_estrella que toma un grafo, un nodo inicial, un nodo objetivo y una función heurística como argumentos
    cola = [(0 + heuristica(inicio, objetivo), 0, inicio, [inicio])] #cola de prioridad que almacena tuplas con (f, g, nodo, camino)
    visitados = set() #conjunto para rastrear nodos visitados

    while cola: #mientras la cola no esté vacía
        f_actual, g_actual, nodo_actual, camino = heapq.heappop(cola) #extrae el nodo con el menor f de la cola
        if nodo_actual == objetivo: #si el nodo actual es el objetivo
            return camino, g_actual #devuelve el camino y el costo g

        if nodo_actual not in visitados: #si el nodo actual no ha sido visitado
            visitados.add(nodo_actual) #marca el nodo como visitado
            for vecino, costo in grafo[nodo_actual]:  #explora los vecinos del nodo actual
                if vecino not in visitados: #si el vecino no ha sido visitado
                    g_nuevo = g_actual + costo #calcula el nuevo costo g
                    f_nuevo = g_nuevo + heuristica(vecino, objetivo) #calcula el nuevo costo f
                    heapq.heappush(cola, (f_nuevo, g_nuevo, vecino, camino + [vecino])) #agrega el vecino a la cola
    return None, float('inf') #si no se encuentra una ruta, devuelve None y un costo infinito

#Ejemplo de uso grafo de la ciudad con distancias entre puntos
grafo_ciudad = {
    'Casa': [('Parque', 2), ('Escuela', 4)], 
    'Parque': [('Casa', 2), ('Biblioteca', 3)],
    'Escuela': [('Casa', 4), ('Tienda', 2)],
    'Biblioteca': [('Parque', 3), ('Cafeteria', 4)],
    'Tienda': [('Escuela', 2), ('Cafeteria', 3)],
    'Cafeteria': []
} #grafo representando la ciudad con nodos y costos

#Función heurística: distancia recta al destino (valores estimados)
def heuristica_ciudad(nodo, objetivo):
    distancias = {
        'Casa': 6,
        'Parque': 4,
        'Escuela': 3,
        'Biblioteca': 2,
        'Tienda': 1,
        'Cafeteria': 0
    }
    return distancias[nodo] #función heurística que devuelve la distancia estimada desde el nodo actual al objetivo

#Ejemplo de uso
camino, distancia = a_estrella(grafo_ciudad, 'Casa', 'Cafeteria', heuristica_ciudad) #llama a la función a_estrella con el grafo de la ciudad, nodo inicial 'Casa', nodo objetivo 'Cafeteria' y la función heurística

if camino is not None: #si se encontró un camino
    print(f"Ruta óptima: {' -> '.join(map(str, camino))} con distancia total {distancia}") #imprime la ruta óptima y la distancia total
else: #si no se encontró un camino
    print("No se encontró una ruta al destino.") #imprime un mensaje indicando que no se encontró una ruta

#Salida esperada: Ruta óptima: Casa -> Parque -> Biblioteca -> Cafeteria con distancia total 9
#Nota: La salida puede variar dependiendo de la heurística y el grafo utilizado.
