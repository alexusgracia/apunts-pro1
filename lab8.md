# Apunts vuitena classe PRO1

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
	bool primer = true;
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
vector < int > calcula_cims(const vector < int > & v) {
  vector < int > cims(v.size());
  int m = 0;

  for (int i = 1; i < v.size() - 1; ++i) {
    if (v[i] > v[i - 1] and v[i] > v[i + 1]) {
      cims[m] = v[i];
      ++m;
    }
  }
  vector < int > sortida(m);
  for (int i = 0; i < m; ++i) {
    sortida[i] = cims[i];
  }
  return sortida;
}

int main() {
  int n;
  cin >> n;

  vector < int > v(n);
  for (int i = 0; i < n; ++i) {
    cin >> v[i];
  }

  vector < int > cims = calcula_cims(v);

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

### Longitud mitjana i lletra mes frequent *X20419*

```c++
#include <iostream>
#include <vector>
using namespace std;

const int LONG_ABECEDARI = 'z' - 'a' + 1;

char lletra_mes_frequent(const string& s) {
    vector<int> freq(LONG_ABECEDARI, 0);
    for (char c : s) ++freq[c - 'a'];

    int millor = 0;
    for (int i = 1; i < LONG_ABECEDARI; ++i) {
        if (freq[i] > freq[millor]) millor = i;
    }
    return char('a' + millor);
}

int main() {
    int n;
    cin >> n;

    vector<string> v(n);
    int suma = 0;

    for (int i = 0; i < n; ++i) {
        cin >> v[i];
        suma += v[i].size();
    }

    double L = double(suma) / double(n);

    int enters = int(L);
    int decimals = int((L - enters) * 100 + 0.5);

    cout << enters << ".";
    if (decimals < 10) cout << "0";
    cout << decimals << endl;

    for (int i = 0; i < n; ++i) {
        if (v[i].size() >= L) {
            cout << v[i] << ": " << lletra_mes_frequent(v[i]) << endl;
        }
    }
}
```



## Introducció a les matrius en C++

Les **matrius** són una estructura fonamental per emmagatzemar dades en format multidimensional, similar a una taula amb **files** i **columnes**. Són molt útils per resoldre problemes relacionats amb geometria, gràfics o càlculs numèrics.

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

### Com podem assegurar-nos que accedim a posicions vàlides de la matriu?
Ho farem amb una funció que ens retornarà si és una posició vàlida

```cpp
bool pos_valida(const Matriu &m, int fil, int col){
    int pos_fila_min, pos_fila_max, pos_col_min, pos_col_max;
    pos_fila_min = pos_col_min = 0;
    pos_fila_max = m.size()-1;
    pos_col_max = m[0].size()-1;
    if(fil>=pos_fila_min and fil<=pos_fila_max and col>=pos_col_min and col<=pos_col_max){
        return true;
    }
    else return false;

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

Alexandre Gràcia Calvo
