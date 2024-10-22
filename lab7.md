# Apunts setena classe PRO1



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
