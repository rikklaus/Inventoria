from inisialisasi import inisialisasi_gudang
from tambah import tambah_stok
from kurangi import kurangi_stok
from lihat import lihat_stok
from transfer import transfer_stok

def menu_utama():
    print("\n=== Manajemen Gudang ===")
    print("1. Tambah Stok")
    print("2. Kurangi Stok")
    print("3. Lihat Stok")
    print("4. Transfer Stok")
    print("5. Keluar")
    
def program_running():
    print("\n======= Selamat Datang di Program Inventoria =======")
    print("Silakan Inisialiasi Rak Pada Gudang ===")
    baris = int(input("Masukkan jumlah rak: "))
    kolom = int(input("Masukkan jumlah kolom per rak: "))

    stok = inisialisasi_gudang(baris, kolom)

    while True:
        menu_utama()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_stok(stok)
        elif pilihan == '2':
            kurangi_stok(stok)
        elif pilihan == '3':
            lihat_stok(stok)
        elif pilihan == '4':
            transfer_stok(stok)
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

program_running()