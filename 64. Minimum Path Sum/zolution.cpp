#include <iostream>
#include <vector>
using namespace std;

// Función para calcular la suma mínima del camino en una cuadrícula
int minPathSum(vector<vector<int>>& grid) {
    // Si la cuadrícula está vacía, devuelve 0
    if (grid.empty() || grid[0].empty()) return 0;

    // Obtener el número de filas y columnas de la cuadrícula
    int rows = grid.size();
    int cols = grid[0].size();

    // Utilizar la cuadrícula de entrada como matriz de programación dinámica para optimizar el espacio
    // Procesar la primera fila: cada celda acumula la suma de las celdas anteriores en la fila
    for (int i = 1; i < cols; ++i) {
        grid[0][i] += grid[0][i - 1];
    }

    // Procesar la primera columna: cada celda acumula la suma de las celdas anteriores en la columna
    for (int i = 1; i < rows; ++i) {
        grid[i][0] += grid[i - 1][0];
    }

    // Rellenar el resto de la cuadrícula
    for (int i = 1; i < rows; ++i) {
        for (int j = 1; j < cols; ++j) {
            // Para cada celda, calcula la suma mínima del camino sumando el valor de la celda
            // y el mínimo de las dos celdas adyacentes (izquierda y arriba)
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]);
        }
    }

    // Devuelve el valor en la esquina inferior derecha de la cuadrícula, que es la suma mínima del camino
    return grid[rows - 1][cols - 1];
}

int main() {
    // Crear una cuadrícula de ejemplo
    vector<vector<int>> grid = {{1, 3, 1}, {1, 5, 1}, {4, 2, 1}};
    
    // Imprimir la suma mínima del camino calculada para la cuadrícula
    cout << "Minimum Path Sum: " << minPathSum(grid) << endl;
    return 0;
}
