def transfer_stok(stok):
    print("\n--- Transfer Stok ---")
    rak_asal = int(input("Masukkan nomor rak asal: ")) - 1
    kolom_asal = int(input("Masukkan nomor kolom asal: ")) - 1
    rak_tujuan = int(input("Masukkan nomor rak tujuan: ")) - 1
    kolom_tujuan = int(input("Masukkan nomor kolom tujuan: ")) - 1

    if rak_asal >= len(stok) or kolom_asal >= len(stok[0]) or rak_tujuan >= len(stok) or kolom_tujuan >= len(stok[0]):
        print("Rak atau kolom tidak valid.")
        return
    
    jumlah = int(input("Masukkan jumlah barang yang ingin ditransfer: "))
    if jumlah > stok[rak_asal][kolom_asal]:
        print("Jumlah barang yang ingin ditransfer melebihi stok di rak asal.")
    else:
        stok[rak_asal][kolom_asal] -= jumlah
        stok[rak_tujuan][kolom_tujuan] += jumlah
        print("Stok berhasil ditransfer.")