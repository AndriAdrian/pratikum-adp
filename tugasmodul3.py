print("nama: andri adrian")
print("NIM : 2310432043")
print("sift: 4")
huruf=65
t = int(input("masukakan tinggi segitiga yang akan di buat menggunakan alphabet : "))
for i in range(t) :
    for a in range(t-i): 
      print(" ",end="")
    for k in range(i+1):
       print(chr(huruf+k),end="")
    for j in range(i,-1,-1):
      if (j==0): 
       print(chr(huruf+j)*0,end="")
      else:
       print(chr(huruf+j-1),end="")     
    print()  