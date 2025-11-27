# Apunts novena classe PRO1

## Repàs de recursivitat, vectors i matrius

### Anagrames *P71916*

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int lletres = ('Z' - 'A' + 'z' - 'a');

int main(){
    int casos;
    cin >> casos;
    while(casos > 0){
        --casos;
        vector <int> abecedari1(lletres, 0);
        vector <int> abecedari2(lletres, 0);
        char lletra = 'a';
        while(lletra != '.'){
            cin >> lletra;
            if (lletra >= 'A' and lletra <= 'Z'){
                abecedari1[lletra - 'A'] = abecedari1[lletra - 'A'] + 1;
            }
            if (lletra >= 'a' and lletra <= 'z'){
                abecedari1[lletra - 'a'] = abecedari1[lletra - 'z'] + 1;
            }
        }
        lletra = 'a';
        while(lletra != '.'){
            cin >> lletra;
            if (lletra >= 'A' and lletra <= 'Z'){
                abecedari2[lletra - 'A'] = abecedari2[lletra - 'A'] + 1;
            }
            if (lletra >= 'a' and lletra <= 'z'){
                abecedari2[lletra - 'a'] = abecedari2[lletra - 'z'] + 1;
            }
        }
        if (abecedari1 == abecedari2) cout << "SI" << endl;
        else cout << "NO" << endl;  
    } 
}
```

### Foc! *P73468*

Exercici per a exemplificar recursivitat i matrius

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Pre: Els índexs i, j han de ser dins de l'interval [0, n-1] i [0, m-1], respectivament.
// Post: Retorna true si la posició (i, j) és vàlida dins la matriu, sinó retorna false.
bool pos_ok(int i, int j, int n, int m) {
	if (i >= 0 and i < n and j >= 0 and j < m) {
		return true;
	} else {
		return false;
	}
}

// Pre: Els valors de n i m són vàlids i indiquen la mida de la matriu.
// Post: Omple la matriu 'bosc' amb les dades llegides des de l'entrada estàndard.
void llegir_matriu(vector<vector<char> >& bosc, int n, int m) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> bosc[i][j];
		}
	}
}

// Pre: La matriu 'bosc' ha estat modificada o omplerta amb els seus valors.
// Post: Imprimeix la matriu 'bosc' a l'entrada estàndard.
void imprimir_matriu(const vector<vector<char> >& bosc, int n, int m) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cout << bosc[i][j];
		}
		cout << endl;
	}
	cout << endl;
}

// Funció per propagar el foc de forma recursiva
// Pre: La matriu 'bosc' ha de ser vàlida, i (i, j) ha de ser una posició dins la matriu.
//      La posició (i, j) ha de ser un arbre ('A') per poder propagar el foc.
// Post: Propaga el foc a les quatre direccions des de la posició (i, j) si és vàlida.
void propagar_foc(vector<vector<char> >& bosc, int i, int j, int n, int m) {
	// Comprovar si la posició és vàlida i conté un arbre
	if (pos_ok(i, j, n, m) and bosc[i][j] == 'A') {
		// Convertir l'arbre en foc
		bosc[i][j] = 'F';

		// Propagar cap a les quatre direccions
		propagar_foc(bosc, i - 1, j, n, m);	 // Esquerra
		propagar_foc(bosc, i + 1, j, n, m);	 // Dreta
		propagar_foc(bosc, i, j - 1, n, m);	 // Amunt
		propagar_foc(bosc, i, j + 1, n, m);	 // Avall

	} else {
		return;
	}
}

// Pre: La matriu 'bosc' conté els arbres (amb 'A' i el foc amb 'F').
// Post: Propaga el foc des de les posicions inicials de foc ('F') i transforma tots els 'F' en '.'
// al final.
void simular_bosc(vector<vector<char> >& bosc, int n, int m) {
	// Buscar tots els arbres encesos ('F') i propagar el foc
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (bosc[i][j] == 'F') {
				// Propagar el foc des d'aquesta posició
				propagar_foc(bosc, i - 1, j, n, m);	 // Esquerra
				propagar_foc(bosc, i + 1, j, n, m);	 // Dreta
				propagar_foc(bosc, i, j - 1, n, m);	 // Amunt
				propagar_foc(bosc, i, j + 1, n, m);	 // Avall
			}
		}
	}

	// Convertir tots els 'F' en '.' (posicions buides)
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (bosc[i][j] == 'F') {
				bosc[i][j] = '.';
			}
		}
	}
}

int main() {
	int n, m;
	while (cin >> n >> m) {
		vector<vector<char> > bosc(n, vector<char>(m));

		llegir_matriu(bosc, n, m);
		simular_bosc(bosc, n, m);
		imprimir_matriu(bosc, n, m);
	}
}
```

### Foc! *P73468_ca*

Solució alternativa:

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Pre: Els índexs i, j han de ser dins de l'interval [0, n-1] i [0, m-1], respectivament.
// Post: Retorna true si la posició (i, j) és vàlida dins la matriu, sinó retorna false.
bool pos_ok(int i, int j, int n, int m) {
	if (i >= 0 and i < n and j >= 0 and j < m) {
		return true;
	} else {
		return false;
	}
}

