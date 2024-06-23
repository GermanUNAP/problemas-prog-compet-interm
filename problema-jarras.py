#problema de las jarras
#Link del video: https://youtu.be/XwVF62vppO8
def obtener_sucesores(estado, capacidades):
    sucesores = []
    a, b = estado
    cap_a, cap_b = capacidades

    # Llenar la Jarra A
    sucesores.append((cap_a, b))
    # Llenar la Jarra B
    sucesores.append((a, cap_b))
    # Vaciar la Jarra A
    sucesores.append((0, b))
    # Vaciar la Jarra B
    sucesores.append((a, 0))
    # Verter A en B (sin derramar)
    if a + b <= cap_b:
        sucesores.append((0, a + b))
    else:
        sucesores.append((a - (cap_b - b), cap_b))
    # Verter B en A (sin derramar)
    if a + b <= cap_a:
        sucesores.append((a + b, 0))
    else:
        sucesores.append((cap_a, b - (cap_a - a)))

    return sucesores

def dfs(capacidades, objetivo, estado_actual, camino_actual, visitados):
    visitados.add(estado_actual)

    if estado_actual[0] == objetivo:
        return camino_actual + [estado_actual]

    for sucesor in obtener_sucesores(estado_actual, capacidades):
        if sucesor not in visitados:
            resultado = dfs(capacidades, objetivo, sucesor, camino_actual + [estado_actual], visitados)
            if resultado:
                return resultado

    return 

# Ejemplo de uso
capacidades = (4, 3)  # Capacidades de las jarras A y B
objetivo = 2  # Objetivo a medir en la Jarra A
estado_inicial = (0, 0)
camino_inicial = []
visitados = set()

solucion = dfs(capacidades, objetivo, estado_inicial, camino_inicial, visitados)

if solucion:
    print("Secuencia de estados para alcanzar el objetivo:")
    for estado in solucion:
        print(estado)
else:
    print("No se puede alcanzar el objetivo con las capacidades dadas.")
"""
Problema
capacidades jarra A = 4 jarra B = 3
la jarra A tiene que tener 2 litros al final
se puede llenar jarra A y B
Se puede vaciar Jarra A y B
se puede llenar Jarra A a jarra B, pero sin derramar
Se puede vaciar Jarra A a B o viceversa, pero sin derramar 
Link del video: https://youtu.be/XwVF62vppO8
"""