program tugas_ADP_soal_no2;
 uses crt;
 var
  n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,jumlah,akar:integer;
  x,ragam,sb:real;
begin
writeln('Nama = Andri Adrian');
writeln('No.BP= 2301432043');
writeln('       ########################');
writeln('      # Nilai Matematika Siswa # ');
writeln('       ########################');
writeln(' -------+-----------');
writeln('! nilai | frekuensi !');
writeln(' -------+-----------');
write('   10   |     ');read(n1);
write('   20   |     ');read(n2);
write('   30   |     ');read(n3);
write('   40   |     ');read(n4);
write('   50   |     ');read(n5);
write('   60   |     ');read(n6);
write('   70   |     ');read(n7);
write('   80   |     ');read(n8);
write('   90   |     ');read(n9);
write('   100  |     ');read(n10);
  akar:=2;
  jumlah:=n1+n2+n3+n4+n5+n6+n7+n8+n9+n10;
  x:=((n1*10)+(n2*20)+(n3*30)+(n4*40)+(n5*50)+(n6*60)
     +(n7*70)+(n8*80)+(n9*90)+(n10*100))/jumlah;
  ragam:=((n1*(10-x)*(10-x))+(n2*(20-x)*(20-x))
         +(n3*(30-x)*(30-x))+(n4*(40-x)*(40-x))+(n5*(50-x)*(50-x))
         +(n6*(60-x)*(60-x))+(n7*(70-x)*(70-x))+(n8*(80-x)*(80-x))
         +(n9*(90-x)*(90-x))+(n10*(100-x)*(100-x)))/(jumlah-1);
  sb:=exp(ln(ragam)/akar);
writeln('rata-rata = ',x);
writeln('ragam = ',ragam);
writeln('simpangan baku = ',sb);
readkey
;
end.