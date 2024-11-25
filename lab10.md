# Apunts desena classe PRO1

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
```txt
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

## Exercicis per a fer avui


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

Entrada:

```txt
Introdueix l'amplada del rectangle: 5
Introdueix l'altura del rectangle: 3
```
Sortida:
```txt
Àrea: 15
Perímetre: 16
```

## Altres formes d'accedir a elements de les structs, especialment amb punters

### Accés mitjançant punters
Quan treballes amb punters a structs, pots accedir als seus membres amb l'operador ->.

```cpp
#include <iostream>
using namespace std;

struct Punt {
    int x, y;
};

int main() {
    Punt p = {5, 10};        // Declarem un punt
    Punt* ptr = &p;          // Declarem un punter a la struct

    // Accedim als membres amb '->'
    cout << "Coordenada X: " << ptr->x << endl;
    cout << "Coordenada Y: " << ptr->y << endl;

    // Alternativa: desreferenciar manualment
    cout << "Coordenada X (manual): " << (*ptr).x << endl;
}
```

### Conceptes clau a recordar:
- Les **structs** són una eina poderosa per organitzar dades relacionades.
- Es poden combinar amb altres tipus de dades (com vectors) per gestionar conjunts d'informació.
- El pas de structs a funcions es pot fer per valor (copia) o per referència (més eficient).

**Consell:** Quan treballis amb structs grans, és preferible passar-les com a referència (`const&`) a les funcions per evitar còpies innecessàries.


### Estudiants *P11141_ca*

```c++
#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Estudiant{
    int dni;
    string nom;
    double nota;
    bool repetidor;
    
};

void informacio(const vector<Estudiant>& es, double& min, double& max, double& mitj){
    min = max = mitj = -1;
    int N;
    N = es.size();
    double cont = 0;
    bool suma = true;
    for (int i = 0; i < N; ++i){
	bool presentat = true;
	if (es[i].nota == -1) presentat = false;
	if (not es[i].repetidor and presentat){
	    if (suma){
		min = 10;
		max = mitj = 0;
		suma = false;
	    }
	    ++cont;
	    if (min > es[i].nota) min = es[i].nota;
	    if (max < es[i].nota) max = es[i].nota;
	    mitj = mitj + es[i].nota;
	}
    }
    if (mitj != -1) mitj /= cont;
}
```

### Vectors comprimits *P16175*

```c++
#include <iostream>
#include <vector>
using namespace std;

struct Parell {
	int valor;	// Diferent de zero
	int pos;	// Més gran o igual que zero
};

typedef vector<Parell> Vec_Com;

// Llegir un vector comprimit
void llegeix(Vec_Com& v) {
	int n;
	cin >> n;
	v.resize(n);
	for (int i = 0; i < n; ++i) {
		char separator;
		cin >> v[i].valor >> separator >> v[i].pos;
	}
}

// Sumar dos vectors comprimits
Vec_Com suma(const Vec_Com& v1, const Vec_Com& v2) {
	int		n1 = v1.size();
	int		n2 = v2.size();
	Vec_Com resultat(n1 + n2);
	int		i = 0, j = 0, k = 0;

	while (i < n1 and j < n2) {
		if (v1[i].pos < v2[j].pos) {
			resultat[k].valor = v1[i].valor;
			resultat[k].pos = v1[i].pos;
			++i;
		} else if (v1[i].pos > v2[j].pos) {
			resultat[k].valor = v2[j].valor;
			resultat[k].pos = v2[j].pos;
			++j;
		} else {
			// Sumar valors si les posicions són iguals
			int suma_valor = v1[i].valor + v2[j].valor;
			if (suma_valor != 0) {	// Només afegir si el valor no és zero
				resultat[k].valor = suma_valor;
				resultat[k].pos = v1[i].pos;
			} else {
				--k;  // Si és zero, no el comptem al resultat
			}
			++i;
			++j;
		}
		++k;  // Incrementar només si s'ha afegit un element
	}

	// Copiar elements restants
	while (i < n1) {
		resultat[k].valor = v1[i].valor;
		resultat[k].pos = v1[i].pos;
		++i;
		++k;
	}
	while (j < n2) {
		resultat[k].valor = v2[j].valor;
		resultat[k].pos = v2[j].pos;
		++j;
		++k;
	}

	// Redimensionar el vector per eliminar espai sobrant
	resultat.resize(k);
	return resultat;
}

// Escriure un vector comprimit
void escriu(const Vec_Com& v) {
	cout << v.size();
	for (size_t i = 0; i < v.size(); ++i) {
		cout << " " << v[i].valor << ";" << v[i].pos;
	}
	cout << endl;
}

int main() {
	int k;
	cin >> k;

	for (int i = 0; i < k; ++i) {
		Vec_Com v1, v2;
		llegeix(v1);
		llegeix(v2);

		Vec_Com resultat = suma(v1, v2);
		escriu(resultat);
	}
}
```

###### Alexandre Gràcia Calvo
