#include <iostream>
#include <cctype>  // For isalnum() and tolower()
using namespace std;

bool isPalindrome(const string &s) {
    int left = 0, right = s.length() - 1;

    while (left < right) {
        // Skip non-alphanumeric characters
        while (left < right && !isalnum(s[left])) {
            left++;
        }
        while (left < right && !isalnum(s[right])) {
            right--;
        }

        // Check if the characters are different
        if (tolower(s[left]) != tolower(s[right])) {
            return false;
        }

        left++;
        right--;
    }

    return true;
}

int main() {
    string s1 = "A man, a plan, a canal: Panama";
    cout << (isPalindrome(s1) ? "true" : "false") << endl;

    string s2 = "race a car";
    cout << (isPalindrome(s2) ? "true" : "false") << endl;

    string s3 = " ";
    cout << (isPalindrome(s3) ? "true" : "false") << endl;

    return 0;
}


/*
Vamos a desglosar el proceso de ejecución del programa utilizando el ejemplo `"A man, a plan, a canal: Panama"`. Este ejemplo es particularmente interesante porque incluye espacios, comas, dos puntos y una mezcla de mayúsculas y minúsculas, todo lo cual el programa debe gestionar para determinar si la cadena es un palíndromo.

### Ejemplo: `"A man, a plan, a canal: Panama"`

Aquí está lo que sucede paso a paso cuando este string se pasa a la función `isPalindrome`:

1. **Inicialización:**
   - `left` se inicializa en 0 (apuntando a la 'A' al principio de la cadena).
   - `right` se inicializa en 29 (apuntando a la 'a' al final de la cadena).

2. **Primera Iteración del Bucle:**
   - `left` está en un carácter alfanumérico ('A'), así que no se mueve.
   - `right` está en un carácter alfanumérico ('a'), así que tampoco se mueve.
   - Se comparan los caracteres: `tolower('A')` es igual a `tolower('a')`, entonces todo bien.
   - `left` se incrementa (ahora es 1, apuntando a la primera ' ').
   - `right` se decrementa (ahora es 28, apuntando a la 'm').

3. **Siguientes Iteraciones:**
   - El bucle continúa, incrementando `left` y decrementando `right`, y saltando los caracteres no alfanuméricos (' ', ',', ':').
   - En cada paso, compara los caracteres en las posiciones `left` y `right`.
   - Por ejemplo, eventualmente `left` apuntará a 'm' y `right` a 'm', ambos se comparan y son iguales.

4. **Hacia el Centro:**
   - Este proceso continúa, moviéndose hacia el centro de la cadena.
   - Cada par de caracteres alfanuméricos correspondientes se compara.

5. **Conclusión:**
   - Cuando `left` y `right` se cruzan, lo que sucede después de haber comparado todas las letras alfanuméricas, la función concluye que la cadena es un palíndromo y retorna `true`.

Por lo tanto, para `"A man, a plan, a canal: Panama"`, el programa seguirá este proceso, comparando cada letra alfanumérica desde ambos extremos de la cadena, ignorando los espacios y signos de puntuación, y al final retornará `true`, indicando que la cadena es un palíndromo.
*/