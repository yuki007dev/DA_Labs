INF = 9999999
n = 8

# початкова матриця ваг графа
W = [
    [0, INF, 1, 6, INF, 4, INF, INF],
    [INF, 0, 8, 8, INF, 3, INF, INF],
    [1, 8, 0, INF, INF, INF, INF, 2],
    [6, 8, INF, 0, 3, INF, INF, INF],
    [INF, INF, INF, 3, 0, 9, 5, INF],
    [4, 3, INF, INF, 9, 0, 7, 1],
    [INF, INF, INF, INF, 5, 7, 0, 7],
    [INF, INF, 2, INF, INF, 1, 7, 0]
]

# копіювання матриці ваг у матрицю відстаней D
D = []
i = 0
while (i < n):
    ryadok = []
    j = 0
    while (j < n):
        ryadok.append(W[i][j])
        j = j + 1
    D.append(ryadok)
    i = i + 1

# основний цикл алгоритму Флойда
k = 0
while (k < n):
    i = 0
    while (i < n):
        j = 0
        while (j < n):
            if (D[i][k] != INF) and (D[k][j] != INF):
                if (D[i][k] + D[k][j] < D[i][j]):
                    D[i][j] = D[i][k] + D[k][j]
            j = j + 1
        i = i + 1
    k = k + 1

print("Фінальна матриця найкоротших відстаней (алгоритм Флойда):")
i = 0
while (i < n):
    ryadok_vyvodu = ""
    j = 0
    while (j < n):
        if (D[i][j] == INF):
            znach = "INF"
        else:
            znach = str(D[i][j])
        ryadok_vyvodu = ryadok_vyvodu + znach.rjust(4)
        j = j + 1
    print("v" + str(i + 1) + ":" + ryadok_vyvodu)
    i = i + 1
