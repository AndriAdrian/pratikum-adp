program uap;

uses
SysUtils,crt;

var
  DataGame  : Text;                                //Modul 8: File Text
  data      : record
    soal    : array [1..30] of string;            //Modul 5 : Array 1D
    jawaban : array [1..30,1..4] of string;      //Modul  6 : Array 2D
    kunci   : array [1..30] of char;
    uang    : array [0..15] of string;
    username: string;
  end;

  mulai, n, pilihan, x, j, acak, a         : integer;
  i             : char;

//Modul 7 : Procedure
procedure kuis;
begin
  data.uang[0] := 'Rp 0,00';
  data.uang[1] := 'Rp 50.000,00';
  data.uang[2] := 'Rp 125.000,00';
  data.uang[3] := 'Rp 250.000,00';
  data.uang[4] := 'Rp 500.000,00';
  data.uang[5] := 'Rp 1.000.000,00';
  data.uang[6] := 'Rp 2.000.000,00';
  data.uang[7] := 'Rp 4.000.000,00';
  data.uang[8] := 'Rp 8.000.000,00';
  data.uang[9] := 'Rp 16.000.000,00';
  data.uang[10] := 'Rp 32.000.000,00';
  data.uang[11] := 'Rp 64.000.000,00';
  data.uang[12] := 'Rp 125.000.000,00';
  data.uang[13] := 'Rp 250.000.000,00';
  data.uang[14] := 'Rp 500.000.000,00';
  data.uang[15] := 'Rp 1.000.000.000,00';

  data.kunci[1] := 'A';
  data.kunci[2] := 'D';
  data.kunci[3] := 'C';
  data.kunci[4] := 'B';
  data.kunci[5] := 'B';
  data.kunci[6] := 'C';
  data.kunci[7] := 'A';
  data.kunci[8] := 'B';
  data.kunci[9] := 'D';
  data.kunci[10]:= 'A';
  data.kunci[11]:= 'B';
  data.kunci[12]:= 'B';
  data.kunci[13]:= 'C';
  data.kunci[14]:= 'A';
  data.kunci[15]:= 'A';
  data.kunci[16]:= 'C';
  data.kunci[17]:= 'B';
  data.kunci[18]:= 'A';
  data.kunci[19]:= 'D';
  data.kunci[20]:= 'B';
  data.kunci[21]:= 'C';
  data.kunci[22]:= 'B';
  data.kunci[23]:= 'A';
  data.kunci[24]:= 'B';
  data.kunci[25]:= 'D';
  data.kunci[26]:= 'A';
  data.kunci[27]:= 'D';
  data.kunci[28]:= 'A';
  data.kunci[29]:= 'C';
  data.kunci[30]:= 'D';

  data.soal[1] := 'Satu Ton ada berapa kilo?';
  data.jawaban[1,1] := 'A. 1000'; //benar
  data.jawaban[1,2] := 'B. 100';
  data.jawaban[1,3] := 'C. 10';
  data.jawaban[1,4] := 'D. 1';

  data.soal[2]:= 'Senjata khas suku aborigin adalah';
  data.jawaban[2,1]:= 'A. Keris';
  data.jawaban[2,2]:= 'B. Palu';
  data.jawaban[2,3]:= 'C. Parang';
  data.jawaban[2,4]:= 'D. Boomerang'; //benar

  data.soal[3]:= 'Yang bukan termasuk pahlawan revolusi adalah';
  data.jawaban[3,1]:= 'A. Ahmad Yani';
  data.jawaban[3,2]:= 'B. Suprapto';
  data.jawaban[3,3]:= 'C. A.H.Nasution'; //benar
  data.jawaban[3,4]:= 'D. S.Parman';

  data.soal[4]:= 'Buku "Negara Kertagama" dikarang oleh';
  data.jawaban[4,1]:= 'A. Mpu Tantular';
  data.jawaban[4,2]:= 'B. Mpu Prapanca';//benar
  data.jawaban[4,3]:= 'C. Mpu Gandring';
  data.jawaban[4,4]:= 'D. Mpu Aji Guna Anom';

  data.soal[5]:= 'Angin yang berhembus dari darat ke laut disebut';
  data.jawaban[5,1]:= 'A. Angin Laut';
  data.jawaban[5,2]:= 'B. Angin Darat';//benar
  data.jawaban[5,3]:= 'C. Angin Lembah';
  data.jawaban[5,4]:= 'D. Angin Gunung';

  data.soal[6]:= 'Lagu "Buka Pintu" berasal dari';
  data.jawaban[6,1]:= 'A. Aceh';
  data.jawaban[6,2]:= 'B. Gorontalo';
  data.jawaban[6,3]:= 'C. Maluku';  //benar
  data.jawaban[6,4]:= 'D. Pontianak';

  data.soal[7]:= 'Pembuluh darah yang mengalirkan darah ke jantung adalah';
  data.jawaban[7,1]:= 'A. Nadi'; //benar
  data.jawaban[7,2]:= 'B. Arteri';
  data.jawaban[7,3]:= 'C. Vena';
  data.jawaban[7,4]:= 'D. Kapiler';

  data.soal[8]:= 'Angin yang berganti arah setiap enam bulan sekali disebut';
  data.jawaban[8,1]:= 'A. Angin Fohn';
  data.jawaban[8,2]:= 'B. Angin Muson';//benar
  data.jawaban[8,3]:= 'C. Angin Laut';
  data.jawaban[8,4]:= 'D. Angin Gunung';

  data.soal[9]:= 'Kandungan utama dalam pupuk ZA adalah';
  data.jawaban[9,1]:= 'A. Magnesium';
  data.jawaban[9,2]:= 'B. Fosfor';
  data.jawaban[9,3]:= 'C. Kalium';
  data.jawaban[9,4]:= 'D. Amonium Sulfat'; //benar

  data.soal[10]:='Alat pencatat gempa adalah';
  data.jawaban[10,1]:= 'A. Seismograf'; //benar
  data.jawaban[10,2]:= 'B. Termometer';
  data.jawaban[10,3]:= 'C. Tensimeter';
  data.jawaban[10,4]:= 'D. Higrometer';

  data.soal[11]:='Lagu "Bagimu Negeri" diciptakan oleh';
  data.jawaban[11,1]:= 'A. W.R. Supratman';
  data.jawaban[11,2]:= 'B. Kusbini';//benar
  data.jawaban[11,3]:= 'C. Ismail Marzuki';
  data.jawaban[11,4]:= 'D. Ibu Soed';

  data.soal[12]:='Senyawa utama yang ada dalam Spirtus adalah';
  data.jawaban[12,1]:= 'A. Air';
  data.jawaban[12,2]:= 'B. Alkohol'; //benar
  data.jawaban[12,3]:= 'C. Kalium';
  data.jawaban[12,4]:= 'D. Urea';

  data.soal[13]:='Alat optic yang digunakan pada kapal selam adalah';
  data.jawaban[13,1]:= 'A. Loop';
  data.jawaban[13,2]:= 'B. Teropong';
  data.jawaban[13,3]:= 'C. Periskop'; //benar
  data.jawaban[13,4]:= 'D. Mikroskop';

  data.soal[14]:=' Ilmu yang mempelajari segala aspek kehidupan Mikroorganisme disebut';
  data.jawaban[14,1]:= 'A. Mikrobiologi'; //benar
  data.jawaban[14,2]:= 'B. Ekologi';
  data.jawaban[14,3]:= 'C. Fisiologi';
  data.jawaban[14,4]:= 'D. Sosiologi';

  data.soal[15] := 'Lagu "Mariam Tomong" berasal dari daerah';
  data.jawaban[15,1] := 'A. Tapanuli'; //benar
  data.jawaban[15,2] := 'B. Sibolga';
  data.jawaban[15,3] := 'C. Banda Aceh';
  data.jawaban[15,4] := 'D. Palu';

  data.soal[16] := 'Petinju yang dijuluki istilah "Si Leher Beton" adalah';
  data.jawaban[16,1] := 'A. Muhammad Ali';
  data.jawaban[16,2] := 'B. Chris John';
  data.jawaban[16,3] := 'C. Mike Tyson'; //benar
  data.jawaban[16,4] := 'D. Evander Holyfield';

  data.soal[17] := 'Dalam tubuh manusia reproduksi aseksual Plasmodium Malaria berlangsung di';
  data.jawaban[17,1] := 'A. Saluran Darah';
  data.jawaban[17,2] := 'B. Eritrosit'; //benar
  data.jawaban[17,3] := 'C. Otak';
  data.jawaban[17,4] := 'D. Paru-paru';

  data.soal[18] := 'Bahan utama untuk membuat Popcorn adalah';
  data.jawaban[18,1] := 'A. Jagung'; //benar
  data.jawaban[18,2] := 'B. Kentang ';
  data.jawaban[18,3] := 'C. Beras';
  data.jawaban[18,4] := 'D. Gandum';

  data.soal[19] := 'Pembuatan kalender masehi berdasar atas perputaran';
  data.jawaban[19,1] := 'A. Bumi pada bulan';
  data.jawaban[19,2] := 'B. Matahari pada bumi';
  data.jawaban[19,3] := 'C. Bulan pada bumi';
  data.jawaban[19,4] := 'D. Bumi pada matahari'; //benar

  data.soal[20] := 'Lagu berikut berasal dari daerah Sumatera Barat, yakni';
  data.jawaban[20,1] := 'A. Soleram';
  data.jawaban[20,2] := 'B. Ayam Den Lapeh';  //benar
  data.jawaban[20,3] := 'C. Ampar-ampar Pisang';
  data.jawaban[20,4] := 'D. Apuse';

  data.soal[21] := 'Mata uang negara Peru adalah';
  data.jawaban[21,1] := 'A. Yen';
  data.jawaban[21,2] := 'B. Dollar';
  data.jawaban[21,3] := 'C. Peso'; //benar
  data.jawaban[21,4] := 'D. Baht';

  data.soal[22] := 'Cabang geografi yang mempelajari bentuk-bentuk muka bumi disebut';
  data.jawaban[22,1] := 'A. Klimatologi';
  data.jawaban[22,2] := 'B. Geomorfologi';  //benar
  data.jawaban[22,3] := 'C. Biogeografi';
  data.jawaban[22,4] := 'D. Arkeologi';

  data.soal[23] := 'Ilmuwan yang pertama melihat adanya sel-sel dengan menggunakan mikroskop adalah';
  data.jawaban[23,1] := 'A. Robert Hooke'; //benar
  data.jawaban[23,2] := 'B. Marie Curie';
  data.jawaban[23,3] := 'C. Isaac Newton';
  data.jawaban[23,4] := 'D. Robert Downey Junior';

  data.soal[24] := 'Ilmu yang mempelajari cara/teknik pembuatan peta disebut';
  data.jawaban[24,1] := 'A. Arkeologi';
  data.jawaban[24,2] := 'B. Kartografi'; //benar
  data.jawaban[24,3] := 'C. Morfologi';
  data.jawaban[24,4] := 'D. Geografi';

  data.soal[25] := 'Naiknya tekanan darah akibat menyempitnya pembuluh nadi dapat dipengaruhi oleh hormon';
  data.jawaban[25,1] := 'A. Melatonin';
  data.jawaban[25,2] := 'B. Estrogen';
  data.jawaban[25,3] := 'C. Insulin';
  data.jawaban[25,4] := 'D. Adrenalin'; //benar

  data.soal[26] := 'Rumus molekul etana adalah';
  data.jawaban[26,1] := 'A. C2H6'; //benar
  data.jawaban[26,2] := 'B. H20';
  data.jawaban[26,3] := 'C. CH3COOH';
  data.jawaban[26,4] := 'D. COOH';

  data.soal[27] := 'Zat makanan yang pada metabolisme menghasilkan energi tinggi untuk satuan berat yang sama adalah';
  data.jawaban[27,1] := 'A. Protein';
  data.jawaban[27,2] := 'B. Vitamin';
  data.jawaban[27,3] := 'C. Gizi';
  data.jawaban[27,4] := 'D. Lemak';  //benar

  data.soal[28] := 'Istilah yang digunakan untuk menyebut orang buta adalah';
  data.jawaban[28,1] := 'A. Tuna Netra'; //benar
  data.jawaban[28,2] := 'B. Tuna Wisma';
  data.jawaban[28,3] := 'C. Tuna Rungu';
  data.jawaban[28,4] := 'D. Tuna Wicara';

  data.soal[29] := 'Universitas negeri yang ada di Padang adalah universitas';
  data.jawaban[29,1] := 'A. Bung Hatta';
  data.jawaban[29,2] := 'B. Putra Indonesia';
  data.jawaban[29,3] := 'C. Andalas';    //benar
  data.jawaban[29,4] := 'D. Gadjah Mada';

  data.soal[30] := 'Pengarang Novel Harry Potter adalah';
  data.jawaban[30,1] := 'A. J.R.R. Tolkien';
  data.jawaban[30,2] := 'B. William Shakespeare';
  data.jawaban[30,3] := 'C. Tere Liye';
  data.jawaban[30,4] := 'D. J.K.Rowling';    //benar

  Randomize;




  for n:= 1 to 15 do
  begin
    clrscr;
    repeat
      acak:= random(30)+n;
    until (acak < 31);
    for j:= 1 to 4 do    //Modul 4 : Perulangan Bersarang
     begin
       gotoxy(20,9); write('-----------------------------------------------------------------------------------');
       gotoxy(20,12); write('-----------------------------------------------------------------------------------');
       gotoxy(22,10); writeln(n,'.',data.soal[acak]);
       gotoxy(55,j+13); writeln(data.jawaban[acak,j]);
     end;

    repeat
      begin
        i := UpCase(i);
        gotoxy(40,20);
        readln(i);
      end;
    until (i = 'A') or (i = 'B') or (i = 'C') or (i = 'D');

    if (i = data.kunci[acak]) then   //Modul 2 : Pengkondisian
      begin
            clrscr;
            gotoxy (45,14); writeln('-----------------------------------');
            gotoxy(45,15); write ('|'); gotoxy(80,15); write('|');
            gotoxy(45,16); write ('|'); gotoxy(80,16); write('|');
            gotoxy(60,15); writeln('BENAR');
            gotoxy(50,16); writeln('UANG ANDA :',data.uang[n]);
            gotoxy (45,17); writeln('-----------------------------------');
            readln;
             if (n = 5) or (n=10) then    //Modul 4 : Pengkondisian Bersarang
              begin
                gotoxy (45,10); writeln('-----------------------------------');
                gotoxy (44,11); write('|'); gotoxy (81,11); write('|');
                gotoxy (50,11);
                write('ANDA SUDAH SAMPAI ANGKA AMAN');
                gotoxy (45,12); writeln('-----------------------------------');
                readln;
              end;
            if (n=15) then
              begin
                clrscr;
                gotoxy(40,9); writeln('---------------------------------------------------');
                gotoxy(40,10); writeln('|'); gotoxy(90,10); writeln('|');
                gotoxy(50,10); writeln('SELAMAT ANDA JADI MILIARDER');
                gotoxy(40,11);  writeln('---------------------------------------------------');
                readln;
                clrscr;
                gotoxy (20,13); write('-----------------------------------------------------------------------------------');
                gotoxy(20,14); write ('|'); gotoxy(103,14); write('|');
                gotoxy(20,15); write ('|'); gotoxy(103,15); write('|');
                gotoxy (40,14); writeln('SELAMAT ANDA MEMBAWA UANG SENILAI :', data.uang[n]);
                gotoxy (20,16); write('-----------------------------------------------------------------------------------');
                readln;

                clrscr;
                gotoxy(50,12); writeln ('Nama  :');
                gotoxy(60,12); readln(data.username);

                assign(DataGame, 'game.txt');    //Modul 8 : File Text
                append (DataGame);
                writeln(DataGame, data.username);
                writeln(DataGame, data.uang[n]);
                close (DataGame);

                gotoxy(55,15); writeln('Data Otomatis Tersimpan!');
                readln;

                clrscr;
                gotoxy (55,15); writeln('MENU ? ');
                gotoxy (45,17); writeln('1. Ya');
                gotoxy (70,17); writeln('2. Tidak');
              repeat
                begin
                  gotoxy (76,18); readln (pilihan);
                end;
              until (pilihan = 1) or (pilihan = 2);
              end;
          end
   else
          begin
            clrscr;
            gotoxy(43,13); write('-----------------------------------------');
            gotoxy(43,14); write('|'); gotoxy(83,14); write('|');
            gotoxy(43,14); write('|'); gotoxy(83,14); write('|');
            gotoxy(43,15); write('|'); gotoxy(83,15); write('|');
            gotoxy(43,16); write('|'); gotoxy(83,16); write('|');
            gotoxy(60,14); writeln('SALAH');
            gotoxy(50,15); writeln('UANG ANDA :',data.uang[n-1]);
            gotoxy(45,16); writeln('ANDA TIDAK BISA MELANJUTKAN PERMAINAN');
            gotoxy(43,17); write('-----------------------------------------');
            Readln;

            clrscr;
                gotoxy (20,13); write('-----------------------------------------------------------------------------------');
                gotoxy(20,14); write ('|'); gotoxy(103,14); write('|');
                gotoxy(20,15); write ('|'); gotoxy(103,15); write('|');
                gotoxy (40,14); writeln('SELAMAT ANDA MEMBAWA UANG SENILAI :', data.uang[n-1]);
                gotoxy (20,16); write('-----------------------------------------------------------------------------------');
                readln;
                   clrscr;
                gotoxy (50,12); writeln ('Nama  :');
                gotoxy (60,12); readln(data.username);

                assign(DataGame, 'game.txt');
                append (DataGame);
                writeln(DataGame, data.username);
                writeln(DataGame, data.uang[n-1]);
                close (DataGame);

                gotoxy(50,15); writeln('Data Otomatis Tersimpan!');
                readln;
            clrscr;
            gotoxy(50,15); writeln('Kembali Ke Menu :');
            Exit;
            readln;
          end;
    end;
  end;



