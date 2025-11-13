# Apunts sisena classe PRO1

## Repàs de recursivitat


La **recursivitat** és un concepte fonamental en informàtica i matemàtiques, que permet resoldre problemes mitjançant la definició d'una solució en termes de si mateixa. En programació, una funció es considera recursiva quan s'invoca a si mateixa durant la seva execució.

### Components d'una Funció Recursiva

1. **Cas Base**: És la condició que permet que la funció deixi de cridar-se a si mateixa. Sense un cas base, la funció pot entrar en un bucle infinit. És el més important de definir.

2. **Crida Recursiva**: És l'execució de la funció dins de la seva pròpia definició, amb arguments modificats que **apropen** la solució al cas base.

### Exemple: Càlcul del Factorial

Un exemple comú de recursivitat és el càlcul del factorial d'un nombre `n` (denotat com `n!`). La definició recursiva és:

- Cas base: `0! = 1`
- Crida recursiva: `n! = n * (n - 1)!`

Per exemple, el factorial de 5 és 120:
I les crides recursives serien:
- 5x 4!
- 5x4x 3!
- 5x4x3x 2!
- 5x4x3x2x 1!
- 5x4x3x2x1x 0! (I aquí es compleix el cas base i tornem enrera fent la multiplicació).
- 5x4x3x2x1x 1
- 5x4x3x2x 1
- 5x4x3x 2
- 5x4x 6
- 5x 24
- 120

### Implementació en C++

```c++
int factorial(int n) {
    if (n == 0) {
        return 1; // Cas base
    }
    return n * factorial(n - 1); // Crida recursiva
}

int main(){
    cout << factorial(1) << endl;
    cout << factorial(2) << endl;
    cout << factorial(3) << endl;
    cout << factorial(4) << endl;
    cout << factorial(5) << endl;
    cout << factorial(6) << endl;

}
```

## Exemples recursivitat

```c++
#include <iostream>
using namespace std;

void es_creixent(int n){
  if (n!= 1) es_creixent(n-1);
  cout << n;
  return;
}
void es_decreixent(int n){
  if (n == 0) return;
  else{
    cout << n;
    es_decreixent(n-1);
  }
}

void es_decreixent2(int n){
  if (n != 0){
    cout << n;
    es_decreixent(n-1);
  }
}


int main(){
  es_creixent(10);
  cout << endl;
  es_decreixent(10);
  cout << endl;
  es_decreixent2(10);
  cout << endl;
}

```

###  Canvis de base *P56549*

```c++

#include <iostream>
using namespace std;

void int_to_binari(int n) {
    if (n >= 2) {
        int_to_binari(n / 2);
    }
    cout << n % 2;
}

void int_to_octal(int n) {
    if (n >= 8) {
        int_to_octal(n / 8);
    }
    cout << n % 8;
}

void int_to_hexadecimal(int n) {
    if (n >= 16) {
        int_to_hexadecimal(n / 16);
    }
    int digit = n % 16;
    if (digit < 10) {
        cout << char('0' + digit);
    } else {
        cout << char('A' + digit - 10);
    }
}

int main() {
    int n;
    while (cin >> n) {
        cout << n << " = ";
        int_to_binari(n);
        cout << ", ";
        int_to_octal(n);
        cout << ", ";
        int_to_hexadecimal(n);
        cout << endl;
    }
    return 0;

}
```


### Exercicis exemple *P24381*

```c++
#include <iostream>
#include <string>

using namespace std;

void cross(int n, char c){
  //PRE: n>3 i n senar
  //POST: creu amb n línies escrites per cout amb caracter c
  for(int i = 0; i < n; ++i){
    if(i == n/2){
      for(int j = 0; j < n; ++j){
        cout << c;
      }
      cout << endl;
    }
    else{
      for(int j = 0; j < n; ++j){
        if(j == n/2)cout << c;
        else if(j < n/2) cout << ' ';
      }
      cout << endl;
    }
  }
}

int main() {
  cross(5, 'X');
}

```



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

### Factorial recursiu  *P12509*

```c++
#include <iostream>
using namespace std;

int factorial(int n){
    if ( n<=1) return 1;
    else return n * factorial(n-1);
}

int main(){
    int n;
    cin >> n;
    cout << factorial(n) << endl;
}

```

### Girant una llista de paraules (1)	 *P26041*

```c++


#include <iostream>
#include <string>

using namespace std;

void funcio_recursiva() {
	string paraula;
	if (cin >> paraula) { // Llegim una paraula de l'entrada
		funcio_recursiva();	// Cridem recursivament la funció
		cout << paraula << endl; // Imprimim la paraula després de la crida recursiva
	}
}

// Main per a testejar 
int main() {
	funcio_recursiva();
}
```

### EXTRA: Per què no podem fer `vector<int> v = {1, 2, 3};` amb la versió de p1++ de PRO1?

En versions antigues de C++, com C++98 i C++03, la sintaxi `vector<int> v = {1, 2, 3};` no és vàlida perquè aquestes versions no suporten l'ús de *llistes d'inicialització* amb claus `{}` per a inicialitzar contenidors com `vector`.

A pro1 usem les següents funcions incloses dins a un alias per a compilar:
`alias p1++="g++ -ansi -O2 -DNDEBUG -D_GLIBCXX_DEBUG -Wall -Wextra -Werror -Wno-uninitialized -Wno-sign-compare -Wshadow"`

Compilaríem fent: `p1++ program.cc -o program.x`, però el que passa internament substitueix el p1++ per l'alias que li hem assignat abans.

L'opció ``-ansi`` força el compilador a utilitzar C++98 (o més específicament, un subconjunt de C++03 sense extensions GNU). Això desactiva totes les característiques introduïdes en C++11 i versions posteriors, incloent-hi les llistes d'inicialització.

- Les *llistes d'inicialització* es van introduir a C++11 amb el concepte d'*initializer lists* (veure `initializer_list`).
- En C++98 i C++03, només es podien inicialitzar vectors utilitzant els seus constructors o assignant valors de forma explícita després de declarar-los.

**És per això que us recomano que useu el compilador g++, perquè no agafem dependència del p1++ i aprenguem a programar amb tots els casos i limitacions en ment :)**

I a més, podrem fer vector<int> v = {1, 2, 3}; i declarem i inicialitzem a la vegada.

Alexandre Gràcia Calvo
