def tambah_stok(stok):
    print("\n--- Tambah Stok ---")
    for i in range(len(stok)):
        for j in range(len(stok[i])):
            jumlah = int(input(f"Rak {i+1}, Kolom {j+1}: "))
            stok[i][j] += jumlah
    print("Stok berhasil ditambahkan.")