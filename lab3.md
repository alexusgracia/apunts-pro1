# Apunts tercera classe PRO1


## Què és un **while**

**while** és una estructura de control iterativa que permet repetir un bloc de codi mentre una condició lògica sigui certa (true).

Quan la condició es torna falsa, el bucle s'atura. 

Aquesta estructura és útil quan no es coneix prèviament el nombre d'iteracions que cal realitzar, i depèn d'una condició canviant dins del bucle.

## Exemple de **while** 

```c++
int i = 0;
while (i < 5) {
    cout << i << endl;
    i++;
}
```

## Recorreguts

### Mitjançant una sentinella

```c++
char sentinella = '#' // O qualsevol lletra, string, nombre, etc.
char c;
cin >> c;
while(c!=sentinella){
    //Tractem el caràcter c

    cin >> c;
}

```

### Entrades infinites

```c++

char c;
while(cin >> c){
    //Tractem el caràcter c
}

```

### Nombre d'entrades

```c++
int n;
char c;
cin >> n;
while(n>0){
    //Stuff here
    cin >> c;
    --n; //És a dir, restem 1 al nombre d'iteracions
    
}
```

## Què és un **for**

**for** és una altra estructura de control iterativa, però a diferència del while, s'utilitza quan es coneix prèviament el nombre d'iteracions o quan aquestes poden estar controlades per un comptador.

El bucle for es divideix en tres parts: inicialització, condició, i actualització. Durant cada iteració, es comprova la condició, i si és certa, es continua executant el bloc de codi.

## Exemple de **for** 

```c++
for (int i = 0; i < 5; i++) {
    cout << i << endl;
}
```

## Quan s'ha de fer servir un **while** i quan un **for**?

No hi ha una norma escrita en general, sempre es pot usar un while en comptes d'un for i un for en comptes d'un while, però la simplicitat d'un o l'altre es fa més evident conforme es va programant i adquirint experiència.

En resum es podria simplificar:

- **`while`** s'utilitza quan la condició depèn d'un factor que pot canviar de manera dinàmica dins del bucle.

- **`for`** és més adequat quan tenim un nombre d'iteracions fix o quan el control de les iteracions és més previsible.


## Loops inside loops

```c++
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        cout << i << "," << j << endl;
    }
}
```

## Structs

### Què són les `structs` en C++?

Una `struct` (abreviatura de **estructura**) és un tipus de dades compost que permet agrupar diverses variables sota un mateix nom. Les variables dins d'una `struct` s'anomenen **membres** i poden ser de diferents tipus. Les `structs` són útils per organitzar dades que estan relacionades entre si.

### Característiques principals:
- Agrupa diversos valors en una sola entitat.
- Els membres són accessibles mitjançant el operador `.`.
- Es pot utilitzar per modelar objectes del món real.


### Accés als membres d'una struct

Per accedir als membres d’una struct:
- Si tens un **objecte directe**, utilitza l'operador `.` (punt).
- Si tens un **punter** (que veurem més endavant) a la struct, utilitza l'operador `->` (fletxa).

### Exemple bàsic amb accés directe
```cpp
#include <iostream>
using namespace std;

// Definim una struct
struct Persona {
    string nom;
    int edat;
};

int main() {
    // Creem una instància de la struct
    Persona p;

    // Assignem valors als membres
    p.nom = "Anna";
    p.edat = 20;

    // Accedim als membres amb l'operador '.'
    cout << "Nom: " << p.nom << endl;
    cout << "Edat: " << p.edat << endl;
}
```

### Exemple senzill

Suposem que volem representar un punt en un pla cartesià amb coordenades `x` i `y`.

```cpp
#include <iostream>
using namespace std;

// Definim una struct
struct Persona {
    string nom;      // Nom de la persona
    int edat;        // Edat de la persona
    double altura;   // Altura en metres
};

int main() {
    // Creem una instància de la struct
    Persona p;

    // Assignem valors als membres
    p.nom = "Joan";
    p.edat = 25;
    p.altura = 1.80;

    // Mostrem les dades
    cout << "Nom: " << p.nom << endl;
    cout << "Edat: " << p.edat << endl;
    cout << "Altura: " << p.altura << " m" << endl;
}
```
Sortida del programa:
```text
Nom: Joan
Edat: 25
Altura: 1.8 m
```

### Un altre exemple

```c++
struct Punt {
    int x;  // Coordenada X
    int y;  // Coordenada Y
};

int main() {
    Punt p1 = {2, 3}; // Inicialitzem un punt
    Punt p2 = {5, 7};

    // Mostrem les coordenades
    cout << "Punt 1: (" << p1.x << ", " << p1.y << ")" << endl;
    cout << "Punt 2: (" << p2.x << ", " << p2.y << ")" << endl;
}
```

### Avantatges de les structs:
1. Faciliten l'organització del codi.
2. Permeten agrupar dades relacionades sota un mateix nom.
3. Són la base per construir objectes més complexos en C++.


### Un altre exemple

Definiu una struct anomenada `Rectangle` que contingui l'amplada i l'altura d'un rectangle. Implementeu un programa que calculi l'àrea i el perímetre utilitzant aquesta struct.

```cpp
#include <iostream>
using namespace std;

// Definim la struct Rectangle
struct Rectangle {
    double amplada;  // Amplada del rectangle
    double altura;   // Altura del rectangle
};

// Funció per calcular l'àrea d'un rectangle
double calcula_area(const Rectangle& r) {
    return r.amplada * r.altura;
}

// Funció per calcular el perímetre d'un rectangle
double calcula_perimetre(const Rectangle& r) {
    return 2 * (r.amplada + r.altura);
}

int main() {
    // Crear una instància de la struct
    Rectangle r;

    // Llegir dades del rectangle
    cout << "Introdueix l'amplada del rectangle: ";
    cin >> r.amplada;
    cout << "Introdueix l'altura del rectangle: ";
    cin >> r.altura;

    // Calcular i mostrar els resultats
    cout << "Àrea: " << calcula_area(r) << endl;
    cout << "Perímetre: " << calcula_perimetre(r) << endl;
}
```

## Exercicis per a fer avui

### Potències *P79817_ca*
```c++
#include <iostream>
using namespace std;

int main(){

    int a, b;
    
    while (cin >> a){
        cin >> b;
        int aux;
        aux = a;
        if (b == 0) aux = 1;
        while (b > 1){
            aux = aux * a;
            --b;
        }
        cout << aux << endl;
    }
}
```

### Control C202E *P32533_ca*
```c++
#include <iostream>
using namespace std;

int main(){
    int n, aux;
    cin >> n;
    aux = n;
    while (aux > 0){
	for(int i = 0; i < (aux - 1); ++i){
	    cout << "+";
	}
	cout << "/";
	for (int j = 0; j < (n - aux) ;++j){
	    cout << "*";
	}
	--aux;
	cout << endl;
    }
}
```

## Resum de la sessió

Contingut:
- Què és un while?
- Condicions de finalització.
- Què és un for?
- Quan escollir entre un for i un while?
- Exercicis


Alexandre Gràcia Calvo
