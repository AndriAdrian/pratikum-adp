def program_adp_modul4(p, l):
    angka = 1
    jumlah= 0
    for i in range(l):
        for j in range(p):
            if angka%3==0 or angka%5==0:
                print("Door",end=" ")
                jumlah += 1
            else:
                print(angka, end=" ")
            angka += 1
        print()
    print("total door yang muncul sebanyak = ",jumlah)
p = 10
l = 10
program_adp_modul4(p,l)