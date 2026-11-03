#include <iostream>
#include <algorithm>

using namespace std;

struct Rebro {
    int u;
    int v;
    int vaga;
};

// сортування ребер за вагою
bool porivnyat(Rebro a, Rebro b) {
    return a.vaga < b.vaga;
}

int batko[9];

int znajty(int i) {
    if (batko[i] == i) {
        return i;
    }
    batko[i] = znajty(batko[i]);
    return batko[i];
}

void obyednat(int a, int b) {
    int koren_a = znajty(a);
    int koren_b = znajty(b);
    batko[koren_a] = koren_b;
}

int main() {
    int n = 8;
    int m = 13;
    
    Rebro spysok[13] = {
        {1, 3, 1},
        {6, 8, 1},
        {3, 8, 2},
        {2, 6, 3},
        {4, 5, 3},
        {1, 6, 4},
        {5, 7, 5},
        {1, 4, 6},
        {6, 7, 7},
        {7, 8, 7},
        {2, 3, 8},
        {2, 4, 8},
        {5, 6, 9}
    };
    
    sort(spysok, spysok + m, porivnyat);
    
    for (int i = 1; i <= n; i = i + 1) {
        batko[i] = i;
    }
    
    int suma = 0;
    int dodano = 0;
    
    cout << "Rebro : Vaga" << endl;
    
    for (int i = 0; i < m; i = i + 1) {
        int u = spysok[i].u;
        int v = spysok[i].v;
        
        if (znajty(u) != znajty(v)) {
            obyednat(u, v);
            cout << u << " - " << v << " : " << spysok[i].vaga << endl;
            suma = suma + spysok[i].vaga;
            dodano = dodano + 1;
            if (dodano == n - 1) {
                break;
            }
        }
    }
    
    cout << "Zagalna vaga: " << suma << endl;
    return 0;
}
