program tugas_adp_satu;
  var
    phi:real;
    r:integer;
begin
  writeln('Nama  : Andri Adrian ');
  writeln('NO.BP : 2310432043 ');
  writeln('             =============================================');
  writeln('             | Menghitung Volume dan Luas Permukaan Bola |');
  writeln('             =============================================');
    phi:=22/7;
    write('Masukan jari-jari bola : ');
    readln(r);
    writeln('Luas Permukaan dari bola dengan jari-jari ',r,' adalah ',4*phi*r*r);
    writeln('Volume dari bola dengan jari-jari ',r,' adalah ',4/3*phi*r*r*r);
readln;
end.