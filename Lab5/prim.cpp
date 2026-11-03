#include <iostream>
using namespace std;

#define INF 9999999
const int V = 8;

// матриця суміжності графа для варіанта 23
int G[V][V] = {
    {0, INF, 1, 6, INF, 4, INF, INF},
    {INF, 0, 8, 8, INF, 3, INF, INF},
    {1, 8, 0, INF, INF, INF, INF, 2},
    {6, 8, INF, 0, 3, INF, INF, INF},
    {INF, INF, INF, 3, 0, 9, 5, INF},
    {4, 3, INF, INF, 9, 0, 7, 1},
    {INF, INF, INF, INF, 5, 7, 0, 7},
    {INF, INF, 2, INF, INF, 1, 7, 0}
};

int main() {
    int kilkist_reber = 0;
    int vybrani[V];
    
    for (int i = 0; i < V; i = i + 1) {
        vybrani[i] = 0;
    }
    
    vybrani[0] = 1; // починаємо з 1 вершини
    
    int suma = 0;
    cout << "Rebro : Vaga" << endl;
    
    while (kilkist_reber < V - 1) {
        int min_vaga = INF;
        int a = 0;
        int b = 0;
        
        for (int i = 0; i < V; i = i + 1) {
            if (vybrani[i] == 1) {
                for (int j = 0; j < V; j = j + 1) {
                    if (vybrani[j] == 0 && G[i][j] != INF && G[i][j] != 0) {
                        if (min_vaga > G[i][j]) {
                            min_vaga = G[i][j];
                            a = i;
                            b = j;
                        }
                    }
                }
            }
        }
        
        cout << a + 1 << " - " << b + 1 << " : " << G[a][b] << endl;
        suma = suma + G[a][b];
        vybrani[b] = 1;
        kilkist_reber = kilkist_reber + 1;
    }
    
    cout << "Zagalna vaga: " << suma << endl;
    return 0;
}
