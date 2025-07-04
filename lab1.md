# Apunts primera classe PRO1

## [Web de l'assignatura](https://pro1.cs.upc.edu/)
https://pro1.cs.upc.edu/

## Llenguatge Markdown

[Cheatsheet](https://www.markdownguide.org/cheat-sheet/)

'#' Hola Permet crear un títol

Els '#' són niuables

Exemple:

## Títol 2
### Títol 3
#### Títol 4
##### Títol 5

Negreta: **Hola**

Italic: *Cursiva*

> Blockquote

Ordered List:
1. Primer element
2. Segon element
3. Tercer element

Unordered List:
- Primer
- Segon
- Tercer

Task list:
- [x] Exemple1
- [ ] Exemple2

    Línia Horitzontal:
    ---

Altres exemples:



    Programar és divertit.

~~Programar és avorrit.~~

Taula:

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

## Comandes linux



```bash
cd                  # Canviar de directori
cd ..               # Canviem a una carpeta enrere
cd exemple/         # Canviem a la carpeta exemple
ls                  # Llistem el contingut del directori
ls -la              # Llistem el contingut del directori i veiem els arxius ocults i atributs
mkdir exemple       # Crear una carpeta
rmdir -r exemple    # Eliminar una carpeta
touch file1         # Creem un arxiu anomenat file1
cp file1 file2      # Copiem el contingut de l'arxiu file1 a file2
mv file1 exemple/   # Movem el fitxer file1 a dins de la carpeta exemple
rm file1            # Esborrem el fitxer file1
cat file1           # Veiem el contingut de l'arxiu per consola
code &              # Obrim el vscode, l'& del final serveix per a què si tanquem la consola no es tanca el vscode 
```
### Tipus de variables
|Paraula | Tipus    |
|--------|----------|
|`bool`  | Booleà   |
|`int`   | enter    |
|`double`| decimal  |
|`char`  | caràcter |
|`string`| cadena de caràcters|

### Com declarem i inicialitzem?
```bash
int a; #Declaració
a = 5; #Inicialització
# Podem declarar i inicialitzar al mateix temps? Depèn
int a, b, c;
a = b = c = 0;
# Alternativa
int a, b, c;
a = 5;
b = 3;
c = 12;
```

### Com crear el meu primer programa c++

```bash
cd ~
mkdir pro1                              # Crear carpeta
cd pro1                                 # Canviar a la carpeta
touch hello_world.cc                    # Crear un fitxer
p1++ hello_world.cc -o hello_world.x    # Compilar amb el compilador de pro1
g++ hello_world.cc -o hello_world.x     # Compilar amb el compilador general
./hello_world.x                         # Executar el programa
```
```c++
#Contingut del programa hello_world.cc
#include iostream
using namespace std
int main() {

    # El meu primer programa en c++
    cout << "Hello World! " << endl;
}
```
## Exercicis fets a classe:

### Hola i Adeu! *X64734_ca*
```c++
#include <iostream>
using namespace std;

int main(){
    cout << "Hola i Adeu!" << endl;
}
```
### Promedio *P99182_es* 
```c++
#include <iostream>
using namespace std;

int main(){
    double a,b;
    cin >> a >> b;
    cout << (a + b)/2 << endl;
}
```

### Quants segons són? *P70955_ca*
```c++
#include <iostream>
using namespace std;

int main (){
    /*
    //Alternativa 1
    int anys, dies, hores, minuts, segons;
    cin >> anys >> dies >> hores >> minuts >> segons;
    int anys_segons = anys*365*24*60*60;
    int dies_segons = dies*24*60*60;
    int hores_segons = hores*60*60;
    int minuts_segons = minuts*60;
    int total_segons = anys_segons + dies_segons + hores_segons + minuts_segons + segons;
    cout << total_segons << endl;
    */
    /*
    //Alternativa 2
    int anys, dies, hores, minuts, segons;
    cin >> anys >> dies >> hores >> minuts >> segons;
    int suma_segons;
    suma_segons = (((((((anys*365)+dies)*24)+hores)*60)+minuts)*60) + segons;
    cout << suma_segons << endl; 
    */
    int anys, dies, hores, minuts, segons;
    cin >> anys >> dies >> hores >> minuts >> segons;
    int segons_any, segons_dia, segons_hores, segons_minuts;
    segons_any = 1*365*24*60*60;
    segons_dia = 1*24*60*60;
    segons_hores = 1*60*60;
    segons_minuts = 1*60;
    cout << segons + segons_minuts*minuts + segons_hores*hores+segons_dia*dies + segons_any*anys << endl;
}
```

### Control C102A *P82374_ca*
>Aquest m'he oblidat de fer-lo avui a classe
```c++
#include <iostream>
using namespace std;


int main() {

    int x, a, b, c, d;
    cin >> x >> a >> b >> c >> d;

    if ((x >= a and x <= b) or (x >= c and x <= d)) {
        cout << "si" << endl;
        }
    else{
        cout << "no" << endl;
    }
}
```
## Resum de la sessió
Contingut:
- Presentació
- Comandes bàsiques linux
- Visual Studio Code
- Primer programa en c++
- Jutge
- Configuració [*clang-format*](https://pro1.cs.upc.edu/recursos/clang-format)
- Exercicis

> **IMPORTANT!!** No us oblideu de [Configurar windows a casa](https://pro1.cs.upc.edu/pdfs/LAB-ConfigurarEntornWindowsACasa.pdf)


Alexandre Gràcia Calvo

