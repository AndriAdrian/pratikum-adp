print(" Nama : Andri Adrian")
print(" NIM  : 2310432043")
print()
print(" Program Toko Kelontong Berkah Selalu")
print()

a = [ ["NAMA PRODUK ", "shampo", "mie instan", "pensil", "garam", "1L minyak", "1KG beras", "1KG tepung", "buku"],
		["HARGA (Rp) ", 1000, 3000, 4000, 1000, 28000, 18000, 11000, 3000],
		["STOK        ", 50, 20, 12, 9, 12, 15, 13, 24] ]
		
print("+-----------------------------------------+")

for i in range(9) :
    for j in range(3) :
        isi = str(a[j][i])
        print("| {:<12}".format(a[j][i]), end = "")
    print("|")
print("+_+")

print()

b = [ ]
for i in range (1,9) :
        total = a[1][i]*a[2][i]
        b.append(total)
        
max_num = b[0]
for i in range (8) :
     if(b[i] > max_num) :
          max_num = b[i] ;
          
min_num = b[0]
for i in range (8) :
     if(b[i] < min_num) :
          min_num = b[i] ;
          
for i in range (8) :
     if max_num == b[i] : 
          print("barang dengan keuntungan terbesar : {:<10} = Rp. {:<5}".format(a[0][i+1], max_num))
          
for i in range (8):
     if min_num == b[i] :
          print("barang dengan keuntungan terkecil : {:<10} = Rp. {:<5}".format(a[0][i+1], min_num))
          
tk = 0
for i in range (8) :
     tk += b[i]
print("total keuntungan barang keseluruhan = Rp. {}".format(tk))