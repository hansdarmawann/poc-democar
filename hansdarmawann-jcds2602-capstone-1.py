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
        "platNo":"B1474PDC",
        "merk":"Land Rover",
        "nama":"Range Rover Sport",
        "trim":"Dynamic SE 3.0 PHEV",
        "tipe":"SUV",
        "bahanBakar":"Hybrid",
        "statusEnergi":0.75,
        "warna":"Borasco Grey",
        "kondisi":"Mulus",
        "ketersediaan":False
    }
]

peminjaman = [
    {
        "platNo":"B1474PDC",
        "detailMobil":"Land Rover Range Rover Sport Dynamic SE 3.0 PHEV - Borasco Grey",
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
            filter = [row for row in mobil if row["platNo"] == plat]
            filtered_table = tabulate(filter, headers="keys")
            print(filtered_table)
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
            filter = [row for row in peminjaman if row["platNo"] == plat]
            filtered_table = tabulate(filter, headers="keys")
            print(filtered_table)
        else:
            print("Data tidak ditemukan.")

def lihatData():
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
            main()
    except:
        print("Input tidak valid. Silahkan input ulang.")
        lihatData()

def main():
    print("Test")

lihatData()

# Validation berguna untuk validasi menu
# try:
#     a = "B1474PDC"
#     print(validation.validate_text(a, pattern='[A-Z]{3}[0-9]{4}[A-Z]{3}'))
# except:
#     lihatPeminjaman(a)