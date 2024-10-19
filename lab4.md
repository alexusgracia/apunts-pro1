# Apunts quarta classe PRO1

## Entrada de dades massiva

A vegades els nostres programes tenen una entrada llarga que fa més difícil debugar, fent feixuga la tasca de compilar i reexecutar i passar les dades cada vegada. És per això que el secret és crear un fitxer amb l'entrada de dades. D'això se n'anomena **redirigir** l'entrada. També podem redirigir la sortida.
Exemples:

```bash
# En aquest exemple el ';' l'usem per a passar múltiples comandes a la terminal, compilant i executant al mateix temps 
p1++ test.cc -o test.x; ./test.x < input.in   # Compilem i executem en una línia i la sortida l'escriu per pantalla
p1++ test.cc -o test.x; ./test.x < input.in > output.out   # Compilem i executem en una línia i la sortida l'escriu en un fitxer
```

## Recorregut 

Un **Recorregut** en programació és el procés de passar per tots els elements d'una estructura de dades per fer-hi alguna operació. 

```c++
#include <iostream>
#include <string>
using namespace std;

int main() {
    string paraula = "programacio";

    for (int i = 0; i < paraula.size(); i++) {
        cout << "Caràcter " << i << ": " << paraula[i] << endl;
    }
}
```

## Cerca

Una **cerca** és l'operació de trobar un element específic dins d'una estructura de dades. El secret és aturar-se quan hem trobat el que estàvem buscant.

### Exemple sense break

```c++
#include <iostream>
#include <string>
using namespace std;

int main() {
    string paraula = "programacio";
    char lletra_a_buscar = 'a';
    bool trobat = false;

    for (int i = 0; i < paraula.size() and not trobat; i++) {
        if (paraula[i] == lletra_a_buscar) {
            cout << "Caràcter trobat a la posició " << i << endl;
            trobat = true;
        }
    }
    if (not trobat) {
        cout << "Caràcter no trobat" << endl;
    }
}
```

### Exemple amb break

Si bé està bé saber com funciona el **break** us recordo que l'ús a l'assignatura de PRO1 **ESTÀ PROHIBIT**.

```c++

#include <iostream>
#include <string>
using namespace std;

int main() {
    string paraula = "programacio";
    char lletra_a_buscar = 'a';
    bool trobat = false;

    for (int i = 0; i < paraula.size(); i++) {
        if (paraula[i] == lletra_a_buscar) {
            cout << "Caràcter trobat a la posició " << i << endl;
            trobat = true;
            break;
        }
    }
    if (!trobat) {
        cout << "Caràcter no trobat" << endl;
    }
}
```

## Quan fer un recorregut i quan fer una cerca?

**Recorregut:** S'utilitza quan cal visitar tots els elements d'una estructura de dades per realitzar alguna operació sobre cadascun (per exemple, imprimir, modificar, sumar).

**Cerca:** S'utilitza quan només es vol trobar un element específic. La cerca seqüencial s'utilitza quan l'estructura no està ordenada, mentre que la cerca binària (que veurem més endavant a l'assignatura) és més eficient però requereix una estructura ordenada.

## Exercicis per a fer avui

### Moviments en el pla *P79784_ca*

```c++
#include <iostream>
using namespace std;

int main(){
    
    char n;
    int x, y;
    x = y = 0;
    
    while (cin >> n){
        
        if (n == 'n') --y;
        if (n == 's') ++y;
        if (n == 'e') ++x;
        if (n == 'o') --x;
    }
    cout << "(" << x << ", " << y << ")" << endl;
}
```

### I-èsim (1) *P39225_ca*

```c++
#include <iostream>
using namespace std;

int main() {
    int n,x;
    bool posicio = false;
    cin >> n;
    int aux = 1;
    while ((cin >> x) and (not posicio)) {
        if (aux == n) {
            posicio = true;
            aux = x;
        }
        else ++aux;
    }
    if (posicio)    cout << "A la posicio " << n << " hi ha un " << aux << "." << endl;
    else cout << "Posicio incorrecta." << endl;  
}
```


## Resum de la sessió

Contingut:
- Entrada de dades massiva
- Què és un recorregut?
- Què és una cerca?.
- Quan fer un recorregut i quan fer una cerca?
- Exercicis


###### Alexandre Gràcia Calvo
