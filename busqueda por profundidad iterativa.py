""" arbol
        1
       / \
      2   3
     / \  /|\
    4   6 4 5 7
   /   / \
  5   7   8
  """
# Definimos una clase para representar los nodos del árbol binario
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# Función para crear el árbol con la estructura dada
def create_tree():
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4a = TreeNode(4)  # Primer nodo con valor 4
    node4b = TreeNode(4)  # Segundo nodo con valor 4
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7a = TreeNode(7)  # Primer nodo con valor 7
    node7b = TreeNode(7)  # Segundo nodo con valor 7
    node8 = TreeNode(8)

    root.children = [node2, node3]
    node2.children = [node4a, node6]
    node3.children = [node4b, node5, node7a]
    node4a.children = [node5]
    node6.children = [node7b, node8]

    return root

# Función auxiliar para la búsqueda en profundidad limitada (DLS)
def depth_limited_search(node, goal, limit):
    if limit == 0:
        return [node.value] if node.value == goal else None
    if limit > 0:
        for child in node.children:
            path = depth_limited_search(child, goal, limit - 1)
            if path:
                return [node.value] + path
    return None

# Función principal para la búsqueda en profundidad iterativa (IDDFS)
def iterative_deepening_dfs(root, goal, max_depth):
    for depth in range(max_depth + 1):
        result = depth_limited_search(root, goal, depth)
        if result is not None:
            return result
    return None  # Si no encontramos el objetivo dentro del límite máximo de profundidad

# Crear el árbol
root = create_tree()

# Establecer los parámetros iniciales para la búsqueda
goal = 8
max_depth = 5

# Ejecutar la búsqueda
result = iterative_deepening_dfs(root, goal, max_depth)

# Imprimir el resultado
print(f"Camino encontrado: {result}")