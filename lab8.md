# Apunts classe PRO1

## Repàs de matrius

Recorda que les matrius són vectors de vectors. En C++ les definim com:

```cpp
vector<vector<int>> matriu(m, vector<int>(n)); // Matriu de m x n
```

Per accedir a un element: `matriu[i][j]` on `i` és la fila i `j` és la columna.

Exemple de recorregut:
```cpp
for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
        cout << matriu[i][j];
    }
}
```

### [Exercici: Sopa de lletres *P18660_ca*](https://jutge.org/problems/P18660_ca)

Un exercici que practica matrius bidimensionals amb vectors de strings. Es tracta de cercar paraules en una sopa de lletres en tres direccions: horitzontal, vertical i diagonal.

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int x, m, n;
    bool first = true;
    while (cin >> x >> m >> n) {
        vector<string> paraules(x);
        for (int i = 0; i < x; ++i) cin >> paraules[i];

        // Matriu que representa la sopa de lletres
        vector<vector<char>> sopa(m, vector<char>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> sopa[i][j];
            }
        }

        // Matriu que marca quines lletres han estat trobades
        vector<vector<bool>> marca(m, vector<bool>(n, false));

        // Per a cada paraula de la llista
        for (int w = 0; w < x; ++w) {
            const string& s = paraules[w];
            int L = s.size();

            // Buscar en totes les posicions de la sopa
            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {

                    // Buscar horitzontal (esquerra a dreta)
                    if (j + L <= n) {
                        bool ok = true;
                        for (int k = 0; k < L and ok; ++k) {
                            if (sopa[i][j + k] != s[k]) ok = false;
                        }
                        if (ok) {
                            for (int k = 0; k < L; ++k) marca[i][j + k] = true;
                        }
                    }

                    // Buscar vertical (dalt a baix)
                    if (i + L <= m) {
                        bool ok = true;
                        for (int k = 0; k < L and ok; ++k) {
                            if (sopa[i + k][j] != s[k]) ok = false;
                        }
                        if (ok) {
                            for (int k = 0; k < L; ++k) marca[i + k][j] = true;
                        }
                    }

                    // Buscar diagonal (dalt-esquerra a baix-dreta)
                    if (i + L <= m and j + L <= n) {
                        bool ok = true;
                        for (int k = 0; k < L and ok; ++k) {
                            if (sopa[i + k][j + k] != s[k]) ok = false;
                        }
                        if (ok) {
                            for (int k = 0; k < L; ++k) marca[i + k][j + k] = true;
                        }
                    }
                }
            }
        }

        if (not first) cout << endl;
        first = false;

        // Escriure la sopa marcant amb majúscules les lletres trobades
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                char c = sopa[i][j];
                if (marca[i][j]) c = c - ('a' - 'A');  // Convertir a majúscula
                cout << c;
                if (j + 1 < n) cout << ' ';
            }
            cout << endl;
        }
    }
}
```

**Conceptes aplicats:**
- **Matrius bidimensionals:** `vector<vector<char>>` per a la sopa i `vector<vector<bool>>` per marcar
- **Vectors de strings:** `vector<string>` per emmagatzemar les paraules a cercar
- **Cerca en matrius:** Implementar tres patrons de búsqueda (horitzontal, vertical, diagonal)

## Structs

### Què són les `structs` en C++?

Una `struct` (abreviatura de **estructura**) és un tipus de dades compost que permet agrupar diverses variables sota un mateix nom. Les variables dins d'una `struct` s'anomenen **membres** i poden ser de diferents tipus. Les `structs` són útils per organitzar dades que estan relacionades entre si.

### Característiques principals:
- Agrupa diversos valors en una sola entitat.
- Els membres són accessibles mitjançant el operador `.`.
- Es pot utilitzar per modelar objectes del món real.


### Accés als membres d'una struct

Per accedir als membres d’una struct utilitzem l'operador `.` (punt), com veurem a l'exemple següent.



### ⚠️ **Important abans de continuar!**

> **Les structs es declaren fora del `main` i sempre acabades en `;` al final!**

Fixa't en l'exemple següent:

```cpp

### Exemple bàsic amb accés directe
```cpp
#include <iostream>
#include <string>
using namespace std;

// Definim una struct
struct Persona {
    string nom;
    int edat;
};  // <-- NO OBLIDIS EL PUNT I COMA!

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

### Exemples senzills

Suposem que volem representar un punt en un pla cartesià amb coordenades `x` i `y`.


```c++
#include <iostream>
using namespace std;

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

**Inicialització per llista `{}`:**

La sintaxi `{2, 3}` és una **inicialització per llista** que permet inicialitzar una struct directament amb els valors dels seus membres, **en l'ordre que es declaren**:
- `Punt p1 = {2, 3}` assigna `p1.x = 2` i `p1.y = 3`
- `Punt p2 = {5, 7}` assigna `p2.x = 5` i `p2.y = 7`

Això és equivalent a:
```cpp
Punt p1;
p1.x = 2;
p1.y = 3;
```


**✨ Nota:** Els parèntesis `()` no funcionen per inicialitzar structs de la mateixa forma. Els parèntesis només funcionarien si definissis un constructor personalitzat per a la struct.

### Avantatges de les structs:
1. Faciliten l'organització del codi.
2. Permeten agrupar dades relacionades sota un mateix nom.
3. Són la base per construir objectes més complexos en C++.


### Exemple pràctic: Calcular l'àrea i perímetre d'un rectangle

A continuació veurem una struct `Rectangle` que pot contenir l'amplada i l'altura d'un rectangle. Implementarem funcions per calcular l'àrea i el perímetre utilitzant aquesta struct.