Function menu :integer;
 begin

  gotoxy(34,8); write('  -------------------------------------------------------');
  gotoxy(35,9);
  writeln('<< SELAMAT DATANG DI KUIS WHO WANT TO BE A MILLIONAIRE >>');
  gotoxy(34,10);write('  -------------------------------------------------------');
  writeln;
  gotoxy (50,13); writeln('----------------');
  gotoxy(55,12); writeln('MENU :');
  writeln();
  gotoxy (50,15); writeln('----------------');
  gotoxy (50,16); writeln('|'); gotoxy (66,16); writeln('|');
  gotoxy (50,17); writeln('|'); gotoxy (66,17); writeln('|');
  gotoxy (50,18); writeln('|'); gotoxy (66,18); writeln('|');
  gotoxy (50,19); writeln('|'); gotoxy (66,19); writeln('|');
  gotoxy (50,20); writeln('----------------');
  gotoxy (53,16); writeln('1. Mulai ');
  gotoxy (53,17); writeln('2. HighScore');
  gotoxy (53,18); writeln('3. Reset');
  gotoxy (53,19); writeln('4. Keluar');
  repeat      //Modul 3 : Perulangan
    begin
      gotoxy(62,14); clreol; readln(mulai);
    end;
  until (mulai =1) or (mulai = 2) or (mulai = 3) or (mulai = 4);
  menu := mulai;
  end;

