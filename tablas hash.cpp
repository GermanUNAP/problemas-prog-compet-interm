#include <iostream>
#include <vector>
#include <list>
#include <string>

// Definimos la estructura del nodo que almacenará los pares clave-valor
struct Nodo {
    std::string clave;
    int valor;
    Nodo(const std::string& c, int v) : clave(c), valor(v) {}
};

// Clase para la tabla hash
class TablaHash {
public:
    // Constructor que inicializa la tabla hash con un tamaño dado
    TablaHash(int tam) : tam(tam) {
        tabla.resize(tam);
    }

    // Función para insertar un par clave-valor en la tabla hash
    void insertar(const std::string& clave, int valor) {
        int indice = funcionHash(clave);
        std::cout << "Insertando clave: " << clave << " en el índice: " << indice << std::endl;
        auto& lista = tabla[indice];
        for (auto& nodo : lista) {
            if (nodo.clave == clave) {
                nodo.valor = valor; // Actualiza el valor si la clave ya existe
                return;
            }
        }
        lista.emplace_back(clave, valor); // Inserta un nuevo nodo si la clave no existe
    }

    // Función para buscar un valor dado una clave
    bool buscar(const std::string& clave, int& valor) {
        int indice = funcionHash(clave);
        std::cout << "Buscando clave: " << clave << " en el índice: " << indice << std::endl;
        auto& lista = tabla[indice];
        for (const auto& nodo : lista) {
            if (nodo.clave == clave) {
                valor = nodo.valor;
                return true;
            }
        }
        return false;
    }

    // Función para eliminar un par clave-valor de la tabla hash
    bool eliminar(const std::string& clave) {
        int indice = funcionHash(clave);
        std::cout << "Eliminando clave: " << clave << " en el índice: " << indice << std::endl;
        auto& lista = tabla[indice];
        for (auto it = lista.begin(); it != lista.end(); ++it) {
            if (it->clave == clave) {
                lista.erase(it);
                return true;
            }
        }
        return false;
    }

private:
    int tam;
    std::vector<std::list<Nodo>> tabla;

    // Función de hash simple
    int funcionHash(const std::string& clave) const {
        int hash = 0;
        for (char c : clave) {
            hash = (hash * 31 + c) % tam;
        }
        return hash;
    }
};

int main() {
    // Crear una tabla hash con un tamaño de 10
    TablaHash tablaHash(10);

    // Insertar algunos pares clave-valor en la tabla hash
    tablaHash.insertar("Alice", 85);
    tablaHash.insertar("Bob", 92);
    tablaHash.insertar("Charlie", 78);
    tablaHash.insertar("David", 90);
    tablaHash.insertar("Eve", 75);
    tablaHash.insertar("Frank", 88);

    // Buscar algunos valores en la tabla hash
    int valor;
    if (tablaHash.buscar("Alice", valor)) {
        std::cout << "Clave: Alice, Valor: " << valor << std::endl;
    } else {
        std::cout << "Clave 'Alice' no encontrada." << std::endl;
    }

    if (tablaHash.buscar("Eve", valor)) {
        std::cout << "Clave: Eve, Valor: " << valor << std::endl;
    } else {
        std::cout << "Clave 'Eve' no encontrada." << std::endl;
    }

    // Eliminar una clave
    if (tablaHash.eliminar("Charlie")) {
        std::cout << "Clave 'Charlie' eliminada." << std::endl;
    } else {
        std::cout << "Clave 'Charlie' no encontrada para eliminar." << std::endl;
    }

    // Verificar eliminación
    if (tablaHash.buscar("Charlie", valor)) {
        std::cout << "Clave: Charlie, Valor: " << valor << std::endl;
    } else {
        std::cout << "Clave 'Charlie' no encontrada después de eliminar." << std::endl;
    }

    return 0;
}
