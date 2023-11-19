#include <iostream>
#include <vector>
using namespace std;

bool isPangram(const string &sentence) {
    vector<bool> seen(26, false);

    // Marcar cada letra que aparece en la oración
    for (char ch : sentence) {
        if (ch >= 'a' && ch <= 'z') {
            seen[ch - 'a'] = true;
        }
    }
    //itera booleanos
    // Verificar si todas las letras han aparecido
    for (bool letterSeen : seen) {
        if (!letterSeen) {
            return false;
        }
    }

    return true;
}

int main() {
    string sentence1 = "thequickbrownfoxjumpsoverthelazydog";
    cout << (isPangram(sentence1) ? "true" : "false") << endl;

    string sentence2 = "leetcode";
    cout << (isPangram(sentence2) ? "true" : "false") << endl;

    return 0;
}
