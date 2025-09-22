# Apunts segona classe PRO1

## Què és la programació?
1. Llenguatge imperatiu: variables, tipus, expressions, condicionals i iteracions
2. Dissenyar procediments per a encapsular solucions de problemes.
3. Metodologia de disseny ascendent.
4. Usar vectors per a guardar informació estructurada.
5. Algorismes fonamentals

## Operacions simples
Una operació simple és aquella que només involucra un sol operador i dos valors (o operands), i retorna un resultat immediat.
```c++
bool major = 5 > 3   // true
bool igual 4 == 4  // true
bool diferent =7 != 2  // true
```

- **Divisió**

    - En C++, la divisió depèn del tipus de dades:

        Divisió entre enters (int):
        ```c++
        int a = 7;
        int b = 2;
        int resultat = a / b;  // resultat = 3
        ```

        

    - Divisió amb nombres de coma flotant (float o double):
        ```c++
        double x = 7.0;
        double y = 2.0;
        double resultat = x / y;  // resultat = 3.5
        ```

        Quan utilitzes float o double, la divisió retorna un nombre amb decimals.

- **Mòdul (%)**

    - El mòdul retorna el **residu** d’una divisió entre enters:
        ```c++
        int a = 7;
        int b = 2;
        int residu = a % b;  // residu = 1
        ```

        7 % 2 dona 1 perquè 7 = 2*3 + 1.

        Només funciona amb nombres enters (int, long, etc.). No es pot fer amb float o double.

- Exemple combinat
    ```c++
    #include <iostream>
    using namespace std;

    int main() {
        int a = 17, b = 5;

        cout << "Divisió: " << a / b << endl;  // 3
        cout << "Mòdul: " << a % b << endl;    // 2

    }
    ```
    Aquí, 17 / 5 = 3 (enter)

    I 17 % 5 = 2 (residu)


## Operadors lògics
Un operador lògic és un símbol o paraula reservada que serveix per combinar o modificar condicions booleanes (condicions que només poden ser true o false).

Dit d’una altra manera: els operadors lògics ens permeten prendre decisions en programes segons si unes condicions es compleixen o no.

1. **and o (&&)**

    etorna true només si ambdues condicions són vertaderes.

    Sintaxi:

    ```c++
    bool resultat = condicio1 and condicio2;
    ```

    - Exemple:
    ```c++
    bool a = true;
    bool b = false;
    bool c = a and b; // false, perquè b és false
    ```


    | a     | b     | a and b |
    |-------|-------|--------|
    | true  | **true**  | **true**   |
    | **true**  | false | false  |
    | false | **true**  | false  |
    | false | false | false  |


2. **or o (||)**

    Retorna true si almenys una de les condicions és vertadera.

    Sintaxi:

    ```c++
    bool resultat = condicio1 or condicio2;
    ```
    Exemple:
    ```c++
    bool a = true;
    bool b = false;
    bool c = a || b; // true, perquè a és true
    ```

    | a | b | a or b |
    |-------|-------|--------|
    | **true** | **true** | **true** |
    | **true** | false | **true** |
    | false | **true** | **true** |
    | false | false | false |

3. **not o (!)**

    Canvia el valor de la condició: true → false i false → true.

    Sintaxi:
    ```c++
    bool resultat = not condicio; //Alternativa: bool resultat = !condicio;
    ```


    Exemple:
    ```c++
    bool a = true;
    bool b = not a; // false
    ```

    | a     | not a    |
    |-------|-------|
    | **true**  | false |
    | false | **true**  |

4. Exemple combinat
    ```c++
    #include <iostream>
    using namespace std;

    int main() {
        bool a = true;
        bool b = false;

        cout << "a and b = " << (a and b) << endl; // 0 (false)
        cout << "a or b = " << (a or b) << endl; // 1 (true)
        cout << "not a = " << (not a) << endl; // 0 (false)

    }
    ```

## Repàs de variables

En C++, els noms de les variables han de complir unes certes regles i tenen algunes limitacions:

1. **Caràcters permesos**:

    Poden contenir lletres (a-z, A-Z), xifres (0-9) i l’underscore (_).

2. **No poden començar per un número.**

    No poden ser paraules reservades:
    Paraules com int, return, if, while, class, etc., no es poden usar com a noms de variables.

3. **Sensibilitat a majúscules i minúscules:**

    Variable, variable i VARIABLE es consideren noms diferents.

4. **Longitud:**

    Teòricament no hi ha un límit estricte de longitud, però alguns compiladors antics poden tenir restriccions pràctiques. 
    Podem formar paraules compostes com per exemple: 
    ```c++
    bool es_cadira; //✅
    bool CadiraGran; //✅
    bool es_una cadira_molt_gran; //⚠️
    bool es_una_cadira_tremendament_gran;//👎
    bool esunacadiraqueesenormeinoemcapalhabitacio;//❌
    ```

5. **Caràcters especials:**

    Només es permet l’underscore (_). Altres caràcters especials com @, #, $, etc., no són vàlids.

6. **Altres convencions:**

    Evitar noms que comencin amb doble underscore (__) o amb underscore seguit de majúscula (_X) ja que estan reservats per a implementacions del compilador.

7. **Important buscar noms simples.**
    Per exemple, per a un nombre auxiliar, li podem dir aux.
    D'altra banda no volem errors causats per complexitat com per exemple:
    ```c++
    bool major_edat = False;
    if(not edat < 18){
        major_edat = True;
    }
    ```
    Alternativa:
    ```c++
    bool major_edat;
    if(edat < 18){
        major_edat = False;
    }
    else{
        major_edat = True;
    }
    ```

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
- Operacions simples
- Operadors lògics
- Repàs variables
- If
- Bucles
- Exercicis


Alexandre Gràcia Calvo
