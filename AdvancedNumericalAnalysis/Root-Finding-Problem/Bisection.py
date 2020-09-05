# TUGAS ANUMLA 1
# Metode Bisection untuk mencari akar persamaan
# Nama  : Alya Mutiara Firdausyi
# NIM   : 20920007

import math

# Input batas, jumlah iterasi, dan toleransi
a = float(input('a0 = '))
b = float(input('b0 = '))
TOL = float(input('Toleransi = '))

# Fungsi yang digunakan
def fx(x) :
    y = 2*x + 3*math.cos(x) - math.exp(x)
    #y = x**3 + 4*x**2 - 10
    return y

# Cek tanda apakah berlainan
if (fx(a) * fx(b)) >= 0 :
    print('Masukkan batas lagi. f(a) dan f(b) harus berlainan tanda!')
    a = int(input('a0 = '))
    b = int(input('b0 = '))

# Cari akar dengan metode bagi dua
print("i \t p \t fx(p)")
i = 1
toleransi = 1000
while toleransi >= TOL :
    p = (b + a)/2
    fxp = fx(p)
    print(i,p,fxp)
    if fx(a)*fxp < 0 :
        a = a
        b = p
    elif fx(a)*fxp > 0 :
        a = p
        b = b
    elif fxp == 0:
        print('Akar ditemukan')
        print('Nilai akar = ' + str(p))
        break
    else :
        print('Metode bagi dua gagal')
        break
    toleransi = abs((b-a)/2)
    i = i + 1

print('Nilai akar = ' + str(p))