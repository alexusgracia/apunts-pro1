# Apunts novena classe PRO1


## Introducció a les matrius en C++

Les **matrius** són una estructura fonamental per emmagatzemar dades en format bidimensional, similar a una taula amb **files** i **columnes**. Són molt útils per resoldre problemes relacionats amb geometria, gràfics o càlculs numèrics.

Cal tenir en compte que una matriu és un vector de vectors, per tant podem tenir n-dimensions.

### Declaració i inicialització d'una matriu sense usar typedef

```c++
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    // Crear una matriu com a vector de vectors
    vector< vector<int> > mat(n, vector<int>(m)); // ULL a la separació entre '>'

    // Llegir la matriu
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> mat[i][j];
        }
    }

    // Imprimir la matriu
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
}
```
### Què és el `typedef`?
El `typedef` s'utilitza per crear un alias o nom alternatiu per a un tipus de dades en C++, millorant la llegibilitat i mantenibilitat del codi. 

### Declaració i inicialització d'una matriu usant typedef

Una matriu en C++ es declara com un vector n-dimensional, especificant el nombre de files i columnes.

**Exemple 1:**
```c++
typedef vector< vector<int> > Matriu; //IMPORTANT: Els espais entre el símbol '>'
```

**Exemple 2:**
```c++
typedef vector<int> fila;
typedef vector<fila> Matriu;

```

### Com accedim a un element d'una matriu?

És molt fàcil, només hem de posar el valor de fila i columna que tenim:
```c++
//Codi previ
int i = 2;
int j = 3;
mat[i][j] //O mat[2][3]
```

### Exemple: Volem llegir una matriu i imprimir-la sense usar funcions

```c++
#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> fila;
typedef vector<fila> Matriu;
//Alternativa: typedef vector< vector<int> > Matriu
int main() {
    int n, m;
    cin >> n >> m;
    Matriu mat(n, fila(m));

    // Llegir la matriu
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> mat[i][j];
        }
    }

    // Imprimir la matriu
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
}
```


### Exemple: Volem llegir una matriu i imprimir-la usant funcions

```c++
#include <iostream>
#include <vector>

using namespace std;

typedef vector<int>	 fila;
typedef vector<fila> Matriu;

void llegir_matriu(Matriu& mat, int n, int m) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> mat[i][j];
		}
	}
}

void imprimir_matriu(const Matriu& mat, int n, int m) {//ULL AL CONST!! El posem perquè no volem cometre l'error de modificar-la quan escrivim
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cout << mat[i][j] << " ";
		}
		cout << endl;
	}
}

int main() {
	int n, m;
	cin >> n >> m;
	Matriu mat(n, fila(m));
	llegir_matriu(mat, n, m);
	imprimir_matriu(mat, n, m);
}
```

### Matrius de n-dimensions
Les matrius de n dimensions (o arrays multidimensionals) permeten emmagatzemar elements en més d'una dimensió. En lloc de tenir només files i columnes (com una matriu 2D), una matriu de n dimensions permet representar dades en més de dues direccions. Cada dimensió addicional permet afegir una nova "capa" o "nivell" d'indexació.


#### Exemple en 3 dimensions

```c++
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int x, y, z;
    cin >> x >> y >> z; // Dimensions de la matriu

    // Crear una matriu 3D
    vector<vector<vector<int> > > mat(x, vector<vector<int> >(y, vector<int>(z)));

    // Llegir els valors de la matriu
    for (int i = 0; i < x; ++i) {
        for (int j = 0; j < y; ++j) {
            for (int k = 0; k < z; ++k) {
                cin >> mat[i][j][k];
            }
        }
    }

    // Imprimir els valors de la matriu
    for (int i = 0; i < x; ++i) {
        cout << "Capa " << i + 1 << ":" << endl;
        for (int j = 0; j < y; ++j) {
            for (int k = 0; k < z; ++k) {
                cout << mat[i][j][k] << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
}
```

## Exercicis per a fer avui


### Matriu transposta *P27498_ca*

```c++
//Matriu transposta
#include <iostream>
#include <vector>
using namespace std;


typedef vector< vector<int> > Matriu;

void swap(int& a, int& b) {
    int c = a;
    a = b;
    b = c;
}

void transposa(Matriu& m) {
    int n = m.size();
    for (int i = 0; i < n - 1; ++i) {
        for (int j = i + 1; j < n; ++j) {
            swap(m[i][j], m[j][i]);
        }
    }
}
```

### Control C401B *P42596*

```c++
#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<int> > Matriu;

// Aquesta funció calcula el mínim i màxim d'una matriu no buida.
void min_max(const Matriu& mat, int& minim, int& maxim) {
	minim = mat[0][0];
	maxim = mat[0][0];

	// Iterem sobre les files.
	for (int i = 0; i < mat.size(); ++i) {
		// Iterem sobre les columnes.
		for (int j = 0; j < mat[i].size(); ++j) {
			if (mat[i][j] < minim) {
				minim = mat[i][j];
			}
			if (mat[i][j] > maxim) {
				maxim = mat[i][j];
			}
		}
	}
}

int main() {
	int n, m;
	int difer_max = -1;		// Per guardar la diferència màxima trobada.
	int millor_matriu = 0;	// Índex de la matriu amb la diferència màxima.
	int index = 0;			// Per iterar per les matrius.

	while (cin >> n >> m) {
		Matriu mat(n, vector<int>(m));
		// Lectura de les files.
		for (int i = 0; i < n; ++i) {
			// Lectura de les columnes.
			for (int j = 0; j < m; ++j) {
				cin >> mat[i][j];
			}
		}

		int minim, maxim;
		min_max(mat, minim, maxim);
		int diferencia = maxim - minim;

		if (diferencia > difer_max) {
			difer_max = diferencia;
			millor_matriu = index;
		}
		++index;
	}

	cout << "la diferencia maxima es " << difer_max << endl;
	cout << "la primera matriu amb aquesta diferencia es la " << millor_matriu + 1 << endl;

}
```

###### Alexandre Gràcia Calvo
