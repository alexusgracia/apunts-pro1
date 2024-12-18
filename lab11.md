# Apunts onzena classe PRO1

## Algorismes fonamentals

### Cerca dicotòmica

La **cerca dicotòmica**, també coneguda com a **cerca binària**, és un algorisme eficient per trobar la posició d’un element en una seqüència ordenada. Aquest mètode redueix repetidament l’interval de cerca a la meitat fins que es localitza l’element o es determina que no està present.

#### Funcionament

1. **Condició inicial**: La llista ha d’estar **ordenada**.
2. **Divisió de l’interval**: Comencem amb dos extrems, `inici` i `final`, que delimiten l’interval on busquem l’element.
3. **Punt mig**: Calculem la posició del mig amb la fórmula:
   \[
   \text{mig} = \text{inici} + \frac{\text{final} - \text{inici}}{2}
   \]
4. **Comparació**:
   - Si l’element al punt `mig` és el que busquem, retornem la seva posició.
   - Si l’element al punt `mig` és més gran que el valor buscat, descartem la `meitat superior`.
   - Si l’element al punt `mig` és més petit que el valor buscat, descartem la `meitat inferior`.
5. **Repetició**: Continuem dividint l’interval fins que l’element es trobi o fins que `inici > final`.

## Complexitat
- **Pitjor cas**: \(O(\log_2 n)\), ja que l’interval es redueix a la meitat a cada pas.
- **Millor cas**: \(O(1)\), si trobem l’element a la primera comparació.
- **Memòria**: La cerca dicotòmica només requereix espai constant \(O(1)\).

### Cerca dicotòmica *P81966*

```cpp
#include <iostream>
#include <vector>
using namespace std;

void retorna(const vector<double>& v){
    for (int i = 0; i < v.size(); ++i){
        cout << v[i];
    }
    cout << endl;
    return;
}

int posicio(double x, const vector<double>& v, int esq, int dre){
    
    if (esq > dre) return -1;
    int meitat = (esq + dre)/2;
    
    if (x > v[meitat]){
        return posicio(x, v, meitat +1, dre);
    }
    else if (x < v[meitat]){
        return posicio(x, v, esq, meitat - 1);
    }
    else return meitat;
}

int main(){
    int n;
    cin >> n;
    vector <double> v(n);
    for (int i = 0; i < n-1; ++i){
        cin >> v[i];
    }
    double nombre;
    cin >> nombre;
    cout << posicio(nombre, v, 0, n);
    //retorna(v);
}
```

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

### Mergesort

Solució del professor Jorge Castro
```c++
#include <iostream>
#include <vector>
using namespace std;


//pre: n > 0
//post: retorna un vector de tamanno n leido de la entrada
vector<int> lee_vector(int n) {
    vector<int> v(n);
    for (int i = 0; i < n; ++i) cin >> v[i];
    return v;
}


//pre:---
//post: valores del vector escritos en output
void escribir_vector(const vector<int>& v) {
    int n = v.size();
    cout << v[0];
    for (int i = 1; i < n; ++i)
    cout << ' ' << v[i];
    cout << endl;
}



// Pre: 0 <= iz <= mit <= de < v.size() i v[iz..mit] y v[mit+1..de], por separado, 
//      estan ordenados de menor a mayor
// Post: los valores de v[iz..de] son los iniciales, pero ordenados de menor a
//       a mayor y el resto de elementos de v no ha cambiado
void fusionar(vector<int>& v, int iz, int mit, int de) {
    vector<int> aux(de - iz + 1);
    int i = iz;      //indice para primer segmento
    int j = mit + 1; //indice para segundo segmento
    int k = 0;       //indice para aux
    while (i <= mit and j <= de) {
        if (v[i] <= v[j]) {
            aux[k] = v[i];
            ++i;
        }
        else {
            aux[k] = v[j];
            ++j;
        }
        ++k;
    }
    while (i <= mit) {
        aux[k] = v[i];
        ++k;
        ++i;
    }
    while (j <= de) {
        aux[k] = v[j];
        ++k;
        ++j;
    }
    //volcamos el resultado de la fusion en v[iz..de]
    int s = aux.size(); //s es de - iz + 1
    for (k = 0; k < s; ++k) v[iz + k] = aux[k];
}


// Pre: iz y de son posiciones validas de v 
// Post: los valores  de v[iz..de] son los  iniciales, pero ordenados de menor a mayor
void mergesort(vector<int>& v, int iz, int de) {
    if (iz < de) {
        int mit = (iz + de)/2;
        mergesort(v, iz, mit);
        //por hipotesis de induccion, v[iz..mit] tiene los valores originales ordenados
        mergesort(v, mit + 1, de);
        //por hipotesis de induccion, v[mit+1..de] tiene los valores originales ordenados
        fusionar(v, iz, mit, de);
    }
}



int main() {
   int n;
   cin >> n;
   vector<int> v = lee_vector(n);
   mergesort(v,0,v.size() - 1);
   escribir_vector(v);
}
```

