# Apunts vuitena classe PRO1





## Exercicis per a fer avui


### Inversió de seqüències *P67268_ca*

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    while (cin >> n){
	vector <int> v(n);
	for (int i = 0; i < n; ++i) cin >> v[i];
	bool primer = true;
	for (int i = n - 1; i >= 0; --i){
	    if (primer){
	    cout << v[i];
	    primer = false;
	    }
	    else cout << " " << v[i];
	}
	cout << endl;
    }
}
```

### Vector muntanyos *X41120_ca*

```c++
#include <iostream>
#include <vector>
using namespace std;

// PRE: |v| ≥ 3
// POST: retorna un vector amb l’alçada de tots els cims de v (en el mateix ordre)
vector<int> calcula_cims(const vector<int>& v) {
	vector<int> cims(v.size());
	int			m = 0;

	for (int i = 1; i < v.size() - 1; ++i) {
		if (v[i] > v[i - 1] and v[i] > v[i + 1]) {
			cims[m] = v[i];
			++m;
		}
	}
	vector<int> sortida(m);
	for (int i = 0; i < m; ++i) {
		sortida[i] = cims[i];
	}
	return sortida;
}

int main() {
	int n;
	cin >> n;

	vector<int> v(n);
	for (int i = 0; i < n; ++i) {
		cin >> v[i];
	}

	vector<int> cims = calcula_cims(v);

	cout << cims.size() << ":";

	if (!cims.empty()) {
		for (int i = 0; i < cims.size(); ++i) {
			cout << ' ' << cims[i];
		}
		cout << endl;

		int ultim_cim = cims[cims.size() - 1];

		bool mes_alts_trobats = false;
		bool primer = true;
		for (int i = 0; i < cims.size(); ++i) {
			if (cims[i] > ultim_cim) {
				if (primer) {
					cout << cims[i];
					primer = false;
				} else {
					cout << ' ' << cims[i];
				}
				mes_alts_trobats = true;
			}
		}
		if (!mes_alts_trobats) {
			cout << '-' << endl;
		} else {
			cout << endl;
		}
	} else {
		cout << endl;
		cout << '-' << endl;
	}
}

```



Alexandre Gràcia Calvo
