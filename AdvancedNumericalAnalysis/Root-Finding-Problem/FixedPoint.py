# TUGAS ANUMLA 1
# Metode Titik Tetap untuk mencari akar persamaan
# Nama  : Alya Mutiara Firdausyi
# NIM   : 20920007

import math

# Input variabel
p0 = float(input('Nilai awal = '))
a = float(input('Batas bawah = '))
b = float(input('Batas atas = '))
TOL = float(input('Toleransi = '))
N = int(input('Iterasi = '))

# Fungsi yang digunakan
def gx(x) :
    # Ganti dengan persamaan yang digunakan
    #return 2*x + 3*math.cos(x) - math.exp(x) + x
    #return -2*x - 3*math.cos(x) + math.exp(x) + x
    #return 1/2*(math.exp(x) - 3*math.cos(x))
    #return math.acos((math.exp(x) - 2*x)/3)
    return math.log(2*x + 3*math.cos(x))
    
# Iterasi metode titik tetap
i = 1
print('i \t p0 \t g(p)')
while i <= N :
    p = gx(p0)
    print(i, p0, p)

    if abs(p-p0) < TOL :
        print('Akar ditemukan')
        print('Nilai akar = ' + str(p))
        break
    elif p < a or p > b :
        print('Perhitungan akar keluar batas [' + str(a)+ ',' + str(b) + ']')
        break
    elif i == N :
        print('Metode gagal setelah ' + str(N) + ' iterasi')
        print('Akar tidak ditemukan')
        break

    p0 = p
    i = i + 1
