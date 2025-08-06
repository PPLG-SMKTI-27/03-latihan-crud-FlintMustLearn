# data buku
books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis dan Perancangan Sistem Informasi", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":0, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""}
]

def tampilkan_data():
    print("No\tISBN\tJudul\tPengarang\tJumlah\tTerpinjam")
    for i in range(len(books)):
        print(i+1,"\t", end=" ")
        print("\t",books[i]["isbn"],"\t", books[i]["judul"], "\t", books[i]["pengarang"], "\t", books[i]["jumlah"], "\t", books[i]["terpinjam"])
        

def tambah_data():
    print("Menambahkan Buku")
    isbn = input("ISBN: ")
    judul = input("Judul: ")
    pengarang = input("Pengarang: ")
    Jumlah = input("jumlah buku yang ingin ditambahkan: ")
    tambahbuku = {"isbn":isbn, "judul":judul, "pengarang":pengarang, "jumlah":Jumlah, "terpinjam":0}
    books.append(tambahbuku)

def edit_data(id):
    if 0 < id <= len(books):
        ISBN = input("Masukkan ISBN Buku yang ingin diubah!: ")
        JUDUL = input("Input Judul Bukunya!: ")
        PENGARANG = input("Masukkan nama pengarang-nya!: ")
        JUMLAH = input("Masukkan Jumlah buku yang ingin diubah: ")
        books[id - 1] = {
            "isbn":ISBN,
            "judul":JUDUL,
            "pengarang":PENGARANG,
            "jumlah":JUMLAH,
            "terpinjam":0
        }
        print("Berhasil!")
        tampilkan_data()
    else:
        print("Invalid!")

def hapus_data(idh):
    if 0 < idh <= len(books):
        del books[idh - 1]
        print("Berhasil!")
        tampilkan_data()

def tampilkan_peminjaman():
    print("No\tISBN\tStatus\tTanggal Pinjam\t Tanggal kembali")
    for i in range(len(records)):
        print(i+1,"\t", end=" ")
        print(records[i]["isbn"], "\t", records[i]["status"], "\t", records[i]["tanggal_pinjam"], "\t", records[i]["tanggal_kembali"])

def tampilkan_belum():
    print("No\tISBN\tStatus\tTanggal Pinjam\t Tanggal kembali")
    j = 1
    for i in range(len(records)):
        if records[i]["status"] == "Belum":
            print(j,"\t", end=" ")
            print(records[i]["isbn"], "\t", records[i]["status"], "\t", records[i]["tanggal_pinjam"], "\t", records[i]["tanggal_kembali"])
            j += 1


def peminjaman():
    pilihlah = int(input("Buku nomor berapa yang ingin kamu pinjam?: "))
    tanggalPinjam = str(input('Tanggal berapa? dalam format "YY-MM-DD" '))
    if books[pilihlah-1]["jumlah"] > 0:
        books[pilihlah-1]["terpinjam"] += 1
        books[pilihlah-1]["jumlah"] -= 1
        BerhasilDiPinjam = {"isbn":books[pilihlah-1]["isbn"], "status":"Belum", "tanggal_pinjam":tanggalPinjam, "tanggal_kembali":""}
        records.append(BerhasilDiPinjam)
        print("Berhasil di pinjam!")
    else:
        print("Buku tidak tersedia!")
    

def pengembalian():
    pilihlah2 = int(input("Buku nomor berapa yang ingin kamu kembalikan?: "))
    tanggalKembalikan = str(input('Tanggal berapa? dalam format "YY-MM-DD" '))
    tanggalPinjam = records[pilihlah2-1]["tanggal_pinjam"]
    BerhasilDiPinjam = {"isbn":books[pilihlah2-1]["isbn"], "status":"Selesai", "tanggal_pinjam":tanggalPinjam, "tanggal_kembali":tanggalKembalikan,}
    records.append(BerhasilDiPinjam)
    if books[pilihlah2-1]["terpinjam"] > 0:
        books[pilihlah2-1]["jumlah"] += 1
        books[pilihlah2-1]["terpinjam"] -= 1
        print("Berhasil di kembalikan!")
    else:
        print("Buku ini tidak ada yang pinjam!!!")


while True:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman yang Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")
    
    match menu:
        case "1":
            tampilkan_data()
        case "2":
            tambah_data()
        case "3":
            edit_data(id = int(input("Input buku dengan nomor berapa yang ingin diubah!: ")))
        case "4":
            hapus_data(idh = int(input("Inout buku dengan nomor berapa yang ingin di hapus!: ")))
        case "5":
            tampilkan_peminjaman()
        case "6":
            tampilkan_belum()
        case "7":
            peminjaman()
        case "8":
            pengembalian()
        case "X" | "x":
            print("Goodbye")
            break
        case _:
            print("Invalid")
