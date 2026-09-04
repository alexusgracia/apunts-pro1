# Apunts setena classe PRO1

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
