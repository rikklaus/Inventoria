def transfer_stok(stok):
    print("\n--- Transfer Stok ---")
    rak_asal = int(input("Masukkan nomor rak asal: ")) - 1
    kolom_asal = int(input("Masukkan nomor kolom asal: ")) - 1
    rak_tujuan = int(input("Masukkan nomor rak tujuan: ")) - 1
    kolom_tujuan = int(input("Masukkan nomor kolom tujuan: ")) - 1

    if rak_asal >= len(stok) or kolom_asal >= len(stok[0]) or rak_tujuan >= len(stok) or kolom_tujuan >= len(stok[0]):
        print("Rak atau kolom tidak valid.")
        return