INF = 9999999
n = 8

# матриця суміжності графа
graf = [
    [0, INF, 1, 6, INF, 4, INF, INF],
    [INF, 0, 8, 8, INF, 3, INF, INF],
    [1, 8, 0, INF, INF, INF, INF, 2],
    [6, 8, INF, 0, 3, INF, INF, INF],
    [INF, INF, INF, 3, 0, 9, 5, INF],
    [4, 3, INF, INF, 9, 0, 7, 1],
    [INF, INF, INF, INF, 5, 7, 0, 7],
    [INF, INF, 2, INF, INF, 1, 7, 0]
]

start = 0
vidstani = []
poperednyky = []
vidvidani = []

i = 0
while (i < n):
    vidstani.append(INF)
    poperednyky.append(-1)
    vidvidani.append(0)
    i = i + 1

vidstani[start] = 0

krok = 0
while (krok < n):
    min_vidstan = INF
    u = -1
    v = 0
    while (v < n):
        if (vidvidani[v] == 0) and (vidstani[v] < min_vidstan):
            min_vidstan = vidstani[v]
            u = v
        v = v + 1

    if (u == -1):
        break

    vidvidani[u] = 1

    v = 0
    while (v < n):
        if (vidvidani[v] == 0) and (graf[u][v] != INF):
            nova_vidstan = vidstani[u] + graf[u][v]
            if (nova_vidstan < vidstani[v]):
                vidstani[v] = nova_vidstan
                poperednyky[v] = u
        v = v + 1

    krok = krok + 1

print("Найкоротші шляхи від вершини 1 (алгоритм Дейкстри):")
v = 1
while (v < n):
    shlyakh = []
    potochna = v
    while (potochna != -1):
        shlyakh.append(potochna + 1)
        potochna = poperednyky[potochna]
    shlyakh.reverse()

    ryadok_shlyakhu = ""
    idx = 0
    while (idx < len(shlyakh)):
        ryadok_shlyakhu = ryadok_shlyakhu + str(shlyakh[idx])
        if (idx < len(shlyakh) - 1):
            ryadok_shlyakhu = ryadok_shlyakhu + " -> "
        idx = idx + 1

    print("1 -> " + str(v + 1) + " : " + ryadok_shlyakhu + " | вага = " + str(vidstani[v]))
    v = v + 1
