from tabulate import tabulate
import datetime

mobil = [
    {
        "platNo": "B1071PDM",
        "namaMobil": "Range Rover P615",
        "deskripsi": "SV, PHEV, British Racing Green",
        "kilometer": 12345.678,
        "statusEnergi": 0.9,
        "kondisi": "Mulus",
        "ketersediaan": False,
        "namaPeminjam": "Fitra Eri",
        "kontak": "081234567891",
        "tanggalPeminjaman": datetime.date(2024, 6, 24),
        "tanggalKembali": datetime.date(2024, 6, 30),
        "alasan": "Keperluan Review"
    },
    {
        "platNo": "B1010LKX",
        "namaMobil": "Mercedes Benz G63 AMG",
        "deskripsi": "Bensin, Blue Metallic",
        "kilometer": 901.23,
        "statusEnergi": 0.75,
        "kondisi": "Mulus",
        "ketersediaan": True,
        "namaPeminjam": "",
        "kontak": "",
        "tanggalPeminjaman": "",
        "tanggalKembali": "",
        "alasan": ""
    }
]

def lihatMobil(plat):
    plat = plat.upper().replace(" ","")
    cari = False
    if plat == "":
        data = mobil
    else:
        for item in mobil:
            if item["platNo"] == plat:
                cari = True
        if cari:
            data = [row for row in mobil if row["platNo"] == plat]
        else:
            print("Data tidak ditemukan.")
            return 
            # Kalau gak ada return, maka Terjadi kesalahan saat mencetak data: cannot access local variable 'data' where it is not associated with a value.
            # Kenapa ? Karena data kosong, sehingga tabulate bingung mau apa.
    try:
        print(tabulate(data, headers="keys", maxcolwidths=[12 for i in range(12)]))
    except Exception as e:
        print("Terjadi kesalahan saat mencetak data:", e)


def hapusMobil(plat):
    plat = plat.upper().replace(" ","")
    cari = False
    for item in mobil:
        if item["platNo"] == plat and item["ketersediaan"] == True:
            cari = True
            mobil.remove(item)
            print("Data terhapus.")
            break
        elif item["platNo"] == plat and item["ketersediaan"] == False:
            cari = True
            print("Mobil harus dikembalikan dulu, baru bisa dihapus.")
            break

    if not cari:
        print("Data tidak ditemukan.")
        

def main():
    try:
        print("""
        Selamat Datang di Sistem Peminjaman Mobil Demo XYZ
        Silahkan Pilih Menu yang Tersedia di Bawah  :
            1. Lihat Data
            2. Tambah Mobil
            3. Update Mobil
            4. Hapus Mobil
            5. Keluar
        """)
        menu = int(input("Masukkan input anda: "))
        if menu == 1:
            plat = input("Masukkan plat nomor anda (kosongkan jika ingin lihat semua data): ")
            lihatMobil(plat)
            main()
        if menu == 4:
            lihatMobil("")
            print()
            plat = input("Masukkan plat nomor anda: ")
            hapusMobil(plat)
            main()
        elif menu == 5:
            print("Terima kasih, sampai jumpa !")
            exit()

    except Exception as e:
        print("Input tidak valid. Silahkan input ulang.")
        # print(e) # Uncomment jika ingin trace error.

if __name__ == "__main__":
    main()
