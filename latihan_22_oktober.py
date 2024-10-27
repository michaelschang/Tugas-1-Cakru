# Ini merupakan projek latihan soal dari modul praktikum mata kuliah Berpikir Komputasional.
# Link modul: https://drive.google.com/file/d/10Yr8_8-u5acNolUqGt9jIdPXS2wvj2tf/view?usp=sharing

# LATIHAN 1
# Source: 1.6.4 | Hal. 9

awal = int(input("Masukkan koordinat katak: "))
a = int(input("Masukkan panjang lompatan katak ke kanan: "))
b = int(input("Masukkan panjang lompatan katak ke kiri: "))

if awal >= 0:
    if awal % 2 == 0 :
        k = a * b
    else :
        k = a * 2
else:
    if awal % 3 == 0 :
        k = b * 2
    else :
        k = a * b

steps_kiri = k // 2
steps_kanan = k - steps_kiri
perpindahan_kiri = b * steps_kiri
perpindahan_kanan = a * steps_kanan
akhir = awal + perpindahan_kanan - perpindahan_kiri
print(f"Koordinat katak sekarang adalah {akhir}")

# LATIHAN 2
# Source: 2.4.1 | Hal. 14

N = int(input("Masukkan N: "))
if N < 0 :
    print("- infinity")
else :
    i = 0
    while 10 ** i < N :
        i += 1
    print(10 ** i)

# LATIHAN 3
# Source: 2.4.2 | Hal. 14

M = int(input("Masukkan M: "))
baris = ""
for i in range(M) :
    baris += str(i+1) + " "
    print(baris)

# LATIHAN 4
# Source: 2.4.3 | Hal. 14

O = int(input("Masukkan O: "))
T = [int(input("")) for i in range(O)]
dibalik = ""
for i in reversed(T) :
    dibalik += str(i) + " "
print("Hasil dibalik:")
print(dibalik)

# LATIHAN 5
# Source: 2.4.4 | Hal. 15

# metode tabel
A = [] # ini diperlukan untuk metode sort
tabel_A = [[], []]
len_A = int(input("Masukkan banyaknya elemen A: "))
for i in range(len_A) :
    A.append(int(input(f"Masukkan elemen A ke-{i+1}: "))) # bisa assign input ini ke var. saja sebenarnya
    if A[i] not in tabel_A[0] :
        tabel_A[0].append(A[i])
        tabel_A[1].append(1)
    else :
        j = tabel_A[0].index(A[i])
        tabel_A[1][j] += 1

B = []
tabel_B = [[], []]
len_B = int(input("Masukkan banyaknya elemen B: "))
for i in range(len_B) :
    B.append(int(input(f"Masukkan elemen B ke-{i+1}: ")))
    if B[i] not in tabel_B[0] :
        tabel_B[0].append(B[i])
        tabel_B[1].append(1)
    else :
        j = tabel_B[0].index(B[i])
        tabel_B[1][j] += 1

anagram = True

for i in range(len(tabel_A[0])) :
    if tabel_A[0][i] in tabel_B[0] :
        j = tabel_B[0].index(tabel_A[0][i])
        if tabel_A[1][i] != tabel_B[1][j] :
            anagram = False
            break
    else :
        anagram = False
        break

if anagram == True :
    print("B adalah anagram dari A")
else :
    print("B bukan anagram dari A")


# metode sort
AA = A
BB = B
for i in range(len_A - 1) :
    for j in range(len_A - 1 - i) :
        if AA[j] > AA[j + 1] :
            AA.insert(j + 2, AA[j])
            AA.pop(j)
for i in range(len_B - 1) :
    for j in range(len_B - 1 - i) :
        if BB[j] > BB[j + 1] :
            BB.insert(j + 2, BB[j])
            BB.pop(j)
if AA == BB :
    print("B adalah anagram dari A")
else :
    print("B bukan anagram dari A")

# LATIHAN 6
# Source: 2.4.5 | Hal. 15

len_kata = int(input("Masukkan panjang string: "))
kata = str(input("Masukkan string: "))
palindrom = True
for i in range(len_kata // 2) :
    if kata[i] != kata[len_kata - i] :
        palindrom = False
        break
print(f"{kata} adalah palindrom") if palindrom == True else print(f"{kata} bukan palindrom")

# LATIHAN 7
# Source: 2.4.6 | Hal. 16

potongan = int(input("Masukkan banyak potongan lego: "))
sisi = 1
kubus = 0
while sisi*sisi*sisi <= potongan :
    potongan -= sisi*sisi*sisi
    kubus += 1
    sisi += 1
print(f"Tuan Leo dapat membuat {kubus} kubus.")

# LATIHAN 8
# Source: 2.4.7 | Hal. 17

star = [' ' for i in range(61)]
for y in range (15, -16, -1) :
    for x in range (30, -31, -1) :
        if (x/2)**2 + (5*y/4 - 2*(abs(x)**(1/2)))**2 <= 120 :
            star[x+30] = '*'
    print(*star)
    star = [' ' for i in range(61)]

# LATIHAN 9
# Source: 2.4.8 | Hal. 17

bilangan = int(input("Masukkan N: "))
cek = bilangan
faktor_prima = [0 for i in range(bilangan)]
ada_prima = False
jumlah_prima = 0

for i in range(2, bilangan) :
    j = i
    while j > 1 :
        if cek / j == cek // j :
            cek = j
        j -= 1
    if cek == i :
        faktor_prima[i] = i
        ada_prima = True
        jumlah_prima += 1
    cek = bilangan

if ada_prima :
    laporan = "Faktor primanya adalah "
    count = 0
    for j, i in enumerate(faktor_prima, start = 1) :
        if i != 0 :
            laporan += str(i)
            count += 1
            if count != jumlah_prima :
                laporan += ", "
            else :
                break
elif bilangan == 1 :
    laporan = f"{bilangan} bukanlah bilangan prima"
else :
    laporan = f"{bilangan} adalah bilangan prima"

print(laporan)

# LATIHAN 10
# Source: 2.4.9 | Hal. 18

nilai = int(input("Masukkan nilai N: "))
L = [int(input(f"Masukkan nilai ke-{i}: ")) for i in range(1, nilai + 1)]
potongan = 0
total = 0

for i in range(nilai - 1) :
    for j in range(nilai - i) :
        for k in range(j, j + i + 1) :
            total += L[k]
        if total % 2 == 0 :
            potongan += 1
        total = 0
print(f"Terdapat {potongan} potong list yang jumlahnya genap")

# Di bawah ini code untuk jika list nya
# berisi bilangan asli berurutan.
# Ini menggunakan trik matematik sedikit.
#for i in range(1, nilai) :
#    if i != 2 :
#        batas = nilai - i + 1
#        if i % 2 == 0 :
#            potongan += batas
#        else :
#            potongan += (batas + 1) // 2
#potongan -= 1