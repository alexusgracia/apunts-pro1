# Apunts cinquena classe PRO1

## Exemple d'iteratiu que farem en recursiu
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

## Petita introducció a recursivitat


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

## Exemple de potència recursiva

```c++
#include <iostream>
using namespace std;

// Precondició: exp >= 0;
int my_pow(int base, int exp) {
    // Cas base: qualsevol número elevat a 0 és 1
    if (exp == 0)
        return 1;
    // Crida recursiva: base * base^(exp - 1)
    return base * my_pow(base, exp - 1);
}

int main() {
    //Fem un main per a comprovar que és correcte
    cout << my_pow(3, 3) << endl; //Ha de donar 27
    cout << my_pow(2, 4) << endl; //Ha de donar 16

}
```

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



### Hola-adéu *P87523*

```c++
#include <iostream>
using namespace std;

int main(){
    char a, b, c, d;
    a = b = c ='x';
    bool trobat = false;
    //cin >> a >> b >> c;
    while(not trobat and cin >> d and d != '.'){
        if(a == 'h' and b == 'o' and c == 'l' and d == 'a') trobat = true;
        else{
            a = b;
            b = c; 
            c = d;
        }
    }
    if (trobat) cout << "hola" << endl;
    else cout << "adeu" << endl;
}

```


### Primer submot repetit de mida 3 *X98718*

```c++
#include <iostream>
using namespace std;

int main () {
    char x,y,z;
    int pos=0;
    int aaa=0,aab=0,aba=0,abb=0, baa=0,bab=0,bba=0,bbb=0;
    bool found=false; 
    cin >> x >> y >> z;

    while (not found){
        if (x=='a' and y=='a' and z=='a') aaa=aaa+1;
        else if (x=='a' and y=='a' and z=='b') aab=aab+1;
        else if (x=='a' and y=='b' and z=='a') aba=aba+1;
        else if (x=='a' and y=='b' and z=='b') abb=abb+1;
        else if (x=='b' and y=='a' and z=='a') baa=baa+1;
        else if (x=='b' and y=='a' and z=='b') bab=bab+1;
        else if (x=='b' and y=='b' and z=='a') bba=bba+1;
        else if (x=='b' and y=='b' and z=='b') bbb=bbb+1;

        if (aaa==2 or aab==2 or aba==2 or abb==2 or baa==2 or bab==2 or bba==2 or bbb==2) found=true;
        if (found) cout << x << y << z << " " << pos << endl;
        pos=pos+1;
        x=y;
        y=z;
        cin >> z;
    }
}

```

### Felicitat i Tristesa (1) *X64929*

```c++
#include <iostream>
using namespace std;

int main () {
    char n, n0, n1, n2;
    int h = 0, s = 0;
    n0 = n1 = n2 = 'x';
    while (cin >> n) {
        n2 = n1;
        n1 = n0;
        n0 = n;

        if ((n2 == ':') and (n1 == '-') and (n0 == ')')) ++h;
        else if ((n2 == '(') and (n1 == '-') and (n0 == ':')) ++h;
        else if ((n2 == ':') and (n1 == '-') and (n0 == '(')) ++s;
        else if ((n2 == ')') and (n1 == '-') and (n0 == ':')) ++s;
    }

    cout << h << " " << s << endl;
}

```

### Quantes frases hi ha despres d'una pregunta i amb més a's que b's *X49928*

```c++
#include <iostream>
using namespace std;

int main(){
    char c;
    int conta, contb, total;
    conta = contb = total = 0;
    bool trobat = false;
    while(cin >> c){
        if(c == 'a') ++conta;
        else if(c == 'b') ++contb;

        else if(c == '?'){
            if(trobat){
                if(conta>contb) ++total;
            }
            trobat = true;
            conta = contb = 0;
        }
        else if(c == '.'){
            if(trobat){
                if(conta>contb) ++total;
            }
            trobat = false;
            conta = contb = 0;
        }
        else if(c == '!'){
            if(trobat){
                if(conta>contb) ++total;
            }
            trobat = false;
            conta = contb = 0;
        }
    }
    cout << total << endl;
    
    
}

```

### Template *PXXXX*

```c++
#include <iostream>
using namespace std;

int main(){


}

```

Alexandre Gràcia Calvo