//Modul 7 : Procedure dan Function
Procedure Highscore;
  begin
    clrscr;
    assign(DataGame, 'game.txt');
    reset(DataGame);

    gotoxy(55,2); writeln('HIGH SCORE');
    gotoxy(53,3); writeln('--------------');

    a:=1;
    while not eof(DataGame) do
      begin
        readln(DataGame, data.username);
        readln(DataGame, Data.uang[n]);
        gotoxy(8,5);
        writeln('No');
        gotoxy(8,6+a);
        writeln(a);
        gotoxy(20,5);
        writeln('NAMA');
        gotoxy(83,5);
        writeln('Uang');
        gotoxy(20,6+a);
        writeln(data.username);
        gotoxy(80,6+a);
        writeln(Data.uang[n]);
        writeln;
        a:=a+1;
      end;
      Close(DataGame);
      readln;
  end;


Procedure keluar;
begin
  clrscr;
    gotoxy(50,10); writeln ('Anda Yakin Ingin Keluar ?');
    gotoxy(40,12); writeln ('1. Ya');
    gotoxy(75,12); writeln ('2. Tidak');
    repeat
      begin
        gotoxy(75,10); readln (pilihan);
      end;
    until (pilihan = 1) or (pilihan = 2);
    if (pilihan = 1) then
      begin
        clrscr;
        gotoxy(50,10); writeln('ANDA BERHASIL KELUAR!');
        Readln;
        exit;
      end
    else
      begin
        clrscr;
        menu;
      end;
end;

Procedure Reset;
  begin
    Assign(DataGame, 'game.txt');
    rewrite(DataGame);
    clrscr;
    close(DataGame);
    gotoxy(50,15); writeln('HighScore telah direset');
    readln;
  end;

//Program Utama
begin
  clrscr;
  while mulai < 4 do
    begin
      clrscr;
      menu;

      case (mulai) of
        1: kuis;
        2: Highscore;
        3: Reset;
        4: Keluar;
      end;

  end;

readln;
end.


