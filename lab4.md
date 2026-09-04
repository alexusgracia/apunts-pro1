# Apunts quarta classe PRO1

### Exemple de què no fer!!! *X98718*
```c++

// AQUEST PROGRAMA NO ÉS CORRECTE
#include <iostream>
using namespace std;

int main(){
    char x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10;
    cin >> x0 >> x1 >> x2 >> x3 >> x4 >> x5 >> x6 >> x7 >> x8 >> x9 >> x10;
    if (x0 == x1 and x1 == x2 and x2 == x3) cout << x0 << x1 << x2 << " " << 1 << endl;
    else if (x0 == x2 and x1 == x3 and x2 == x4) cout << x0 << x1 << x2 << " " << 2 << endl;
    else if (x1 == x2 and x2 == x3 and x3 == x4) cout << x1 << x2 << x3 << " " << 2 << endl;
    else if (x0 == x3 and x1 == x4 and x2 == x5) cout << x0 << x1 << x2 << " " << 3 << endl;
    else if (x1 == x3 and x2 == x4 and x3 == x5) cout << x1 << x2 << x3 << " " << 3 << endl;
    else if (x2 == x3 and x3 == x4 and x4 == x5) cout << x2 << x3 << x4 << " " << 3 << endl;
    else if (x0 == x4 and x1 == x5 and x2 == x6) cout << x0 << x1 << x2 << " " << 4 << endl;
    else if (x1 == x4 and x2 == x5 and x3 == x6) cout << x1 << x2 << x3 << " " << 4 << endl;
    else if (x2 == x4 and x3 == x5 and x4 == x6) cout << x2 << x3 << x4 << " " << 4 << endl;
    else if (x3 == x4 and x4 == x5 and x5 == x6) cout << x3 << x4 << x5 << " " << 4 << endl;
    else if (x0 == x5 and x1 == x6 and x2 == x7) cout << x0 << x1 << x2 << " " << 5 << endl;
    else if (x1 == x5 and x2 == x6 and x3 == x7) cout << x1 << x2 << x3 << " " << 5 << endl;
    else if (x2 == x5 and x3 == x6 and x4 == x7) cout << x2 << x3 << x4 << " " << 5 << endl;
    else if (x3 == x5 and x4 == x6 and x5 == x7) cout << x3 << x4 << x5 << " " << 5 << endl;
    else if (x4 == x5 and x5 == x6 and x6 == x7) cout << x4 << x5 << x6 << " " << 5 << endl;
    else if (x0 == x6 and x1 == x7 and x2 == x8) cout << x0 << x1 << x2 << " " << 6 << endl;
    else if (x1 == x6 and x2 == x7 and x3 == x8) cout << x1 << x2 << x3 << " " << 6 << endl;
    else if (x2 == x6 and x3 == x7 and x4 == x8) cout << x2 << x3 << x4 << " " << 6 << endl;
    else if (x3 == x6 and x4 == x7 and x5 == x8) cout << x3 << x4 << x5 << " " << 6 << endl;
    else if (x4 == x6 and x5 == x7 and x6 == x8) cout << x4 << x5 << x6 << " " << 6 << endl;
    else if (x5 == x6 and x6 == x7 and x7 == x8) cout << x5 << x6 << x7 << " " << 6 << endl;
    else if (x0 == x7 and x1 == x8 and x2 == x9) cout << x0 << x1 << x2 << " " << 7 << endl;
    else if (x1 == x7 and x2 == x8 and x3 == x9) cout << x1 << x2 << x3 << " " << 7 << endl;
    else if (x2 == x7 and x3 == x8 and x4 == x9) cout << x2 << x3 << x4 << " " << 7 << endl;
    else if (x3 == x7 and x4 == x8 and x5 == x9) cout << x3 << x4 << x5 << " " << 7 << endl;
    else if (x4 == x7 and x5 == x8 and x6 == x9) cout << x4 << x5 << x6 << " " << 7 << endl;
    else if (x5 == x7 and x6 == x8 and x7 == x9) cout << x5 << x6 << x7 << " " << 7 << endl;
    else if (x6 == x7 and x7 == x8 and x8 == x9) cout << x6 << x7 << x8 << " " << 7 << endl;
    else if (x0 == x8 and x1 == x9 and x2 == x10) cout << x0 << x1 << x2 << " " << 8 << endl;
    else if (x1 == x7 and x2 == x8 and x3 == x10) cout << x1 << x2 << x3 << " " << 8 << endl;  
    else if (x2 == x8 and x3 == x9 and x4 == x10) cout << x2 << x3 << x4 << " " << 8 << endl;  
    else if (x3 == x8 and x4 == x9 and x5 == x10) cout << x3 << x4 << x5 << " " << 8 << endl;
    else if (x4 == x8 and x5 == x9 and x6 == x10) cout << x4 << x5 << x6 << " " << 8 << endl;
    else if (x5 == x8 and x6 == x9 and x7 == x10) cout << x5 << x6 << x7 << " " << 8 << endl;
    else if (x6 == x8 and x7 == x9 and x8 == x10) cout << x6 << x7 << x8 << " " << 8 << endl;
    else if (x7 == x8 and x8 == x9 and x9 == x10) cout << x7 << x8 << x9 << " " << 8 << endl;
```
Solució bona

```c++
//AQUEST SÍ ÉS CORRECTE
#include <iostream>
using namespace std;

int main () {
    char x,y,z;
    int pos=0;
    int a=0,b=0,c=0,d=0, e=0,f=0,g=0,h=0;
    bool found=false; 
    cin >> x >> y >> z;

    while (not found){
        if (x=='a' and y=='a' and z=='a') a=a+1;
        else if (x=='a' and y=='a' and z=='b') b=b+1;
        else if (x=='a' and y=='b' and z=='a') c=c+1;
        else if (x=='a' and y=='b' and z=='b') d=d+1;
        else if (x=='b' and y=='a' and z=='a') e=e+1;
        else if (x=='b' and y=='a' and z=='b') f=f+1;
        else if (x=='b' and y=='b' and z=='a') g=g+1;
        else if (x=='b' and y=='b' and z=='b') h=h+1;

        if (a==2 or b==2 or c==2 or d==2 or e==2 or f==2 or g==2 or h==2) found=true;
        if (found) cout << x << y << z << " " << pos << endl;
        pos=pos+1;
        x=y;
        y=z;
        cin >> z;
    }
}
```

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

#### Alternativa 1
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

#### Alternativa 2

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


###  Número del revés en hexadecimal *P60816_ca*

```c++
#include <iostream>
using namespace std;

int main()
{
    int a;
    cin >> a;
    string resultat = "";
    if (a == 0)
    {
        resultat = "0";
    }
    while (a > 0)
    {
        int residu = a % 16;
        if (residu > 9)
        {
            if (residu == 10)
                resultat = resultat + 'A';
            else if (residu == 11)
                resultat = resultat + 'B';
            else if (residu == 12)
                resultat = resultat + 'C';
            else if (residu == 13)
                resultat = resultat + 'D';
            else if (residu == 14)
                resultat = resultat + 'E';
            else if (residu == 15)
                resultat = resultat + 'F';
        }
        else
        {
            resultat = resultat + char(residu + '0');
        }
        a = a / 16;
    }
    cout << resultat << endl;
    cout << resultat.length() << endl;
    
    // Si volgúessim hexadecimal correcte ( i no al revés)
    /*

    for (int i = 0; i < resultat.length(); ++i)
    {
        cout << resultat[resultat.length() - i - 1];
    }
    cout << endl;
    */
}
```
