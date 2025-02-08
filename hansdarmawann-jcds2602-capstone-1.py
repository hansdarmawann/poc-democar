from tabulate import tabulate
import validation
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
    if len(mobil) == 0:
        print("Tidak ada mobil yang tersedia.")
    else:
        if plat == "":
            print(tabulate(mobil, headers="keys"))
        else:
            filter = [row for row in mobil if row["platNo"] == plat]
            filtered_table = tabulate(filter, headers="keys")
            print(filtered_table)

def lihatPeminjaman(plat):
    if len(peminjaman) == 0:
        print("Tidak ada peminjaman yang sedang berjalan.")
    else:
        if plat == "":
            print(tabulate(peminjaman, headers="keys"))
        else:
            filter = [row for row in peminjaman if row["platNo"] == plat]
            filtered_table = tabulate(filter, headers="keys")
            print(filtered_table)

# Validation berguna untuk validasi menu
# try:
#     a = "B1474PDC"
#     print(validation.validate_text(a, pattern='[A-Z]{3}[0-9]{4}[A-Z]{3}'))
# except:
#     lihatPeminjaman(a)