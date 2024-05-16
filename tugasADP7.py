print(" Nama : Andri Adrian")
print(" NIM  : 2310432043")
print()
print(" Tugas 7 Modul 7 → Program GLBB")
print()

v0 = [ ]
a = [ ]
t = [ ]

def input_data(n) :
    for i in range(n) :
        d = float(input(" kecepatan rata rata (v0) : "))
        v0.append(d)
        b = float(input(" percepatan (a) : "))
        a.append(b)
        c = float(input(" waktu (t) : "))
        t.append(c)
    return v0, a, t
n = int(input(" Input jumlah GLBB yang akan di cari = "))
inputan = input_data(n)

def kecepatan_akhir(n) :
    vt = [ ]
    for i in range (n) :
        d = v0[ i ] + ((a[ i ])*(t[ i ]))
        vt.append(d)
    return vt
hasil_vt = kecepatan_akhir(n)

def jarak(n) :
    s = [ ]
    for i in range (n) :
        d = (v0[ i ]*t[ i ]) + (0.5*a[ i ]*((t[ i ])**2))
        s.append(d)
    return s
hasil_s = jarak(n)

print()
print(" +-----+-----------------+-------------+---------+-----------------+-------------+")
print(" | {:<3} | {:<15} | {:<11} | {:<7} | {:<15} | {:<11} |".format("n", "Kecepatan Awal", "Percepatan", "Waktu", "Kecepatan Akhir", "Jarak"))
print(" +-----+-----------------+-------------+---------+-----------------+-------------+")

for i in range(n) :
    print(" | {:<3} | {:<15} | {:<11} | {:<7} | {:<15} | {:<11} |".format(i+1, v0[ i ], a[ i ], t[ i ], hasil_vt[ i ], hasil_s[ i ]))
print(" +-----+-----------------+-------------+---------+-----------------+-------------+")

n = len(inputan)