class Supermarket:
    Pemasukan = 0
    Pengeluaran = 0
    Produks = []

    def __init__(self, nama):
        self.nama = nama

    def FuncTambah(self, Produks):
        for produkBaru in Produks:
            for produk in self.Produks:
                if produk['nama'] == produkBaru['nama']:
                    print("Produk", produkBaru['nama'], "sudah ada.")
                    return False
            self.Produks.append(produkBaru)
            self.Pengeluaran += produkBaru['harga'] * produkBaru['stok']

        for produk in self.Produks:
            produk["harga"] = int(produk["harga"])
        print("Produk berhasil ditambahkan")
        return False
    
    def FuncUbahProduk(self):
        NamaProduk = input("Masukkan nama produk: ")
        for produk in self.Produks:
            if produk['nama'] == NamaProduk.capitalize():
                pilihan = input("Apakah Anda ingin mengubah stok atau harga? (S/H): ")
                if pilihan.upper() == "S":
                    gantiStok = int(input("Masukkan jumlah stok baru: "))
                    produk['stok'] = gantiStok
                    print("Stok", NamaProduk, "telah diganti menjadi", gantiStok)
                    if produk['stok'] == 0:
                                Supermarket.Produks.remove(produk)
                                print("Produk", NamaProduk, "telah habis dan dihapus dari daftar produk.")
                elif pilihan.upper() == "H":
                    gantiHarga = int(input("Masukkan harga baru: "))
                    produk['harga'] = gantiHarga
                    print("Harga", NamaProduk, "telah diganti menjadi", gantiHarga)
                return
        print("Produk", NamaProduk, "tidak ditemukan")

    def FuncPemasukan(self):
        if self.Pemasukan == 0:
            print("Pemasukan: 0")
            return False
        else:
            print("Pemasukan: ", self.Pemasukan)
            return False
    
    def FuncPengeluaran(self):
        if self.Pengeluaran == 0:
            print("Pengeluaran: 0")
            return False
        else:
            print("Pengeluaran: ", self.Pengeluaran)
            return False
    
    def FuncTampilkan(self):
        if len(self.Produks) == 0:
            print("Produk kosong")
            return False
        else:
            print("{:<20} {:<10} {:<10}".format('Nama', 'Harga', 'Stok'))
            print("="*40)
            for produk in self.Produks:
                print("{:<20} {:<10} {:<10}".format(produk['nama'], produk['harga'], produk['stok']))
            return False

    def FuncDetail(self):
        print("Nama Toko\t: ", self.nama)
        return False
    
    def FuncExit(self):
        print("Terima kasih telah menggunakan layanan kami")
        exit()
KosongProd = []
Supermarket = Supermarket("Purwadhika Berkah")

while True:

    CekVal = input("Apakah anda Customer/Admin? (C/A) Ketik E untuk Exit : ")
    if CekVal.upper() == "A":
       
       while True:
        print("""
1. Tambah Produk
2. Ubah Detail Stok/Harga Produk
3. Cek Pengeluaran dan Pemasukan
4. Detail Toko
5. Tampilkan Produk
6. Exit
        """)
        try:
            pilihan = int(input("Masukkan pilihan (1-6): "))
        except ValueError:
            print("Input tidak valid. Masukkan angka!")
            continue

        if pilihan == 1:
            try:
                NamaProduk = input("Masukkan nama produk: ")
                HargaProduk = int(input("Masukkan harga produk: "))
                Stok = int(input("Masukkan stok produk: "))
                produk = dict(nama=NamaProduk, harga=HargaProduk, stok=Stok)
                KosongProd.append(produk)
                Supermarket.FuncTambah(KosongProd)
                KosongProd.clear()
            except ValueError:
                continue
        elif pilihan == 2:
            Supermarket.FuncTampilkan()
            Supermarket.FuncUbahProduk()
        elif pilihan == 3:
            Supermarket.FuncPengeluaran()
            Supermarket.FuncPemasukan()
        elif pilihan == 4:
            Supermarket.FuncDetail()
        elif pilihan == 5:
            Supermarket.FuncTampilkan()
        elif pilihan == 6:
            break
            
    elif CekVal.upper() == "C":
        while True:
            print("""
1. Membeli Barang
2. Melihat Produk 
3. Exit
""")
            try:    
               pilihan = int(input("Masukkan pilihan (1-3): "))
            except ValueError:
               print("Input tidak valid. Masukkan angka!")
               continue

            if pilihan == 1:
                if  len(Supermarket.Produks) == 0:
                    print("Maaf, saat ini tidak ada produk yang tersedia")
                else:
                    Supermarket.FuncTampilkan()
                    NamaProduk = input("Masukkan nama produk: ")
                    jumlah = int(input("Masukkan jumlah: "))
                    for produk in Supermarket.Produks:
                        if produk['nama'] == NamaProduk.capitalize():
                            if produk['stok'] >= jumlah:
                                produk['stok'] -= jumlah
                                print("Anda membeli", NamaProduk, "sebanyak", jumlah)
                                Supermarket.Pemasukan += produk['harga'] * jumlah
                                if produk['stok'] == 0:
                                    Supermarket.Produks.remove(produk)
                            else:
                                print("Stok", NamaProduk, "tidak cukup")
            elif pilihan == 2:
                Supermarket.FuncTampilkan()
            elif pilihan == 3:
                break
    elif CekVal.upper() == "E":
        Supermarket.FuncExit()