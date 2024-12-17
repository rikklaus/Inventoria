def kurangi_stok(stok):
    print("\n--- Kurangi Stok ---")
    for i in range(len(stok)):
        for j in range(len(stok[i])):
            jumlah = int(input(f"Rak {i+1}, Kolom {j+1}: "))
            if jumlah > stok[i][j]:
                print(f"Jumlah melebihi stok di Rak {i+1}, Kolom {j+1}.")
            else:
                stok[i][j] -= jumlah
    print("Stok berhasil dikurangi.")