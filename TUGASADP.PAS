program tiket_pesawat;
uses crt;
var
 Nama,jk,kt,jm,jakarta,denpasar,surabaya,ekonomi,bisnis,FirstClass:string;
 Umur,jp,cp,tp,jt:integer;
 harga,total:real;

begin
clrscr;
writeln('nama : andri adrian');
writeln('nim  : 2301432043');
writeln ('                           $ TRIPELOKA $');
writeln ('                           -------------');
writeln;
writeln ('  Selamat datang di TRIPELOKA platfrom penyedia tiket pesawat');
writeln;
writeln ('  Masukan Data Diri Anda');
write   ('  Nama : ');
readln  (Nama);
write   ('  Umur : ');
readln  (Umur);
write   ('  jenis kelamin : ');
readln  (jk);
writeln;
writeln;
writeln ('      Informasi Penerbangan');
writeln ('      ---------------------');
writeln (' Penerbangan Dari : Padang');
writeln (' >>>>>>>>>>>>>>>>>>>>>>');
writeln (' ! Tujuan Penerbangan !');
writeln (' <<<<<<<<<<<<<<<<<<<<<<');
writeln (' +---------------------+');
writeln (' |  NO  |     KOTA     |');
writeln (' |---------------------|');
writeln (' |  1   |   Jakarta    |');
writeln (' |  2   |   Denpasar   |');
writeln (' |  3   |   Surabaya   |');
writeln (' +---------------------+');
write   (' Pilih kota tujuan penerbangan : ');
readln  (tp);
  if(tp=1)then
  begin
       kt:='Jakarta';
       writeln(' Penerbangan padang - jakarta');
       writeln('        +-----------------+');
       writeln('        |  Class Pesawat  |');
       writeln('        +-----------------+');
       writeln;
       writeln('+----------------------------------+');
       writeln('| NO |    class    |     harga     |');
       writeln('+----------------------------------+');
       writeln('| 1  | Ekonimi     | Rp.800000     |');
       writeln('| 2  | Bisnis      | Rp.1000000    |');
       writeln('| 3  | First Class | Rp.1200000    |');
       writeln('+----------------------------------+');
       writeln;
       writeln('pilih class penerbangan : ');
       readln(cp);
       if(cp=1)then
       begin
       jm:='Ekonomi';
       harga:=800000;
       end
       else
       if(cp=2)then
       begin
       jm:='Bisnis';
       harga:=1000000;
       end
       else
       if(cp=3)then
       begin
       jm:='FirstClass';
       harga:=1200000
       end
  end
  else
  if(tp=2)then
  begin
       kt:='Denpasar';
       writeln(' Penerbangan padang - denpasar');
       writeln('        +-----------------+');
       writeln('        |  Class Pesawat  |');
       writeln('        +-----------------+');
       writeln;
       writeln('+----------------------------------+');
       writeln('| NO |    class    |     harga     |');
       writeln('+----------------------------------+');
       writeln('| 1  | Ekonimi     | Rp.1200000    |');
       writeln('| 2  | Bisnis      | Rp.1500000    |');
       writeln('| 3  | First Class | Rp.2000000    |');
       writeln('+----------------------------------+');
       writeln;
       writeln('pilih class penerbangan : ');
       readln(cp);
       if(cp=1)then
       begin
       jm:='Ekonomi';
       harga:=1200000;
       end
       else
       if(cp=2)then
       begin
       jm:='Bisnis';
       harga:=1500000
       end
       else
       if(cp=3)then
       begin
       jm:='FirstClass';
       harga:=2000000
       end
  end
  else
  if(tp=3)then
  begin
       kt:='Surabaya';
       writeln(' Penerbangan padang - surabaya');
       writeln('        +-----------------+');
       writeln('        |  Class Pesawat  |');
       writeln('        +-----------------+');
       writeln;
       writeln('+----------------------------------+');
       writeln('| NO |    class    |     harga     |');
       writeln('+----------------------------------+');
       writeln('| 1  | Ekonimi     | Rp.1700000    |');
       writeln('| 2  | Bisnis      | Rp.1800000    |');
       writeln('| 3  | First Class | Rp.2200000    |');
       writeln('+----------------------------------+');
       writeln;
       writeln('pilih class penerbangan : ');
       readln(cp);
       if(cp=1)then
       begin
       jm:='Ekonomi';
       harga:=1700000;
       end
       else
       if(cp=2)then
       begin
       jm:='Bisnis';
       harga:=1800000
       end
       else
       if(cp=3)then
       begin
       jm:='FirstClass';
       harga:=2200000
       end;
  end;
write('Jumlah tiket yang di pesan : ');
readln(jt);
  if(jt>3)then
  total:=jt*harga*0.25
  else
  total:=jt*harga;
writeln;
writeln('  struk pemesanan');
writeln;
writeln('  NAMA           : ',nama);
writeln('  UMUR           : ',umur);
writeln('  Jenis Kelamin  : ',jk);
writeln('  --------------------');
writeln('  Kota Tujuan    : ',kt);
writeln('  Jenis Maskapai : ',jm);
writeln('  Jumlah Tiket   : ',jt);
writeln('  Total harga    : Rp.',total:0:0);

readkey;
end.