# Apunts setena classe PRO1

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


## Resum de la sessió

Contingut:
- Exercicis


###### Alexandre Gràcia Calvo
