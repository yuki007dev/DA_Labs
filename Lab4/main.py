slova = ['ЯК', 'ДОБРЕ', 'ВЧИШСЯ', 'ТО', 'ЛЕГКО', 'ПРАЦЮЄТЬСЯ', 'А', 'ЛІНУЄШСЯ', 'БІДУЄТЬСЯ']

alfavit = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10,
    'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20,
    'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28, 'Ш': 29, 'Щ': 30,
    'Ь': 31, 'Ю': 32, 'Я': 33
}

def klyuch_slova(slovo):
    suma = 0
    for bukva in slovo:
        if bukva in alfavit:
            suma = suma + alfavit[bukva]
    return suma

def hesh_dilennya(k, rozmir):
    return k % rozmir

def hesh_mnozhennya(k, rozmir):
    a = 0.6180339887
    drib = (k * a) % 1.0
    return int(rozmir * drib)

print("розрахунок ключів слів:")
for s in slova:
    k = klyuch_slova(s)
    h_div = hesh_dilennya(k, 13)
    h_mul = hesh_mnozhennya(k, 16)
    print(s, "k =", k, "h_div =", h_div, "h_mul =", h_mul)

# 1. відкрите хешування
def open_hash_table(words, m, hash_type="div"):
    tablytsya = []
    i = 0
    while i < m:
        tablytsya.append([])
        i = i + 1

    for s in words:
        k = klyuch_slova(s)
        if hash_type == "div":
            adresa = hesh_dilennya(k, m)
        else:
            adresa = hesh_mnozhennya(k, m)
        tablytsya[adresa].append(s)
    return tablytsya

def poshuk_open(tbl, shukane, m, hash_type="div"):
    k = klyuch_slova(shukane)
    if hash_type == "div":
        adresa = hesh_dilennya(k, m)
    else:
        adresa = hesh_mnozhennya(k, m)
    
    spysok = tbl[adresa]
    kilkist_porivnyan = 0
    znajdeno = False
    idx = 0
    while idx < len(spysok):
        kilkist_porivnyan = kilkist_porivnyan + 1
        if spysok[idx] == shukane:
            znajdeno = True
            break
        idx = idx + 1
    return znajdeno, adresa, kilkist_porivnyan

tbl_open_div = open_hash_table(slova, 13, "div")
tbl_open_mul = open_hash_table(slova, 16, "mul")

print("\nвідкрита таблиця (ділення, m=13):")
i = 0
while i < 13:
    print(str(i).zfill(2) + ":", tbl_open_div[i])
    i = i + 1

# 2. закрите хешування
def closed_hash_table(words, m, hash_type="div"):
    tablytsya = [None] * m
    for s in words:
        k = klyuch_slova(s)
        if hash_type == "div":
            poch_adresa = hesh_dilennya(k, m)
        else:
            poch_adresa = hesh_mnozhennya(k, m)
        krok = 0
        while krok < m:
            potik_adresa = (poch_adresa + krok) % m
            if tablytsya[potik_adresa] is None:
                tablytsya[potik_adresa] = s
                break
            krok = krok + 1
    return tablytsya

def poshuk_closed(tbl, shukane, m, hash_type="div"):
    k = klyuch_slova(shukane)
    if hash_type == "div":
        poch_adresa = hesh_dilennya(k, m)
    else:
        poch_adresa = hesh_mnozhennya(k, m)
    
    kilkist_porivnyan = 0
    znajdeno = False
    krok = 0
    while krok < m:
        potik_adresa = (poch_adresa + krok) % m
        kilkist_porivnyan = kilkist_porivnyan + 1
        if tbl[potik_adresa] is None:
            break
        if tbl[potik_adresa] == shukane:
            znajdeno = True
            break
        krok = krok + 1
    return znajdeno, potik_adresa, kilkist_porivnyan

tbl_closed_div = closed_hash_table(slova, 13, "div")
tbl_closed_mul = closed_hash_table(slova, 16, "mul")

print("\nзакрита таблиця (ділення, m=13):")
i = 0
while i < 13:
    val = tbl_closed_div[i]
    if val is None:
        val = "(NULL)"
    print(str(i).zfill(2) + ":", val)
    i = i + 1

# 3. порівняння кількості порівнянь
print("\nпошук слів та порівняння:")
print("слово | open_div | open_mul | closed_div | closed_mul")

sum_od = 0
sum_om = 0
sum_cd = 0
sum_cm = 0

for s in slova:
    _, _, c_od = poshuk_open(tbl_open_div, s, 13, "div")
    _, _, c_om = poshuk_open(tbl_open_mul, s, 16, "mul")
    _, _, c_cd = poshuk_closed(tbl_closed_div, s, 13, "div")
    _, _, c_cm = poshuk_closed(tbl_closed_mul, s, 16, "mul")

    sum_od = sum_od + c_od
    sum_om = sum_om + c_om
    sum_cd = sum_cd + c_cd
    sum_cm = sum_cm + c_cm

    print(s, c_od, c_om, c_cd, c_cm)

n = len(slova)
print("\nсума порівнянь:", sum_od, sum_om, sum_cd, sum_cm)
print("середня кількість:", round(sum_od / n, 2), round(sum_om / n, 2), round(sum_cd / n, 2), round(sum_cm / n, 2))
