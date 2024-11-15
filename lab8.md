# Apunts vuitena classe PRO1

## Passar per valor i per referència en funcions en C++

En C++, es poden passar arguments a les funcions de dues maneres principals: **per referència** i **per valor**. 

<div style="text-align: center;">
  <video width="560" height="300" controls>
    <source src="https://img-9gag-fun.9cache.com/photo/az9pOnp_460svvp9.webm" type="video/webm">
    Si no es veu aquest vídeo, prem aquí: ![Meme coffee](https://img-9gag-fun.9cache.com/photo/az9pOnp_460svvp9.webm)
  </video>
</div>


![https://img-9gag-fun.9cache.com/photo/az9pOnp_460svvp9.webm](/imatges/coffee.webm)


### Passar per valor

Quan es passa un argument per valor, es crea una còpia de l'argument original dins de la funció. Això vol dir que qualsevol canvi fet sobre el paràmetre dins de la funció no afectarà el valor original fora de la funció.

```cpp
#include <iostream>

void incrementarPerValor(int num) {
    num++;  // Incrementa la còpia local de num
    cout << "Dins de la funció (per valor): " << num << endl;
}

int main() {
    int x = 5;
    incrementarPerValor(x);  // Es passa el valor de x
    cout << "Fora de la funció: " << x << endl;  // x segueix sent 5
}
```

### Passar per referència
Quan es passa un argument per referència, es passa l'adreça de la variable original. Això vol dir que qualsevol canvi fet sobre el paràmetre dins de la funció afectarà directament la variable original.

```cpp
#include <iostream>

void incrementarPerReferencia(int& num) {
    num++;  // Incrementa el valor original de num
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


## Què és un vector?

Un **vector** és una estructura de dades dinàmica proporcionada per la llibreria estàndard de C++ (`vector`). Els vectors permeten emmagatzemar un conjunt d'elements del mateix tipus i ajustar la seva mida automàticament durant l'execució del programa.

Característiques principals:
- **Redimensionament automàtic**: La mida d'un vector pot augmentar o disminuir segons calgui.
- **Accés aleatori**: Es pot accedir a qualsevol element utilitzant el seu índex.
- **Gestió automàtica de memòria**: No cal preocupar-se per alliberar memòria (ja ho veurem més endavant).
- **Si no fem bé l'accés petarà**: Si intentem accedir a una posició d'un vector que no existeix tindrem un bonic error.

### Tipus de vectors

Els vectors en C++ poden emmagatzemar elements de qualsevol tipus de dades, incloent-hi tipus primitius com `int`, `char`, i `double`, així com tipus compostos com `string` o objectes personalitzats(que veurem més endavant, tuples, matrius, etc)

#### Vectors de tipus primitiu:

```cpp
vector<int> enters; //Vector de tipus int [1, 2, 3, 4, 5]
vector<bool> booleans; //Vector de tipus bool [true, false, true, true]
vector<char> caracters; //Vector de tipus char, fixeu-vos que una string és una cadena de caràcters ['a', 'b', 'c', 'd']
vector<string> cadenes;// Vector de tipus string ["Charmander", "Bulbasaur", "Squirtle", "Pikachu"]

```

### Com s'inicialitza un vector?

Un **vector** en C++ es pot inicialitzar de diverses maneres

#### Inicialització amb una mida fixa

Es pot declarar un vector amb una mida fixa, amb tots els elements inicialitzats a un valor per defecte (0 en el cas dels enters):

```cpp
vector<int> v(5); // Un vector de 5 elements inicialitzats a 0
```
#### Inicialització amb una mida fixa i valor específic

```cpp
vector<int> v(5, 0); // Un vector de 5 elements inicialitzats a 0
```

#### Inicialització amb valors

```cpp

vector<int> v(3); // Un vector amb 3 elements específics
v[0] = 1;
v[1] = 2;
v[2] = 3
```

#### Inicialització mitjançant un altre vector

```cpp

vector<int> v2(v); // Crea un nou vector v2 amb els mateixos elements que v
```

### Com s'esborra un vector?

```cpp
vector<int> v; // Suposem que conté [1, 2, 3]
v.clear(); // El vector ara està buit
```

### Funcions principals de vectors
1. **size()**: Retorna la mida actual del vector (el nombre d'elements):
   
```cpp
vector<int> v; // Suposem que conté [1, 2, 3]
cout << "Mida del vector: " << v.size() << endl; // Mostra: 3

```
2. **empty()**: Retorna true si està buit, altrament false

```cpp
vector<int> v;//No hem declarat tamany ni contingut
if (v.empty()) {
    cout << "El vector està buit." << endl;
}
```
3. N'hi ha més, però estan prohibides (de moment) a pro1.


### Exemple d'inicialització i accés

```cpp
#include <iostream>
#include <vector>

int main() {
    vector<int> v(5);
	v[0] = 1;
	v[1] = 2;
	v[2] = 3;
	v[3] = 4;
	v[4] = 5;

    for (int i = 0; i < v.size(); ++i) {
        cout << v[i] << ' ';
    }
    cout << endl;

}

```
### Problema de l'exemple d'incialització i accés
Us heu fixat que en l'exemple d'inicialització tindrem sempre un espai al final? Com ho solucionem?

1␣2␣3␣4␣5**␣**⤶


Volem tenir això:
1␣2␣3␣4␣5⤶

#### Solució: Escriure un espai abans de cada element que no sigui el primer


```cpp
#include <iostream>
#include <vector>

int main() {
    vector<int> v(5);
	v[0] = 1;
	v[1] = 2;
	v[2] = 3;
	v[3] = 4;
	v[4] = 5;
    bool primer = true;
    for (int i = 0; i < v.size(); ++i) {
        if (primer){
            cout << v[i];
            primer = false;
        }
        else {
            cout << ' ' << v[i]; //Escriurem un espai abans d'escriure cada element
        }
    }

}
```


## Exercicis per a fer avui


### Inversió de seqüències *P67268_ca*

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    while (cin >> n){
	vector <int> v(n);
	for (int i = 0; i < n; ++i) cin >> v[i];
	int primer = true;
	for (int i = n - 1; i >= 0; --i){
	    if (primer){
	    cout << v[i];
	    primer = false;
	    }
	    else cout << " " << v[i];
	}
	cout << endl;
    }
}
```

### Vector muntanyos *X41120_ca*

```c++
#include <iostream>
#include <vector>
using namespace std;

// PRE: |v| ≥ 3
// POST: retorna un vector amb l’alçada de tots els cims de v (en el mateix ordre)
vector<int> calcula_cims(const vector<int>& v) {
	vector<int> cims(v.size());
	int			m = 0;

	for (int i = 1; i < v.size() - 1; ++i) {
		if (v[i] > v[i - 1] and v[i] > v[i + 1]) {
			cims[m] = v[i];
			++m;
		}
	}
	vector<int> sortida(m);
	for (int i = 0; i < m; ++i) {
		sortida[i] = cims[i];
	}
	return sortida;
}

int main() {
	int n;
	cin >> n;

	vector<int> v(n);
	for (int i = 0; i < n; ++i) {
		cin >> v[i];
	}

	vector<int> cims = calcula_cims(v);

	cout << cims.size() << ":";

	if (!cims.empty()) {
		for (int i = 0; i < cims.size(); ++i) {
			cout << ' ' << cims[i];
		}
		cout << endl;

		int ultim_cim = cims[cims.size() - 1];

		bool mes_alts_trobats = false;
		bool primer = true;
		for (int i = 0; i < cims.size(); ++i) {
			if (cims[i] > ultim_cim) {
				if (primer) {
					cout << cims[i];
					primer = false;
				} else {
					cout << ' ' << cims[i];
				}
				mes_alts_trobats = true;
			}
		}
		if (!mes_alts_trobats) {
			cout << '-' << endl;
		} else {
			cout << endl;
		}
	} else {
		cout << endl;
		cout << '-' << endl;
	}
}

```

### EXTRA: Per què no podem fer `vector<int> v = {1, 2, 3};` amb la versió de p1++ de PRO1?

En versions antigues de C++, com C++98 i C++03, la sintaxi `vector<int> v = {1, 2, 3};` no és vàlida perquè aquestes versions no suporten l'ús de *llistes d'inicialització* amb claus `{}` per a inicialitzar contenidors com `vector`.

A pro1 usem les següents funcions incloses dins a un alias per a compilar:
`alias p1++="g++ -ansi -O2 -DNDEBUG -D_GLIBCXX_DEBUG -Wall -Wextra -Werror -Wno-uninitialized -Wno-sign-compare -Wshadow"`

Compilem fent: `p1++ program.cc -o program.x`, però el que passa internament substitueix el p1++ per l'alias que li hem assignat abans.

L'opció ``-ansi`` força el compilador a utilitzar C++98 (o més específicament, un subconjunt de C++03 sense extensions GNU). Això desactiva totes les característiques introduïdes en C++11 i versions posteriors, incloent-hi les llistes d'inicialització.

- Les *llistes d'inicialització* es van introduir a C++11 amb el concepte d'*initializer lists* (veure `initializer_list`).
- En C++98 i C++03, només es podien inicialitzar vectors utilitzant els seus constructors o assignant valors de forma explícita després de declarar-los.

###### Alexandre Gràcia Calvo
