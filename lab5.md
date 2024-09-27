# Apunts quinta classe PRO1


## Exercicis per a fer avui


### Màxim de cada seqüència *P71753_ca*

```c++
#include <iostream>

using namespace std;

int main(){
    int n;
    while (cin >> n){
        int primer;
        cin >> primer;
        int max = primer;
        for (int i = 0; i < n-1; ++i){
            int x;
            cin >> x;
            if (x > max) max = x;
        }
        cout << max << endl;
    }
}
```

### Línies ordenades (1) *P89979_ca*

```c++
#include <iostream>
#include <string>
using namespace std;

int main(){
    int n;
    string paraula1, paraula2;
    bool trobada = false;
    for (int i = 1; cin >> n and not trobada; ++i){
	paraula1 = "a";
	bool ordenada = true;
	while (n > 0){
	    cin >> paraula2;
	    if (paraula1 > paraula2) ordenada = false;
	    paraula1 = paraula2;
	    --n;
	}
	if (ordenada){
	    cout << "La primera linia ordenada creixentment es la ";
	    cout << i << ".";
	    trobada = true;
	}
    }
    if (not trobada) cout << "No hi ha cap linia ordenada creixentment.";
    cout << endl;
}
```


## Resum de la sessió

Contingut:
- Exercicis


###### Alexandre Gràcia Calvo
