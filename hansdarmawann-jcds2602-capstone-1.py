from tabulate import tabulate
import datetime
import os
import platform


mobil = [
    {
        "platNo": "B1071PDM",
        "namaMobil": "Range Rover P615",
        "deskripsi": "SV, PHEV, British Racing Green", #to be removed
        "kilometer": 12345.678,
        "statusEnergi": 0.9, #to be removed
        "kondisi": "Mulus", #to be removed
        "ketersediaan": False, #ganti jadi ya atau tidak
        "namaPeminjam": "Fitra Eri",
        "kontak": "081234567891",
        "tanggalPeminjaman": datetime.date(2024, 6, 24),
        "tanggalKembali": datetime.date(2024, 6, 30),
        "alasan": "Keperluan Review"
    },
    {
        "platNo": "B1010LKX",
        "namaMobil": "Mercedes Benz G63 AMG",
        "deskripsi": "Bensin, Blue Metallic", #to be removed
        "kilometer": 901.23,
        "statusEnergi": 0.75, #to be removed
        "kondisi": "Mulus", #to be removed
        "ketersediaan": True, #ganti jadi ya atau tidak
        "namaPeminjam": "",
        "kontak": "",
        "tanggalPeminjaman": "",
        "tanggalKembali": "",
        "alasan": ""
    }
]

def lihatMobil(plat):
    try:
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
        print(tabulate(data, headers="keys", maxcolwidths=[12 for i in range(12)]))
    except Exception as e:
        print("Terjadi kesalahan saat mencetak data.")

def hapusMobil(plat):
    try:
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
    except Exception as e:
        print("Terjadi kesalahan saat meghapus data.")

def tambahMobil():
    while True:
        platNo = input("Masukkan plat nomor Mobil: ").upper().replace(" ","")
        tersedia = True #kalau ditaruh di outside loop, maka dia looping forever.
        for i in mobil:
            if i["platNo"] == platNo:
                tersedia = False
                print("Plat nomor mobil sudah tersedia. Silahkan input ulang plat nomor mobilnya.")

        if tersedia == True:
            print("Data berhasil di-input.")
            break
    namaMobil = input("Masukkan nama mobil: ")
    deskripsi = input("Masukkan deskripsi mobil")
    kilometer = float(input("Masukkan kilometer mobil"))
    statusEnergi = float(input("Masukkan status energi: "))
    kondisi = input("Masukkan kondisi mobil: ")
    mobilBaru = {
        "platNo": platNo,
        "namaMobil": namaMobil,
        "deskripsi": deskripsi,
        "kilometer": kilometer,
        "statusEnergi": statusEnergi,
        "kondisi": kondisi,
        "ketersediaan": True,
        "namaPeminjam": "",
        "kontak": "",
        "tanggalPeminjaman": "",
        "tanggalKembali": "",
        "alasan": ""
    }
    mobil.append(mobilBaru)

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
            lanjutkan()
        if menu == 4:
            lihatMobil("")
            print()
            plat = input("Masukkan plat nomor anda: ")
            hapusMobil(plat)
            lanjutkan()
        elif menu == 5:
            print("Terima kasih, sampai jumpa !")
            exit()

    except Exception as e:
        print("Input tidak valid. Silahkan input ulang.")

def lanjutkan():
    osName = platform.system()
    input("Tekan Enter untuk melanjutkan...")
    if osName == 'Windows':
        os.system("cls") #ganti parameternya jadi "clear" jika MacOS atau Linux
    else:
        os.system("clear")
    main()

if __name__ == "__main__":
    main()
# tambahMobil()