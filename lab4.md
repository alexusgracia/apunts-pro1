# Apunts quarta classe PRO1

## Entrada de dades massiva

A vegades els nostres programes tenen una entrada llarga que fa més difícil debugar, fent feixuga la tasca de compilar i reexecutar i passar les dades cada vegada. És per això que el secret és crear un fitxer amb l'entrada de dades. D'això se n'anomena **redirigir** l'entrada. També podem redirigir la sortida.
Exemples:

```bash
# En aquest exemple el ';' l'usem per a passar múltiples comandes a la terminal, compilant i executant al mateix temps 
g++ test.cc -o test.x; ./test.x < input.in   # Compilem i executem en una línia i la sortida l'escriu per pantalla
g++ test.cc -o test.x; ./test.x < input.in > output.out   # Compilem i executem en una línia i la sortida l'escriu en un fitxer
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

## Passar per valor i per referència en funcions en C++

En C++, es poden passar arguments a les funcions de dues maneres principals: **per referència** i **per valor**. 

<div style="text-align: center;">
  ![https://repo.fib.upc.edu/alexandre.gracia/apunts-pro1/-/blob/main/assets/coffee.webm](/assets/coffee.webm)
</div>



### Passar per valor

Quan es passa un argument per valor, es crea una còpia de l'argument original dins de la funció. Això vol dir que qualsevol canvi fet sobre el paràmetre dins de la funció no afectarà el valor original fora de la funció.

```cpp
#include <iostream>

void incrementarPerValor(int num) {
    num = 57;  // Canviem el valor de num
    cout << "Dins de la funció (per valor): " << num << endl;
}

int main() {
    int x = 5;
    incrementarPerValor(x);  // Es passa el valor de x
    cout << "Fora de la funció: " << x << endl;  // x segueix sent 5
}
```

### Passar per referència
Quan es passa un argument per referència, es passa l'adreça de la variable original. Això es fa afegint `&` entre el tipus de paràmetre i el nom del paràmetre. Per exemple: int& num.
Això implica que qualsevol canvi fet sobre el paràmetre dins de la funció afectarà directament la variable original.

```cpp
#include <iostream>

void incrementarPerReferencia(int& num) { // fixeu-vos l'ús de & !!!!!!
    num = 57;  // Canviem el valor de num
    cout << "Dins de la funció (per referència): " << num << endl;
}

int main() {
    int x = 5;
    incrementarPerReferencia(x);  // Es passa la referència de x
    cout << "Fora de la funció: " << x << endl;  // x ha estat modificat
}
```

### Quan passar per valor i per referència?
#### Passar per valor
* Utilitza-ho quan no vulguis que la funció modifiqui el valor original de la variable.
* Adequat per tipus de dades petits (com enters o caràcters), on la còpia és eficient.
#### Passar per referència
* Utilitza-ho quan vulguis modificar el valor original dins de la funció.

* És més eficient per a tipus de dades grans (com arrays o objectes), ja que evita la còpia de la informació.

## Què és  `const`?

La paraula clau `const` en C++ es fa servir per declarar que una variable o un paràmetre és constant, és a dir, que no es pot modificar després de la seva inicialització. Això pot ajudar a evitar errors i millorar la claredat del codi. 

### `const` amb variables locals

Quan declarem una variable local com a `const`, no podrem modificar el seu valor després de la seva inicialització. Això ajuda a garantir que el valor de la variable es mantingui constant al llarg del seu abast.

```cpp
#include <iostream>

int main() {
    const int x = 10; // x és constant
    cout << "El valor de x és: " << x << endl;

    // x = 20;  // Error! No es pot modificar una variable constant
}
```
La variable x es declara com a const, així que no es pot modificar el seu valor un cop assignat.

### `const` en paràmetres de funció
Es pot utilitzar const per garantir que els paràmetres de funció no es modificaran. Això és útil quan volem assegurar-nos que els valors passats a la funció no canviïn durant la seva execució.

```cpp

#include <iostream>

void mostrarValor(const int x) {
    cout << "El valor passat és: " << x << sendl;

    // x = 20;  // Error! No es pot modificar x perquè és const
}

int main() {
    int a = 10;
    mostrarValor(a);  // Passa 'a' com a paràmetre constant
}
```

### Const amb referència
Quan es passa un paràmetre per referència, podem utilitzar const per garantir que no es modificaran els valors originals.

```cpp
#include <iostream>

void mostrarValor(const int& x) {
    cout << "El valor passat per referència és: " << x << endl;

    // x = 20;  // Error! No es pot modificar x perquè és const
}

int main() {
    int a = 10;
    mostrarValor(a);  // Passa 'a' per referència com a constant
    return 0;
}
```
En aquest cas, el paràmetre `x` es passa per referència i es declara com a `const`. Això vol dir que, tot i que x és passat per referència (i, per tant, apunta a la variable original), no es pot modificar dins de la funció.



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
        else if (n == 's') ++y;
        else if (n == 'e') ++x;
        else if (n == 'o') --x;
        else cout << "No hauria de passar mai" << endl;
    }
    cout << "(" << x << ", " << y << ")" << endl;
}
```

### I-èsim (1) *P39225_ca*
En aquest exemple el tractem com si fos entrades infinites:

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

En aquesta alternativa el tractem com si fos entrada amb sentinella:

```c++
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int i, valor;
    cin >> i >> valor;
    bool trobat = false;
    int pos = 0;
    while (valor != -1 and not trobat)
    {
        ++pos;
        if (i == pos)
            trobat = true;
        else
        {
            cin >> valor;
        }
    }
    if (trobat)
    {
        cout << "A la posicio " << i << " hi ha un " << valor << '.' << endl;
    }
    else
    {
        cout << "Not trobat" << endl;
    }
}

```

### Tauler d'escacs (1) *P42280_ca*
En aquest exemple el tractem com si fos entrades infinites:

### Alternativa 1
```c++
#include <iostream>
using namespace std;

int main(){
    int f, c;
    cin >> f >> c;
    int total = 0;
    for(int i = 0; i < f; ++i){
        char nombre;
        for (int j = 0; j < c; ++j){
	    cin >> nombre;
            total =  total + (nombre-'0');
        }
    }
    cout << total << endl;
}
```

### Alternativa 2

```c++
#include <iostream>
using namespace std;

int main()
{
    int f, c;
    cin >> f >> c;
    int suma = 0;
    for (int i = 0; i < f; ++i)
    {
        string s;
        cin >> s;
        for (int j = 0; j < s.size(); ++j)
        {
            suma = suma + s[j] - '0';
        }
    }
    cout << suma << endl;
}

```

Alexandre Gràcia Calvo
