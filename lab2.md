# Apunts segona classe PRO1

## Què és la programació?
1. Llenguatge imperatiu: variables, tipus, expressions, condicionals i iteracions
2. Dissenyar procediments per a encapsular solucions de problemes.
3. Metodologia de disseny ascendent.
4. Usar vectors per a guardar informació estructurada.
5. Algorismes fonamentals

## Què és un condicional?

Un condicional és una estructura de control que permet que el programa prengui decisions basades en una condició lògica (true o false). 

Aquesta condició determina si un bloc de codi s'executarà o no. 

``if`` 

``else if``

``else``

```c++
int x = 10;
if (x > 5) {
    cout << "x és més gran que 5";
} else {
    cout << "x és menor o igual a 5";
}
```


## Què és un while

while és una estructura de control iterativa que permet repetir un bloc de codi mentre una condició lògica sigui certa (true).

Quan la condició es torna falsa, el bucle s'atura. 

Aquesta estructura és útil quan no es coneix prèviament el nombre d'iteracions que cal realitzar, i depèn d'una condició canviant dins del bucle.

## Exemple de while 

```c++
int i = 0;
while (i < 5) {
    cout << i << endl;
    i++;
}
```

## Exercicis per a fer avui

### Número del revés *P50327_ca*
```c++
#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    bool continua = true;
    while(n >= 0 and continua){
        cout << n%10;
        n = n/10;
        if(n == 0) continua = false;
    }
    cout << endl;
}
```

### Control C201A *P38614_ca*
```c++
#include <iostream>
using namespace std;

int main () {
    int a;
    int posicio = 1;
    int resultat = 0;
    cin >> a;
    int aux = a;
    while(a != 0){
        if(posicio%2 == 1){
            int residu = a%10;
            resultat = resultat + residu;
        }
        a = a/10;
        ++posicio;
    }
}
```
## Resum de la sessió

Contingut:
- Què és la programació?
- If
- Bucles
- Exercicis


###### Alexandre Gràcia Calvo
