#TUGAS REGRESI HAEKAL 152018085#

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
    for x in range(n):
        arr.append((inp[x] ** 2))
        out += arr[x]
    return out, arr


def cariA(inpX, inpY, inpN):
    Yi = nilai1(inpY)[0]
    Xi2, nXi2 = nilaipow1(inpX)[:2]
    Xi = nilai1(inpX)[0]
    XiYi = nilai2(inpX, inpY)[0]
    out = []
    for x in range(n):
        out.append(round(((Yi * Xi2) - (Xi * XiYi)) / ((inpN * nXi2[x]) - (Xi ** 2)), 3))
    return out

def cariB(inpX, inpY, inpN):
    Yi = nilai1(inpY)[0]
    Xi = nilai1(inpX)[0]
    XiYi = nilai2(inpX, inpY)[0]
    out = []
    for x in range(n):
        out.append(round(((inpN * XiYi) - (Xi * Yi)) / ((inpN * Xi) - (Xi ** 2)), 3))
    return out

def inputdata():
    global n
    print('Inputkan nilai a (konstanta)')
    while True:
        entry = input('number : ')
        if entry == '':
            break
        try:
            x.append(int(entry))
        except:
            print("Nilai tidak valid!")
    print('Inputkan nilai b (koefisien)')
    while True:
        entry = input('number : ')
        if entry == '':
            break
        try:
            y.append(int(entry))
        except:
            print("Nilai tidak valid!")
    n = int(input('nilai n : '))



'''__MAIN PROGRAM__'''
x = []
y = []
n = 0
inputdata()
a = cariA(x,y,n)
b = cariB(x,y,n)
print('Nilai a (konstatnta) = ', a)
print('Nilai b (koefisien) = ', b)
print('===Bentuk Persamaan===')
for i in range(n):
    print('(', i+1 ,') Y = ', a[i], ' + (', b[i], ')x')

    #Tugas 1 Pemrograman Simulasi