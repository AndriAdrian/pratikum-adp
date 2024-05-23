print("nama: andri adrian")
print("nim: 2310432043")
print("sift: 4")


def load_data(filename):
    data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                tanggal, deskripsi, nominal, tipe_transaksi = line.strip().split(',')
                data.setdefault(tanggal, []).append({'deskripsi': deskripsi, 'nominal': float(nominal), 'type': tipe_transaksi})
    except FileNotFoundError:
        pass
    return data

def menyimpan_data(filename, data):
    with open(filename, 'w') as file:
        for tanggal, transactions in data.items():
            for transaction in transactions:
                file.write(f"{tanggal},{transaction['deskripsi']},{transaction['nominal']},{transaction['type']}\n")

def masukan_data(data):
    tanggal = input("Masukkan tanggal transaksi (YYYY-MM-DD): ")
    deskripsi = input("Masukkan keterangan transaksi: ")
    nominal = float(input("Masukkan jumlah uang: "))
    tipe_transaksi = input("Masukkan tipe transaksi (pemasukan/pengeluaran): ").lower()
    data.setdefault(tanggal, []).append({'deskripsi': deskripsi, 'nominal': nominal, 'type': tipe_transaksi})
    print("Transaksi berhasil ditambahkan!")

def hapus_data(data):
    tanggal = input("Masukkan tanggal transaksi yang ingin dihapus (YYYY-MM-DD): ")
    if tanggal in data:
        print("Transaksi pada tanggal tersebut:")
        for i, transaction in enumerate(data[tanggal]):
            print(f"{i+1}. {transaction['deskripsi']}: {transaction['nominal']} ({transaction['type']})")
        choice = int(input("Pilih nomor transaksi yang ingin dihapus: ")) - 1
        del data[tanggal][choice]
        if not data[tanggal]:
            del data[tanggal]
        print("Transaksi berhasil dihapus!")
    else:
        print("Tidak ada transaksi pada tanggal tersebut.")

def tampilkan_data(data):
    if not data:
        print("Tidak ada data keuangan yang tersimpan.")
    else:
        print("Data keuangan:")
        for tanggal, transactions in data.items():
            print(f"Tanggal: {tanggal}")
            for transaction in transactions:
                print(f"- {transaction['deskripsi']}: {transaction['nominal']} ({transaction['type']})")

filename = "keuangan.txt"
data = load_data(filename)

while True:
    print("\nMenu:")
    print("1. Tambah Transaksi")
    print("2. Hapus Transaksi")
    print("3. Tampilkan Data Keuangan")
    print("4. Keluar")
    a = input("Masukkan pilihan (1/2/3/4): ")

    if a == '1':
        masukan_data(data)
        menyimpan_data(filename, data)
    elif a == '2':
        hapus_data(data)
        menyimpan_data(filename, data)
    elif a == '3':
        tampilkan_data(data)
    elif a == '4':
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")