# Apunts quinta classe PRO1


# Petita introducció a funcions

Una **funció** en C++ és un bloc de codi que realitza una tasca específica. 

Les funcions ajuden a estructurar el codi en parts reutilitzables. 

Tota funció té tipus de retorn, el nom i els paràmetres.

### Tipus de funcions en C++

1. **Funció `void`**: No retorna cap valor. Es fa servir per a funcions que només executen accions.

```c++
void saludar() {  
    cout << "Hola a tothom!" << endl;  
}  
```

2. **Funció que retorna un enter (`int`)**: Retorna un valor de tipus enter. S'utilitza quan necessitem que la funció ens torni un valor numèric sencer.

```c++
int sumar(int a, int b) {  
    return a + b;  
}  
```

3. **Funció que retorna un booleà (`bool`)**: Retorna un valor lògic `true` o `false`. Es fa servir sovint per a funcions que realitzen comprovacions.

```c++
bool es_parell(int num) {  
    return num % 2 == 0;  
}  
```

4. **Funció que retorna un nombre decimal (`double`)**: Retorna un valor decimal. Es fa servir per càlculs amb números amb decimals.

```c++
double dividir(double a, double b) {  
    return a / b;  
}  
```

5. **Funció que retorna una cadena de text (`string`)**: 

```c++

string retornar_salutacio() {  
    return "PRO1 mola!";  
}  
```

6. **Podem fer funcions dins de funcions? __Sí!__ **

```c++
#include <iostream>
using namespace std;


bool es_parell(int num) {  
    return num % 2 == 0;  
}  

void imprimeix_si_es_parell(int a){
    bool b = es_parell(a);
    if (b){
        cout << "Es parell" << endl;
    }
    else cout << "No és parell" << endl;
}


int main(){
    int num1 = 12;
    imprimeix_si_es_parell(num1);

    int num2 = 15;
    imprimeix_si_es_parell(num2);

    int num3 = 7;
    imprimeix_si_es_parell(num3);

}
```

# Exercici nombres estranys amb funcions:
```c++
#include <iostream>
using namespace std;

int my_pow(int digit, int digits){
    int resultat = 1;
    for (int i = 0; i < digits; i++) {
        resultat = resultat * digit;
    }
    return resultat;
}

int n_digits(int n) {
    int digits = 0;
    while (n > 0) {
        digits++;
        n = n/10;
    }
    return digits;
}

int elevar_numero_i_suma(int num, int digits) {
    int suma = 0;
    while (num > 0) {
        int digit = num % 10;
        suma = suma + my_pow(digit, digits);
        num = num/10;
    }
    return suma;
}

int main() {

    int n;

    while(cin >> n){

        int digits = n_digits(n);
        
        int suma = elevar_numero_i_suma(n, digits);
        
        if (suma == n) {
            cout << "strange number: "<< n  << endl;
        } else {
            cout << "not strange number: "<< n << endl;
        }
    }
}
```

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