### Insert sort

Solució del professor Jorge Castro
```c++
void insert_sort(vector<int>& v) {
    int n = v.size();
    for (int i = 1; i < n; ++i) {
        int x = v[i];
        int j = i;
        while (j > 0 and v[j - 1] > x) {
            v[j] = v[j - 1];
            --j;
        }
        v[j] = x;
    }
}
```

### Sort time
Solució del professor Jorge Castro per a la comparació de temps per inserció, quick sort i mergesort

```c++
#include <iostream> 
#include <vector>
#include <algorithm> 
#include <sys/time.h> 
using namespace std; 




//pre: n > 0
//post: retorna un vector de tamanno n leido de la entrada
vector<int> lee_vector(int n) {
    vector<int> v(n);
    for (int i = 0; i < n; ++i) cin >> v[i];
    return v;
}


//pre:---
//post: valores del vector escritos en output
void escribir_vector(const vector<int>& v) {
    int n = v.size();
    cout << v[0];
    for (int i = 1; i < n; ++i)
        if (i > 0 and i%25 == 0) cout << endl << v[i];
        else cout << ' ' << v[i];
    cout << endl;  
}


////////////////////////////////////////////////////////////////////////////
//////////////////////Mergesort////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////



// Pre: 0 <= iz <= mit <= de < v.size() i v[iz..mit] y v[mit+1..de], por separado, 
//      estan ordenados de menor a mayor
// Post: los valores de v[iz..de] son los iniciales, pero ordenados de menor a
//       a mayor y el resto de elementos de v no ha cambiado
void fusionar(vector<int>& v, int iz, int mit, int de) {
    vector<int> aux(de - iz + 1);
    int i = iz;      //indice para primer segmento
    int j = mit + 1; //indice para segundo segmento
    int k = 0;       //indice para aux
    while (i <= mit and j <= de) {
        if (v[i] <= v[j]) {
            aux[k] = v[i];
            ++i;
        }
        else {
            aux[k] = v[j];
            ++j;
        }
        ++k;
    }
    while (i <= mit) {
        aux[k] = v[i];
        ++k;
        ++i;
    }
    while (j <= de) {
        aux[k] = v[j];
        ++k;
        ++j;
    }
    //volcamos el resultado de la fusion en v[iz..de]
    int s = aux.size(); //s es de - iz + 1
    for (k = 0; k < s; ++k) v[iz + k] = aux[k];
}



// Pre: iz y de son posiciones validas de v 
// Post: los valores  de v[iz..de] son los  iniciales, pero ordenados de menor a mayor
void mergesort(vector<int>& v, int iz, int de) {
    if (iz < de) {
        int mit = (iz + de)/2;
        mergesort(v, iz, mit);
        //por hipotesis de induccion, v[iz..mit] tiene los valores originales ordenados
        mergesort(v, mit + 1, de);
        //por hipotesis de induccion, v[mit+1..de] tiene los valores originales ordenados
        fusionar(v, iz, mit, de);
    }
}



///////////////////////////////////////////////////////////////////////////
/////////////////////////////Insercion/////////////////////////////////////
//////////////////////////////////////////////////////////////////////////

// Pre:  ---
// Post: v contiene los valores iniciales y  esta ordenado de menor a mayor
void insert_sort(vector<int>& v) {
    int n = v.size();
    for (int i = 1; i < n; ++i) {
        int x = v[i];
        int j = i;
        while (j > 0 and v[j - 1] > x) {
            v[j] = v[j - 1];
            --j;
        }
        v[j] = x;
    }
}
   
///////////////////////////////////////////////////////////////////////////
////////////////////Quicksort//////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////


//pre: e y d son indices validos de v y e < d y pivote es v[e]
//post: v[e..d] contiene los valores originales reordenados en dos partes
//v[e..mid] contiene los menores o iguales a pivote
//v[mid] es pivote
//v[mid + 1..d] los mayores
//y e <= mid <= d
void separa(vector<int>& v, int pivote, int e, int d, int& mid) {
    int ee = e;
    while (e < d) {
        while (e < d and v[e] <= pivote) ++e;
        while (e < d and v[d] > pivote) --d;
        if (e < d) swap(v[e], v[d]);
    }
    if (v[e] > pivote) mid = e - 1;
    else mid = e;  
    //mid es la  ultima posicion  con valor  <= que pivote
    swap(v[ee], v[mid]);
}
            


// Pre: 0<=e<=d<v.size()
// Post: els elements de v[e..d] son els inicials, pero ordenats creixentment
void quicksort(vector<int>& v, int e, int d) {
    if (e < d) {
        int mid;
        separa(v, v[e], e, d, mid);
        quicksort(v, e, mid - 1);
        quicksort(v, mid + 1, d);
    }
}



int main() {
   cout.setf(ios::fixed);
   cout.precision(10);
   int n;
   cin >> n;
   vector<int> v = lee_vector(n);
   vector<int> clon_v = v;
   //calculamos tiempo cuando ordenamos por insercion
   struct timeval start, stop;
   //escribir_vector(v);
   gettimeofday(&start, NULL);
   insert_sort(v);
   gettimeofday(&stop, NULL);
   double time_elapsed = stop.tv_sec - start.tv_sec;
   time_elapsed += (stop.tv_usec - start.tv_usec)*1e-6;
   cout << "Time elapsed insert_sort: " << time_elapsed;
   cout << " sec" << endl;
   //escribir_vector(v);
   //calculamos tiempo cuando ordenamos por fusion
   v = clon_v;
   //escribir_vector(v);
   gettimeofday(&start, NULL);
   mergesort(v, 0, n - 1);
   gettimeofday(&stop, NULL);
   time_elapsed = stop.tv_sec - start.tv_sec;
   time_elapsed += (stop.tv_usec - start.tv_usec)*1e-6;
   cout << "Time elapsed mergesort: " << time_elapsed;
   cout << " sec" << endl;
   //escribir_vector(v);
   //calculamos tiempo cuando ordenamos  con sort():
   v = clon_v;
   //escribir_vector(v);
   gettimeofday(&start, NULL);
   sort(v.begin(), v.end());
   gettimeofday(&stop, NULL);
   time_elapsed = stop.tv_sec - start.tv_sec;
   time_elapsed += (stop.tv_usec - start.tv_usec)*1e-6;
   cout << "Time elapsed sort(): " << time_elapsed;
   cout << " sec" << endl;
   //escribir_vector(v);   
   //calculamos tiempo cuando ordenamos  con quicksort():
   v = clon_v;
   gettimeofday(&start, NULL);
   quicksort(v, 0, n -1);
   gettimeofday(&stop, NULL);
   time_elapsed = stop.tv_sec - start.tv_sec;
   time_elapsed += (stop.tv_usec - start.tv_usec)*1e-6;
   cout << "Time elapsed quicksort(): " << time_elapsed;
   cout << " sec" << endl;
   //escribir_vector(v);
}

```


## Exercicis per a fer avui

### Garbell d'Eratòstenes *P89124*

```c++
#include <iostream>
#include <vector>
using namespace std;

const int MAX = 1000;

void marca_multiples(int i, vector<bool>& garbell){
    int n = garbell.size();
    for (int j = 2*i; j < n; j += i)
	garbell[j] = false;
}

vector<bool> precalcula_garbell(int n){
    //garbell [i] indica si i es primer
    vector<bool> garbell(n, true);
    
    garbell[0] = garbell[1] = false;
    for (int i = 2; i < MAX; ++i){
	if (garbell[i]) marca_multiples(i, garbell);
    }
	return garbell;
}

int main(){
    vector<bool> es_primer = precalcula_garbell(MAX*MAX + 1);
    
    int n;
    while (cin >> n){
	cout << n;
	if (not es_primer[n]) cout << " no";
	//bool true, es primer, bool false, no es primer ;
	//Haig d'anar del valor minim al maxim al garbell;
	// El vector ha d'anar entre 0 i un miliÃ³
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

###### Alexandre Gràcia Calvo
