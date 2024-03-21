print("Nama : Andri Adrian")
print("NIM  : 2310432043")
print()
print("                                      ! TRIPELOKA !")
print("                                       ----------- ")
print()
print("  Selamat Datang di TRIPELOKA Platform penyedia Tiket pesawat")
print("  Diskon 25% pengguna baru untuk pembelian jumlah tiket lebih dari 3")
print()
print("  Masukan Data Diri Anda ")
nama=str(input("  Nama : "))
umur=(input("  Umur : "))
jk=str(input("  Jenis Kelamin : "))
print()
print()
print("          Informasi Penerbangan")
print("          ---------------------")
print("  Penerbangan Dari : Padang")
print("  >>>>>>>>>>>>>>>>>>>>>>>>")
print("  #  Tujuan Penerbangan  #")
print("  <<<<<<<<<<<<<<<<<<<<<<<<")
print("  +----------------------")
print("  |  NO  |     KOTA     |")
print("  +---------------------+")
print("  |  1   |  Jakarta     |")
print("  |  2   |  Denpasar    |")
print("  |  3   |  Surabaya    |")
print("  +---------------------+")
tp=(input("  Pilih Kota Tujuan : "))
if(tp:=1):
    kt="jakarta"
    print("  Penerbangan Padang - Jakarta")
    print(" +-------------------+")
    print(" | Class Penerbangan |")
    print(" +-------------------+")
    print()
    print("  +------------------------------------+")
    print("  | NO |  Class       |     Harga      |")
    print("  +------------------------------------+")
    print("  | 1  | Ekonomi      |  Rp 800.000    |")
    print("  | 2  | Bisnis       |  Rp 1.000.000  |")
    print("  | 3  | First Class  |  Rp 1.200.000  |")
    print("  +------------------------------------+")
    print()
    cp=(input("  Pilih Class Penerbangan : "))
    if(cp:=1):
        jm="Ekonomi"
        harga=800000
    elif(cp:=2):
        jm="Bisnis"
        harga=1000000
    elif(cp:=3):
        jm="Firts Class"
        harga=1200000
elif(tp:=3):
    kt="Surabaya"
    print("  Penerbangan Padang - Surabaya")
    print(" +-------------------+")
    print(" | Class Penerbangan |")
    print(" +-------------------+")
    print()
    print("  +------------------------------------+")
    print("  | NO |  Class       |     Harga      |")
    print("  +------------------------------------+")
    print("  | 1  | Ekonomi      |  Rp 1.700.000  |")
    print("  | 2  | Bisnis       |  Rp 1.800.000  |")
    print("  | 3  | First Class  |  Rp 2.200.000  |")
    print("  +------------------------------------+")
    print()
    cp=(input("  Pilih Class Penerbangan : "))
    if(cp:=1):
        jm="Ekonomi"
        harga=1700000
    elif(cp:=2):
        jm="Bisnis"
        harga=1800000
    elif(cp:=3):
        jm="Firts Class"
        harga=2200000
elif(tp:=2):
    kt="Denpasar"
    print("  Penerbangan Padang - Denpasar")
    print(" +-------------------+")
    print(" | Class Penerbangan |")
    print(" +-------------------+")
    print()
    print("  +------------------------------------+")
    print("  | NO |  Class       |     Harga      |")
    print("  +------------------------------------+")
    print("  | 1  | Ekonomi      |  Rp 1.200.000  |")
    print("  | 2  | Bisnis       |  Rp 1.500.000  |")
    print("  | 3  | First Class  |  Rp 2.000.000  |")
    print("  +------------------------------------+")
    print()
    cp=(input("  Pilih Class Penerbangan : "))
    if(cp:=1):
        jm="Ekonomi"
        harga=800000
    elif(cp:=2):
        jm="Bisnis"
        harga=1000000
    elif(cp:=3):
        jm="Firts Class"
        harga=1000000               
print()
jt=int(input("  Jumlah Tiket Yang di Pesan : "))
if(jt>3):
    total=(jt*harga)-(jt*harga*0.25)
else:
    total=(jt*harga)
print()
print("     Struk Pemesanan")
print()
print("  NAMA          : "+nama)
print("  UMUR          : "+umur)
print("  Jenis Kelamin : "+jk)
print("  ----------------------------------")
print("  Kota Tujuan    : "+kt)
print("  Jenis Maskapai : "+jm)
print("  Jumlah Tiket   : ",jt)
print("  Total Harga    : Rp.",int(total))    