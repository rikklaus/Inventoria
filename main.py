from menu import menu_utama

def program_running():
    print("\n=== Inisialisasi Gudang ===")
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