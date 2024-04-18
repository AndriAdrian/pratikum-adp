p1=int(input("banyak angka pada himpunan X = "))
p2=int(input("banyak angka pada himpunan Y = "))
himpunan1=[]
himpunan2=[]
for i in range (p1):
    while True:
        data=int(input(f"Masukan anggota {i+1} untuk himpunan X (selang 1-9) = "))
        if data in range (0,10):
            himpunan1.append(data)
            break
        else:
            print("angka yang anda masukan tidak berada pada selang")
            print("mohon masukan anggota untuk himpunan X lagi")
for i in range (p2):
    while True :
        data=int(input(f"Masukan anggota {i+1} untuk himpunan Y (selang 1-9) = "))
        if data in range (0,10):
            himpunan2.append(data)
            break
        else:
            print("angka yang anda masukan tidak berada pada selang")
            print("mohon masukan anggota untuk himpunan Y lagi")
himpunan1_aja=[ data for data in himpunan1 if data not in himpunan2]
himpunan2_aja=[ data for data in himpunan2 if data not in himpunan1]
himpunan1dan2=[ data for data in himpunan1 if data in himpunan2]
print(f"anggota himpunan X {himpunan1}")
print(f"anggota himpunan Y {himpunan2}")
print(f"angka yang hanya ada di himpunan X adalah {himpunan1_aja}")
print(f"angka yang hanya ada di himpunan Y adalah {himpunan2_aja}")
print(f"angka yang ada di himpunan X dan Y adalah {himpunan1dan2}")