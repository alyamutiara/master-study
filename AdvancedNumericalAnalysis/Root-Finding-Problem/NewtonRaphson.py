import math
print('--- Metode Newton Raphson ---')

p0 = float(input('Nilai awal = '))
a = float(input('Batas bawah = '))
b = float(input('Batas atas = '))
TOL = float(input('Toleransi = '))
N = int(input('Jumlah iterasi = '))

def f(x) :
    #return 2*x + 3*math.cos(x) - math.exp(x) + x
    #return -2*x - 3*math.cos(x) + math.exp(x) + x
    #return 1/2*(math.exp(x) - 3*math.cos(x))
    #return math.acos((math.exp(x) - 2*x)/3)
    #return math.log(2*x + 3*math.cos(x))
    return 2*x + 3*math.cos(x) - math.exp(x)

def fx(x) :
    #return 3 - 3*math.sin(x) - math.exp(x)
    #return -1 + 3*math.sin(x) + math.exp(x)
    #return (math.exp(x)/2) + (3*math.sin(x)/2)
    #return -1 + 3*math.sin(x) + math.exp(x)*math.log(math.exp(1))
    #return (2 - 3*math.sin(x))/(2*x + 3*math.cos(x))
    return 2 - 3*math.sin(x) - math.exp(x)

i = 1
while i <= N :
    p = p0 - f(p0)/fx(p0)
    print(i,p0,p)

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