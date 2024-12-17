def lihat_stok(stok):
    print("\n--- Kondisi Stok Gudang ---")
    for i in range(len(stok)):
        for j in range(len(stok[i])):
            print(f"Rak {i+1}, Kolom {j+1}: {stok[i][j]}")