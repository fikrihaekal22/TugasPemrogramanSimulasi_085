# PROGRAM KORELASI HAEKAL#


# -----------------------------------------#

#penjelasan membuat fungsi untuk mengambil nilai dan menghitung nilai,

#ngitung 1 nilai
def nilai1(inp):
    arr = []
    out = 0
    for x in range(n):
        arr.append(inp[x])
        out += arr[x]
    return out, arr

#ngitung 2 nilai
def nilai2(inpX, inpY):
    arr = []
    out = 0
    for x in range(n):
        arr.append((inpX[x] * inpY[x]))
        out += arr[x]
    return out, arr

#ngitung kuadrat nilai
def nilaipow1(inp):
    arr = []
    out = 0
    #untuk menghitung nilainya
    for x in range(n):
        arr.append((inp[x] ** 2))
        out += arr[x]
    return out, arr

#operasi perhitungan
def cariHasil(inpX, inpY, inpN):
    Yi = nilai1(inpY)[0]
    Yi2 = nilaipow1(inpY)[0]
    Xi2 = nilaipow1(inpX)[0]
    Xi = nilai1(inpX)[0]
    XiYi = nilai2(inpX, inpY)[0]
    out = round(((inpN * XiYi) - (Xi * Yi)) / ((((inpN * Xi2) - (Xi ** 2)) * ((inpN * Yi2) - (Yi ** 2))) ** 0.5), 3)
    return out
# NRP : 152018085

#pengkategorian dari hasil nilai r
def skalaguilford(inp):
    if (inp < 0.2) and (inp >= 0):
        skala = 'Sangat Lemah'
    elif (inp < 0.4) and (inp >= 0.2):
        skala = 'Lemah'
    elif (inp < 0.6) and (inp >= 0.4):
        skala = 'Sedang'
    elif (inp < 0.8) and (inp >= 0.6):
        skala = 'Baik'
    elif (inp <= 1.0) and (inp >= 0.8):
        skala = 'Sangat Baik'
    return skala


def inputdata():
    global n
    print('Inputkan nilai x')
    while True:
        entry = input('num : ')
        if entry == '':
            break
        try:
            x.append(int(entry))
        except:
            print("Nilai tidak valid!")
    print('Inputkan nilai y')
    while True:
        entry = input('number : ')
        if entry == '':
            break
        try:
            y.append(int(entry))
        except:
            print("Nilai tidak valid!")
    n = int(input('Inputkan jumlah nilai : '))


'''__MAIN PROGRAM__'''
x = []
y = []
n = 0
inputdata()
print('====Hasil====')
hasil = cariHasil(x, y, n)
print('Skala angka = ', hasil)
print('Skala Guilford =', skalaguilford(hasil))
print('Jenis Koefisien Determinasi =', (hasil ** 2) * 100, '%')
print('Ditemukan', 100 - ((hasil ** 2) * 100), '% kontribusi dari faktor lain')

#Tugas Pemrograman Simulasi