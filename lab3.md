# Apunts tercera classe PRO1


## Què és un **while**

**while** és una estructura de control iterativa que permet repetir un bloc de codi mentre una condició lògica sigui certa (true).

Quan la condició es torna falsa, el bucle s'atura. 

Aquesta estructura és útil quan no es coneix prèviament el nombre d'iteracions que cal realitzar, i depèn d'una condició canviant dins del bucle.

## Exemple de **while** 

```c++
int i = 0;
while (i < 5) {
    cout << i << endl;
    i++;
}
```

## Recorreguts

### Mitjançant una sentinella

```c++
char sentinella = '#' // O qualsevol lletra, string, nombre, etc.
char c;
cin >> c;
while(c!=sentinella){
    //Tractem el caràcter c

    cin >> c;
}

```

### Entrades infinites

```c++

char c;
while(cin >> c){
    //Tractem el caràcter c
}

```

### Nombre d'entrades

```c++
int n;
char c;
cin >> n;
while(n>0){
    //Stuff here
    cin >> c;
    --n; //És a dir, restem 1 al nombre d'iteracions
    
}
```

## Què és un **for**

**for** és una altra estructura de control iterativa, però a diferència del while, s'utilitza quan es coneix prèviament el nombre d'iteracions o quan aquestes poden estar controlades per un comptador.

El bucle for es divideix en tres parts: inicialització, condició, i actualització. Durant cada iteració, es comprova la condició, i si és certa, es continua executant el bloc de codi.

## Exemple de **for** 

```c++
for (int i = 0; i < 5; i++) {
    cout << i << endl;
}
```

## Quan s'ha de fer servir un **while** i quan un **for**?

No hi ha una norma escrita en general, sempre es pot usar un while en comptes d'un for i un for en comptes d'un while, però la simplicitat d'un o l'altre es fa més evident conforme es va programant i adquirint experiència.

En resum es podria simplificar:

- **`while`** s'utilitza quan la condició depèn d'un factor que pot canviar de manera dinàmica dins del bucle.

- **`for`** és més adequat quan tenim un nombre d'iteracions fix o quan el control de les iteracions és més previsible.


## Loops inside loops

```c++
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        cout << i << "," << j << endl;
    }
}
```

## Exercicis per a fer avui

### Potències *P79817_ca*
```c++
#include <iostream>
using namespace std;

int main(){

    int a, b;
    
    while (cin >> a){
        cin >> b;
        int aux;
        aux = a;
        if (b == 0) aux = 1;
        while (b > 1){
            aux = aux * a;
            --b;
        }
        cout << aux << endl;
    }
}
```

### Control C202E *P32533_ca*
```c++
#include <iostream>
using namespace std;

int main(){
    int n, aux;
    cin >> n;
    aux = n;
    while (aux > 0){
	for(int i = 0; i < (aux - 1); ++i){
	    cout << "+";
	}
	cout << "/";
	for (int j = 0; j < (n - aux) ;++j){
	    cout << "*";
	}
	--aux;
	cout << endl;
    }
}
```

## Resum de la sessió

Contingut:
- Què és un while?
- Condicions de finalització.
- Què és un for?
- Quan escollir entre un for i un while?
- Exercicis


Alexandre Gràcia Calvo
