import random
import os
import threading
import time

class Game:
    def __init__(self):
        self.data = {
            'soal': [None] * 30,
            'jawaban': [[None] * 4 for _ in range(30)],
            'kunci': [None] * 30,
            'uang': [None] * 16,
            'username': ""
        }
        self.mulai = 0
        self.timer_expired = False
        self.answer = None
        self.time_left = 0

    def kuis(self):
        self.data['uang'] = [
            'Rp 0,00', 'Rp 50.000,00', 'Rp 125.000,00', 'Rp 250.000,00',
            'Rp 500.000,00', 'Rp 1.000.000,00', 'Rp 2.000.000,00',
            'Rp 4.000.000,00', 'Rp 8.000.000,00', 'Rp 16.000.000,00',
            'Rp 32.000.000,00', 'Rp 64.000.000,00', 'Rp 125.000.000,00',
            'Rp 250.000.000,00', 'Rp 500.000.000,00', 'Rp 1.000.000.000,00'
        ]

        self.data['kunci'] = [
            'A', 'D', 'C', 'C', 'B', 'D', 'C', 'A', 'B', 'C', 'D', 'B',
            'C', 'B', 'B', 'C', 'D', 'A', 'C', 'C', 'B', 'C', 'D', 'A',
            'C', 'B', 'B', 'A', 'B', 'C',
        ]

        self.data['soal'][0] = 'Satu Ton ada berapa kilo?'
        self.data['jawaban'][0] = ['A. 1000', 'B. 100', 'C. 10', 'D. 1']
        self.data['soal'][1] = 'Senjata khas suku aborigin adalah'
        self.data['jawaban'][1] = ['A. Keris', 'B. Palu', 'C. Parang', 'D. Boomerang']
        self.data['soal'][2] = 'Yang bukan termasuk pahlawan revolusi adalah'
        self.data['jawaban'][2] = ['A. Ahmad Yani', 'B. Suprapto', 'C. A.H.Nasution', 'D. S.Parman']
        self.data['soal'][3] = 'Apa ibu kota dari negara Jepang?'
        self.data['jawaban'][3] = ['A. bejing', 'B. seoul', 'C. tokyo', 'D. bangkok']
        self.data['soal'][4] = 'Siapa penulis novel "Harry Potter"?'
        self.data['jawaban'][4] = ['A. J.R.R. Tolkien', 'B. J.K. Rowling', 'C. George R.R. Martin', 'D. Suzanne Collins']
        self.data['soal'][5] = 'Di mana lokasi Menara Eiffel?'
        self.data['jawaban'][5] = ['A. London', 'B. Berlin', 'C. Madrid', 'D. Paris']
        self.data['soal'][6] = 'Unsur kimia apa yang memiliki simbol Au ?'
        self.data['jawaban'][6] = ['A. Perak', 'B. Tembaga', 'C. Emas', 'D. Aluminium']
        self.data['soal'][7] = 'Planet mana yang dikenal sebagai planet merah?'
        self.data['jawaban'][7] = ['A. Mars', 'B. Venus', 'C. Jupiter', 'D. Saturnus']
        self.data['soal'][8] = 'Berapa jumlah planet dalam Tata Surya?'
        self.data['jawaban'][8] = ['A. 7', 'B. 8', 'C. 9', 'D. 10']
        self.data['soal'][9] = 'Siapa presiden pertama Amerika Serikat?'
        self.data['jawaban'][9] = ['A. Abraham Lincoln', 'B. Thomas Jefferson', 'C. George Washington', 'D. John Adams']
        self.data['soal'][10] = 'Revolusi Industri dimulai di negara mana?'
        self.data['jawaban'][10] = ['A. Amerika Serikat', 'B. Prancis', 'C. Jerman', 'D. Inggris']
        self.data['soal'][11] = 'Pada tahun berapa Indonesia merdeka?'
        self.data['jawaban'][11] = ['A. 1942', 'B. 1945', 'C. 1950', 'D. 1955']
        self.data['soal'][12] = 'Film apa yang memenangkan penghargaan Film Terbaik di Oscar tahun 2020?'
        self.data['jawaban'][12] = ['A. Joker', 'B. 1917', 'C. Parasite', 'D. Once Upon a Time in Hollywood']
        self.data['soal'][13] = 'Siapa yang menyanyikan lagu Shape of You?'
        self.data['jawaban'][13] = ['A. Justin Bieber', 'B. Ed Sheeran', 'C. Shawn Mendes', 'D. Bruno Mars']
        self.data['soal'][14] = 'Serial TV apa yang menceritakan tentang kerajaan fiksi Westeros?'
        self.data['jawaban'][14] = ['A. The Witcher', 'B. Game of Thrones', 'C. Vikings', 'D. The Mandalorian']
        self.data['soal'][15] = 'Berapa kali Brazil memenangkan Piala Dunia FIFA?'
        self.data['jawaban'][15] = ['A. 3 kali', 'B. 4 kali', 'C. 5 kali', 'D. 6 kali']
        self.data['soal'][16] = 'Siapa petenis wanita yang memenangkan Grand Slam terbanyak?'
        self.data['jawaban'][16] = ['A. Martina Navratilova', 'B. Serena Williams', 'C. Steffi Graf', 'D. Margaret Court']
        self.data['soal'][17] = 'Di cabang olahraga apa Michael Phelps terkenal?'
        self.data['jawaban'][17] = ['A. Renang', 'B. Atletik', 'C. Senam', 'D. Sepak bola']
        self.data['soal'][18] = 'Negara mana yang memiliki bendera dengan bintang tunggal?'
        self.data['jawaban'][18] = ['A. Turki', 'B. Amerika Serikat', 'C. Vietnam', 'D. Malaysia']
        self.data['soal'][19] = 'Apa nama ibu kota dari negara Kanada?'
        self.data['jawaban'][19] = ['A. Toronto', 'B. Vancouver', 'C. Ottawa', 'D. Montreal']
        self.data['soal'][20] = 'Siapa yang menemukan lampu pijar?'
        self.data['jawaban'][20] = ['A. Nikola Tesla', 'B. Thomas Edison', 'C. Alexander Graham Bell', 'D. James Watt']
        self.data['soal'][21] = 'Benda langit mana yang merupakan pusat Tata Surya?'
        self.data['jawaban'][21] = ['A. Bumi', 'B. Bulan', 'C. Matahari', 'D. Mars']
        self.data['soal'][22] = 'Apa satuan untuk mengukur intensitas arus listrik?'
        self.data['jawaban'][22] = ['A. Volt', 'B. Ohm', 'C. Watt', 'D. Ampere']
        self.data['soal'][23] = 'Unsur kimia mana yang memiliki simbol O?'
        self.data['jawaban'][23] = ['A. Oksigen', 'B. Hidrogen', 'C. Nitrogen', 'D. Karbon']
        self.data['soal'][24] = 'Perang Dunia II berakhir pada tahun berapa?'
        self.data['jawaban'][24] = ['A. 1943', 'B. 1944', 'C. 1945', 'D. 1946']
        self.data['soal'][25] = 'Di mana tembok Berlin berada?'
        self.data['jawaban'][25] = ['A. Prancis', 'B. Jerman', 'C. Rusia', 'D. Polandia']
        self.data['soal'][26] = 'Siapa raja Mesir yang terkenal dengan makamnya yang berisi banyak harta karun?'
        self.data['jawaban'][26] = ['A. Ramses II', 'B. Tutankhamun', 'C. Cleopatra', 'D. Akhenaten']
        self.data['soal'][27] = 'Grup musik mana yang dikenal dengan album "Abbey Road"?'
        self.data['jawaban'][27] = ['A. The Beatles', 'B. The Rolling Stones', 'C. Led Zeppelin', 'D. Pink Floyd']
        self.data['soal'][28] = 'Siapa yang menyutradarai film "Titanic"?'
        self.data['jawaban'][28] = ['A. Steven Spielberg', 'B. James Cameron', 'C. Martin Scorsese', 'D. Quentin Tarantino']
        self.data['soal'][29] = 'Film mana yang pertama kali menampilkan karakter James Bond?'
        self.data['jawaban'][29] = ['A. Goldfinger', 'B. From Russia with Love', 'C. Dr. No', 'D. Thunderball']

        random.seed()

        for n in range(15):
            os.system('cls' if os.name == 'nt' else 'clear')

            acak = random.randint(0, 29)

            print('-----------------------------------------------------------------------------------')
            print(f"{n + 1}. {self.data['soal'][acak]}")
            for j in range(4):
                print(self.data['jawaban'][acak][j])
            print('-----------------------------------------------------------------------------------')

            # Set timer for 30 seconds
            self.timer_expired = False
            self.answer = None
            self.time_left = 30
            timer_thread = threading.Thread(target=self.start_timer)
            timer_thread.start()

            while not self.timer_expired and self.answer is None:
                print(f"Waktu tersisa: {self.time_left} detik")
                self.answer = input("Pilihan Anda (A/B/C/D): ").upper()
                if self.answer not in ['A', 'B', 'C', 'D']:
                    self.answer = None

            timer_thread.join()

            if self.timer_expired:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('-----------------------------------------')
                print('|              WAKTU HABIS              |')
                print('-----------------------------------------')
                print(f"UANG ANDA: {self.data['uang'][n]}")
                print('ANDA TIDAK BISA MELANJUTKAN PERMAINAN')
                print('-----------------------------------------')
                input("Tekan Enter untuk melanjutkan...")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"SELAMAT ANDA MEMBAWA UANG SENILAI: {self.data['uang'][n]}")
                input("Tekan Enter untuk melanjutkan...")
                os.system('cls' if os.name == 'nt' else 'clear')
                self.data['username'] = input("Nama: ")
                with open('game.txt', 'a') as DataGame:
                    DataGame.write(f"{self.data['username']}\n")
                    DataGame.write(f"{self.data['uang'][n]}\n")
                print('Data Otomatis Tersimpan!')
                input("Tekan Enter untuk melanjutkan...")
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Kembali Ke Menu :')
                input("Tekan Enter untuk melanjutkan...")
                self.menu()
                break

            if self.answer == self.data['kunci'][acak]:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('-----------------------------------')
                print('|              BENAR              |')
                print('-----------------------------------')
                print(f"UANG ANDA: {self.data['uang'][n + 1]}")
                print('-----------------------------------')
                input("Tekan Enter untuk melanjutkan...")

                if n + 1 in [5, 10]:
                    print('-----------------------------------')
                    print('|    ANDA SUDAH SAMPAI ANGKA AMAN   |')
                    print('-----------------------------------')
                    input("Tekan Enter untuk melanjutkan...")

                if n + 1 == 15:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('---------------------------------------------------')
                    print('|            SELAMAT ANDA JADI MILIARDER            |')
                    print('---------------------------------------------------')
                    input("Tekan Enter untuk melanjutkan...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"SELAMAT ANDA MEMBAWA UANG SENILAI: {self.data['uang'][n + 1]}")
                    input("Tekan Enter untuk melanjutkan...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.data['username'] = input("Nama: ")
                    with open('game.txt', 'a') as DataGame:
                        DataGame.write(f"{self.data['username']}\n")
                        DataGame.write(f"{self.data['uang'][n + 1]}\n")
                    print('Data Otomatis Tersimpan!')
                    input("Tekan Enter untuk melanjutkan...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('MENU?')
                    print('1. Ya')
                    print('2. Tidak')
                    while True:
                        try:
                            pilihan = int(input())
                            if pilihan in [1, 2]:
                                break
                        except ValueError:
                            print("Input tidak valid, coba lagi.")
                    if pilihan == 1:
                        self.menu()
                    else:
                        exit()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('-----------------------------------------')
                print('|                SALAH                 |')
                print('-----------------------------------------')
                print(f"UANG ANDA: {self.data['uang'][n]}")
                print('ANDA TIDAK BISA MELANJUTKAN PERMAINAN')
                print('-----------------------------------------')
                input("Tekan Enter untuk melanjutkan...")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"SELAMAT ANDA MEMBAWA UANG SENILAI: {self.data['uang'][n]}")
                input("Tekan Enter untuk melanjutkan...")
                os.system('cls' if os.name == 'nt' else 'clear')
                self.data['username'] = input("Nama: ")
                with open('game.txt', 'a') as DataGame:
                    DataGame.write(f"{self.data['username']}\n")
                    DataGame.write(f"{self.data['uang'][n]}\n")
                print('Data Otomatis Tersimpan!')
                input("Tekan Enter untuk melanjutkan...")
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Kembali Ke Menu :')
                input("Tekan Enter untuk melanjutkan...")
                self.menu()
                break

    def start_timer(self):
        while self.time_left > 0 and self.answer is None:
            time.sleep(1)
            self.time_left -= 1
        self.timer_expired = self.time_left == 0

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('  -------------------------------------------------------')
            print('<< SELAMAT DATANG DI KUIS WHO WANT TO BE A MILLIONAIRE >>')
            print('  -------------------------------------------------------')
            print('MENU :')
            print('----------------')
            print('| 1. Mulai      |')
            print('| 2. HighScore  |')
            print('| 3. Reset      |')
            print('| 4. Keluar     |')
            print('----------------')
            try:
                self.mulai = int(input("Pilih menu: "))
                if self.mulai in [1, 2, 3, 4]:
                    if self.mulai == 1:
                        self.kuis()
                    elif self.mulai == 2:
                        self.highscore()
                    elif self.mulai == 3:
                        self.reset()
                    elif self.mulai == 4:
                        exit()
            except ValueError:
                print("Input tidak valid, coba lagi.")

    def highscore(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('HIGH SCORE')
        print('--------------')
        try:
            with open('game.txt', 'r') as DataGame:
                lines = DataGame.readlines()
                a = 1
                for i in range(0, len(lines), 2):
                    username = lines[i].strip()
                    uang = lines[i + 1].strip()
                    print(f"No {a}: {username} - {uang}")
                    a += 1
        except FileNotFoundError:
            print("Belum ada data highscore.")
        input("Tekan Enter untuk kembali ke menu...")

    def reset(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.path.exists("game.txt"):
            os.remove("game.txt")
        print("Data highscore telah direset.")
        input("Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    game = Game()
    game.menu()
