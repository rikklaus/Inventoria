# Fungsi untuk input stok barang dari pengguna dengan nama kategori
def input_stok(gudang_name):
    print(f"\nMasukkan stok barang untuk {gudang_name}:")
    stok = []
    kategori_barang = []  # Menyimpan nama kategori
    for i in range(3):  # Jumlah baris (3 kategori barang)
        kategori = input(f"Masukkan nama kategori untuk kategori {i+1}: ")
        kategori_barang.append(kategori)  # Menyimpan nama kategori
        row = []
        for j in range(3):  # Jumlah kolom (3 jenis barang per kategori)
            jumlah = int(input(f"Masukkan jumlah barang untuk kategori '{kategori}', barang {j+1}: "))
            row.append(jumlah)
        stok.append(row)
    
    return stok, kategori_barang

# Fungsi untuk input pengurangan stok setelah pengiriman
def input_pengurangan():
    print("\nMasukkan jumlah pengurangan stok setelah pengiriman:")
    pengurangan = []
    for i in range(3):  # Jumlah kategori
        row = []
        for j in range(3):  # Jumlah jenis barang
            jumlah_pengurangan = int(input(f"Masukkan jumlah pengurangan untuk kategori {i+1}, barang {j+1}: "))
            row.append(jumlah_pengurangan)
        pengurangan.append(row)
    return pengurangan

# Mengambil input stok barang di Gudang A dan Gudang B
stok_gudang_A, kategori_A = input_stok("Gudang A")
stok_gudang_B, kategori_B = input_stok("Gudang B")

# Mengambil input pengurangan stok setelah pengiriman
pengurangan = input_pengurangan()

# Inisialisasi matriks untuk hasil operasi
total_stok = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

stok_setelah_pengiriman = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]

# PENJUMLAHAN: Menghitung total stok dari Gudang A + Gudang B
for i in range(len(stok_gudang_A)):       # Iterasi baris
    for j in range(len(stok_gudang_A[0])):  # Iterasi kolom
        total_stok[i][j] = stok_gudang_A[i][j] + stok_gudang_B[i][j]

# PENGURANGAN: Menghitung stok setelah ada pengiriman (dikurangkan sesuai input pengguna)
for i in range(len(total_stok)):       
    for j in range(len(total_stok[0])):  
        stok_setelah_pengiriman[i][j] = total_stok[i][j] - pengurangan[i][j]  # Dikurangi sesuai input

# Menampilkan hasil
print("\nStok Gudang A:")
for i, row in enumerate(stok_gudang_A):
    print(f"Kategori '{kategori_A[i]}': {row}")

print("\nStok Gudang B:")
for i, row in enumerate(stok_gudang_B):
    print(f"Kategori '{kategori_B[i]}': {row}")

print("\nTotal Stok (A + B):")
for i, row in enumerate(total_stok):
    print(f"Kategori '{kategori_A[i]}': {row}")

print("\nStok Setelah Pengiriman (Dikurangkan sesuai input):")
for i, row in enumerate(stok_setelah_pengiriman):
    print(f"Kategori '{kategori_A[i]}': {row}")