// Pre: Els valors de n i m són vàlids i indiquen la mida de la matriu.
// Post: Omple la matriu 'bosc' amb les dades llegides des de l'entrada estàndard.
void llegir_matriu(vector<vector<char> >& bosc, int n, int m) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> bosc[i][j];
		}
	}
}

// Pre: La matriu 'bosc' ha estat modificada o omplerta amb els seus valors.
// Post: Imprimeix la matriu 'bosc' a l'entrada estàndard.
void imprimir_matriu(const vector<vector<char> >& bosc, int n, int m) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cout << bosc[i][j];
		}
		cout << endl;
	}
	cout << endl;
}

// Funció per propagar el foc de forma recursiva
// Pre: La matriu 'bosc' ha de ser vàlida, i (i, j) ha de ser una posició dins la matriu.
//      La posició (i, j) ha de ser un arbre ('A') per poder propagar el foc.
// Post: Propaga el foc a les quatre direccions des de la posició (i, j) si és vàlida.
void propagar_foc(vector<vector<char> >& bosc, int i, int j, int n, int m) {
	// Comprovar si la posició és vàlida i conté un arbre
	if (pos_ok(i, j, n, m) and bosc[i][j] == 'A') {
		// Convertir l'arbre en foc
		bosc[i][j] = '.';

		// Propagar cap a les quatre direccions
		propagar_foc(bosc, i - 1, j, n, m);	 // Esquerra
		propagar_foc(bosc, i + 1, j, n, m);	 // Dreta
		propagar_foc(bosc, i, j - 1, n, m);	 // Amunt
		propagar_foc(bosc, i, j + 1, n, m);	 // Avall

	} else {
		return;
	}
}

// Pre: La matriu 'bosc' conté els arbres (amb 'A' i el foc amb 'F').
// Post: Propaga el foc des de les posicions inicials de foc ('F') i transforma tots els 'F' en '.'
// al final.
void simular_bosc(vector<vector<char> >& bosc, int n, int m) {
	// Buscar tots els arbres encesos ('F') i propagar el foc
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (bosc[i][j] == 'F') {
                bosc[i][j] = '.';
				// Propagar el foc des d'aquesta posició
				propagar_foc(bosc, i - 1, j, n, m);	 // Esquerra
				propagar_foc(bosc, i + 1, j, n, m);	 // Dreta
				propagar_foc(bosc, i, j - 1, n, m);	 // Amunt
				propagar_foc(bosc, i, j + 1, n, m);	 // Avall
			}
		}
	}
}

int main() {
	int n, m;
	while (cin >> n >> m) {
		vector<vector<char> > bosc(n, vector<char>(m));

		llegir_matriu(bosc, n, m);
		simular_bosc(bosc, n, m);
		imprimir_matriu(bosc, n, m);
	}
}

```

## Exercicis per a fer avui

### Garbell d'Eratòstenes *P89124*

```c++
#include <iostream>
#include <vector>
using namespace std;

const int MAX = 1000;

void marca_multiples(int i, vector<bool> &garbell)
{
    int n = garbell.size();
    for (int j = 2 * i; j < n; j += i)
        garbell[j] = false;
}

void precalcula_garbell(vector<bool> &garbell)
{
    // garbell [i] indica si i es primer

    garbell[0] = garbell[1] = false;
    for (int i = 2; i < MAX; ++i)
    {
        if (garbell[i])
            marca_multiples(i, garbell);
    }
    return;
}

void imprimeix_n(vector<bool> &garbell, int n)
{
    for (int i = 0; i < n; ++i)
    {
        if (garbell[i])
            cout << "primer ";
        else
            cout << "not primer ";
        cout << i << " ";
        cout << endl;
    }
}

int main()
{
    vector<bool> garbell(MAX * MAX + 1, true);
    // imprimeix_n(garbell, 20);
    precalcula_garbell(garbell);
    // imprimeix_n(garbell, MAX * MAX + 1);
    int n;
    while (cin >> n)
    {
        cout << n;
        if (not garbell[n])
            cout << " no";
        // bool true, es primer, bool false, no es primer ;
        // Haig d'anar del valor minim al maxim al garbell;
        //  El vector ha d'anar entre 0 i un miliÃ³
        cout << " es primer" << endl;
    }
}

```

### Inserció en taula ordenada *P98179*

```c++
#include <vector>
using namespace std;

void insereix(vector<double>& v) {
	// Últim element que hem de col·locar en la posició correcta
	double element = v[v.size() - 1];

	// Comencem des de l'últim element ordenat (penúltim element de v)
	int i = v.size() - 2;

	// Movem els elements més grans cap a la dreta
	while (i >= 0 and v[i] > element) {
		v[i + 1] = v[i];
		i--;
	}

	// Col·loquem l'element a la seva posició correcta
	v[i + 1] = element;
}
```