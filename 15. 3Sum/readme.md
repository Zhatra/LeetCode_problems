## 15. 3Sum
<div class="_1l1MA" data-track-load="description_content"><p>Given an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>

<p>Notice that the solution set must not contain duplicate triplets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
<strong>Explanation:</strong> 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> []
<strong>Explanation:</strong> The only possible triplet does not sum up to 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> [[0,0,0]]
<strong>Explanation:</strong> The only possible triplet sums up to 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 3000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>

## Explicación del código `threeSum`

Este código es una implementación de la función `threeSum` de la clase `Solution`, que se utiliza para encontrar todas las tripletas únicas en una lista de enteros `nums` cuya suma sea igual a cero. Específicamente, busca tripletas (a, b, c) donde a + b + c = 0.

### Detalles del código:

1. Se define la clase `Solution`, que contendrá el método `threeSum`.

2. `threeSum` toma un argumento `nums`, que es una lista de enteros, y devuelve una lista de listas que representan las tripletas cuya suma es cero.

3. Se inicializa una lista vacía `res`, que se utilizará para almacenar las tripletas que cumplan la condición requerida.

4. La lista `nums` se ordena en orden ascendente utilizando el método `sort()`. Ordenar la lista es un paso crucial para que el algoritmo funcione correctamente.

5. A continuación, se itera a través de la lista `nums` utilizando un bucle `for` junto con `enumerate()`. `i` contendrá el índice actual y `a` el valor actual en cada iteración.

6. Antes de continuar, se realizan algunas optimizaciones:
   - Se verifica si `a` es mayor que cero. Como la lista está ordenada y si `a` es mayor que cero, entonces `a + b + c` será mayor que cero para cualquier par de elementos restantes en la lista, por lo que no es posible obtener una suma de cero con `a` como primer elemento. Por lo tanto, el bucle se rompe.
   - Se comprueba si `a` es igual al elemento anterior `nums[i - 1]`. Si es así, eso significa que ya se procesó una tripletas con `a` como primer elemento, y para evitar duplicados, se continúa con el próximo valor en la lista.

7. Una vez que se ha realizado la optimización, se definen dos punteros `l` y `r`. `l` apunta al siguiente elemento después de `a` y `r` apunta al último elemento de la lista.

8. Se inicia un bucle `while` que continuará hasta que `l` sea menor que `r`. Esto se hace para explorar todas las posibles combinaciones de parejas `(b, c)`.

9. En cada iteración del bucle, se calcula la suma `threeSum` de `a`, `nums[l]` y `nums[r]`.

10. Si `threeSum` es mayor que cero, eso significa que el valor de `r` es demasiado grande para obtener una suma de cero, por lo que se decrementa `r` en uno para intentar con un valor menor.

11. Si `threeSum` es menor que cero, eso significa que el valor de `l` es demasiado pequeño para obtener una suma de cero, por lo que se incrementa `l` en uno para intentar con un valor mayor.

12. Si `threeSum` es igual a cero, eso significa que hemos encontrado una tripletas (a, b, c) que suma cero. Se agrega esta tripletas a la lista de resultados `res`.

13. Después de agregar la tripletas, tanto `l` como `r` se mueven para evitar duplicados. Si hay elementos repetidos en la lista, se incrementa `l` hasta que `nums[l]` sea diferente del valor anterior en la lista y se decrementa `r` hasta que `nums[r]` sea diferente del valor posterior en la lista.

14. El bucle exterior continúa con el siguiente valor de `a` y repite el proceso.

15. Una vez que se ha recorrido toda la lista, la función retorna la lista `res` que contiene todas las tripletas que suman cero. Estas tripletas están en orden ascendente y no contienen duplicados debido a las optimizaciones realizadas.

En resumen, el código utiliza el algoritmo de "Two Pointers" (dos punteros) para buscar tripletas en una lista ordenada, evitando elementos repetidos y realizando optimizaciones para mejorar la eficiencia del algoritmo. La complejidad del algoritmo es de O(n^2), donde "n" es el número de elementos en la lista `nums`.
