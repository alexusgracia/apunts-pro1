# Apunts sisena classe PRO1


## Exercicis per a fer avui


### Funció per la suma del mínim i el màxim de tres enters  *X46340*

```c++
#include <iostream>
using namespace std;

int sum_min_max(int x, int y, int z){
    int min, max;
    if(x <= y and x <= z) min = x;
    else if(y<=z) min = y;
    else min = z;
    
    if(x >= y and x >= z) max = x;
    else if(y>=z) max = y;
    else max = z;    
    return min + max;
}

int main(){
    cout << sum_min_max(736,291,348) << endl;
    cout << sum_min_max(12,-569,666) << endl;

}

```

### Factorial iteratiu *P57474*

```c++
#include <iostream>
using namespace std;

int factorial(int n){
    int sum = 1;
    for (int i = 1; i <= n; ++i){
        sum = sum*i;
    }
    return sum;
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


## Resum de la sessió

Contingut:
- Exercicis


###### Alexandre Gràcia Calvo
