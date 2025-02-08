from tabulate import tabulate
# import validation
import datetime

mobil = [
    {
        "platNo":"B1071PDM",
        "merk":"Land Rover",
        "nama":"Range Rover",
        "trim":"SE 3.0 PHEV LWB",
        "tipe":"SUV",
        "bahanBakar":"Hybrid",
        "statusEnergi":0.9,
        "warna":"Belgravia Green",
        "kondisi":"Mulus",
        "ketersediaan":True
    },
    {
        "platNo":"B1606PEL",
        "merk":"Mercedes Benz",
        "nama":"G Class",
        "trim":"G63 AMG",
        "tipe":"SUV",
        "bahanBakar":"Hybrid",
        "statusEnergi":0.75,
        "warna":"MANUFAKTUR night black magno",
        "kondisi":"Mulus",
        "ketersediaan":False
    }
]

peminjaman = [
    {
        "platNo":"B1606PEL",
        "detailMobil":"Mercedes Benz G Class G63 AMG - MANUFAKTUR night black magno",
        "namaPeminjam":"Fitra Eri",
        "noSIMA":"123456789",
        "noTelp":"08123456789",
        "alasan":"Keperluan review",
        "tanggalPinjam":datetime.datetime(2024,6,24),
        "tanggalKembali":datetime.datetime(2024,6,30)
    }
]

def lihatMobil(plat):
    cari = False
    if plat == "":
        print(tabulate(mobil, headers="keys"))
    else:
        for item in mobil:
            if item["platNo"]==plat:
                cari = True
        if cari:
            pilih = [row for row in mobil if row["platNo"] == plat]
            hasil = tabulate(pilih, headers="keys")
            print(hasil)
        else:
            print("Data tidak ditemukan.")

def lihatPeminjaman(plat):
    cari = False
    if plat == "":
        print(tabulate(peminjaman, headers="keys"))
    else:
        for item in peminjaman:
            if item["platNo"]==plat:
                cari = True
        if cari:
            pilih = [row for row in peminjaman if row["platNo"] == plat]
            hasil = tabulate(pilih, headers="keys")
            print(hasil)
        else:
            print("Data tidak ditemukan.")

def lihatData():
    while True:
        try:
            print("""
            Lihat Data
                1. Lihat Mobil
                2. Lihat Peminjaman
                3. Kembali ke Menu Utama
            """
            )
            menu = int(input("Masukkan input anda: "))
            if menu == 1:
                plat = input("Masukkan plat nomor anda (kosongkan jika ingin lihat semua data): ").upper().replace(" ","")    
                lihatMobil(plat)
                lihatData()
            elif menu == 2:
                plat = input("Masukkan plat nomor anda (kosongkan jika ingin lihat semua data): ").upper().replace(" ","")   
                lihatPeminjaman(plat)
                lihatData()
            else:
                print("Kembali ke menu utama.")
                break
        except:
            print("Input tidak valid. Silahkan input ulang.")
            lihatData()

def main():
    while True:
        try:
            print("""
            Selamat Datang di Sistem Peminjaman Mobil Demo XYZ
            Silahkan Pilih Menu yang Tersedia di Bawah  :
                1. Lihat Data
                2. Tambah Mobil
                3. Pinjam Mobil
                4. Kembalikan Mobil
                5. Hapus Mobil
                6. Keluar
            """)
            menu = int(input("Masukkan input anda: "))
            if menu == 1:
                lihatData()
                main()
            elif menu == 6:
                print("Terima kasih, sampai jumpa !")
                break

        except:
            print("Input tidak valid. Silahkan input ulang.")
            main()


main()

# Validation berguna untuk validasi menu
# try:
#     a = "B1474PDC"
#     print(validation.validate_text(a, pattern='[A-Z]{3}[0-9]{4}[A-Z]{3}'))
# except:
#     lihatPeminjaman(a)