```cpp
#include <iostream>
using namespace std;

// Definim la struct Rectangle
struct Rectangle {
    double amplada;  // Amplada del rectangle
    double altura;   // Altura del rectangle
};

// Pre: r és un Rectangle vàlid amb amplada i altura > 0
// Post: retorna l'àrea del rectangle (amplada * altura)
double calcula_area(const Rectangle& r) {
    return r.amplada * r.altura;
}

// Pre: r és un Rectangle vàlid amb amplada i altura > 0
// Post: retorna el perímetre del rectangle (2 * (amplada + altura))
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

### [Exemple del jutge: Rellotge *P45616_ca*](https://jutge.org/problems/P45616_ca)

Un cas més complex on la struct s'utilitza amb funcions que la modifiquen per referència:

```cpp
#include <iostream>
using namespace std;

struct Rellotge {
    int h; // hores (0 <= h < 24)
    int m; // minuts (0 <= m < 60)
    int s; // segons (0 <= s < 60)
};

// Pre: cap
// Post: retorna un Rellotge amb h=0, m=0, s=0 (mitja nit)
Rellotge mitja_nit() {
    Rellotge r;
    r.h = r.m = r.s = 0;
    return r;
}

// Pre: r és un Rellotge vàlid amb 0 <= h < 24, 0 <= m < 60, 0 <= s < 60
// Post: incrementa r en un segon, mantenint les invariants de validitat
void incrementa(Rellotge& r) {
    ++r.s;
    if (r.s == 60) {
        r.s = 0;
        ++r.m;
        if (r.m == 60) {
            r.m = 0;
            ++r.h;
            if (r.h == 24) {
                r.h = 0;
            }
        }
    }
}

// Pre: r és un Rellotge vàlid amb 0 <= h < 24, 0 <= m < 60, 0 <= s < 60
// Post: escriu r a cout en format HH:MM:SS (amb zeros a l'esquerra)
void escriu(const Rellotge& r) {
    if (r.h < 10) cout << "0";
    cout << r.h << ":";
    if (r.m < 10) cout << "0";
    cout << r.m << ":";
    if (r.s < 10) cout << "0";
    cout << r.s << endl;
}

int main() {
    Rellotge r = mitja_nit();
    escriu(r); // Mostra: 00:00:00
    
    incrementa(r);
    escriu(r); // Mostra: 00:00:01
}
```

**Conceptes importants:**
- Passem la struct per referència (`Rellotge&`) quan volem modificar-la dins d'una funció.
- Passem la struct per referència constant (`const Rellotge&`) quan només volem llegir-la.
- Les structs es retornen per valor i es copien automàticament.

### [Exemple de structs niuats: F001A. Alumnes de la FIPS *P81104_ca*](https://jutge.org/problems/P81104_ca)

Un exemple més avançat amb structs que contenen altres structs i vectors:

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Assignatura {
    string nom;
    double nota;
};

struct Alumne {
    string nom;
    int dni;
    vector<Assignatura> ass;  // Vector d'assignatures
};

// Pre: alums conté alumnes vàlids, dni és un enter vàlid, nom_assignatura és un string no buit
// Post: retorna la nota de l'assignatura nom_assignatura per a l'alumne amb dni;
//       retorna -1 si l'alumne o l'assignatura no existeixen
double nota(const vector<Alumne>& alums, int dni, string nom_assignatura) {
    for (int i = 0; i < alums.size(); ++i) {
        if (alums[i].dni == dni) {
            for (int j = 0; j < alums[i].ass.size(); ++j) {
                if (nom_assignatura == alums[i].ass[j].nom) {
                    return alums[i].ass[j].nota;
                }
            }
        }
    }
    return -1;  // No trobada
}

// Pre: ass és un vector d'Assignatura vàlid
// Post: retorna la mitjana de les notes no negatives de ass;
//       retorna -1 si el vector és buit o totes les notes són negatives
double mitjana(const vector<Assignatura>& ass) {
    int n = ass.size();
    if (n == 0) return -1;
    int cont = 0;
    double suma = 0.0;
    for (int i = 0; i < n; ++i) {
        if (ass[i].nota != -1) {
            ++cont;
            suma += ass[i].nota;
        }
    }
    if (cont == 0) return -1;
    return suma / cont;
}

int main() {
    int n;
    cin >> n;
    
    vector<Alumne> alums(n);
    for (int i = 0; i < n; ++i) {
        cin >> alums[i].nom >> alums[i].dni;
        int num_assignatures;
        cin >> num_assignatures;
        
        alums[i].ass.resize(num_assignatures);
        for (int j = 0; j < num_assignatures; ++j) {
            cin >> alums[i].ass[j].nom >> alums[i].ass[j].nota;
        }
    }
    
    // Consultes
    int dni;
    while (cin >> dni) {
        string assignatura;
        cin >> assignatura;
        cout << nota(alums, dni, assignatura) << endl;
    }
    
}
```

**Conceptes importants:**
- **Structs niuats:** Un struct pot contenir altres structs o vectors de structs.
- **Vectors dinàmics:** Usem `vector<Assignatura>` per emmagatzemar assignatures d'un alumne.
- **Accés entrellaçat:** Accedim a dades profundes com `alums[i].ass[j].nota`.

---

## 📚 Recomanat per al proper dia

**Consulta el document:** [Algorismes fonamentals](./alg-fonamentals.pdf)

**Especialment important:** Estudi en profunditat de la **cerca dicotòmica (binary search)**
- Entendre com funciona l'algoritme
- Pensar en casos d'ús
