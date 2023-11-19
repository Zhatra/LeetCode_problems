#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    /**
     * Calcula el número de operaciones necesarias para hacer que todos los elementos
     * de un vector sean iguales. Una operación consiste en reducir el valor más grande
     * al siguiente valor más grande que sea estrictamente menor.
     *
     * @param nums Vector de enteros.
     * @return El número de operaciones necesarias para igualar todos los elementos.
     */
    int reductionOperations(vector<int>& nums) {
        // Ordenar el vector en orden descendente para facilitar la comparación
        // de elementos adyacentes y encontrar el siguiente valor más grande.
        sort(nums.rbegin(), nums.rend());

        // Inicializa el contador de operaciones.
        int operations = 0;

        // Recorre el vector y compara cada elemento con su predecesor.
        // Si el elemento actual es diferente de su predecesor, significa que
        // hemos encontrado un nuevo valor más bajo al que se deben reducir
        // todos los valores anteriores más grandes.
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] != nums[i - 1]) {
                // Suma el índice actual al contador de operaciones.
                // Esto representa el número de elementos más grandes que
                // deben ser reducidos a este nuevo valor más bajo.
                operations += i;
            }
        }

        // Retorna el número total de operaciones realizadas.
        return operations;
    }
};
