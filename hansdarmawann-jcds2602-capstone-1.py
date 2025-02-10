from tabulate import tabulate
import datetime
import os
import platform


mobil = [
    {
        "platNo": "B1071PDM",
        "namaMobil": "Range Rover P615",
        "kilometer": 12345.678,
        "tersedia": "Ya",
        "namaPeminjam": "Fitra Eri",
        "kontak": "081234567891",
        "tanggalPeminjaman": datetime.date(2024, 6, 24),
        "tanggalKembali": datetime.date(2024, 6, 30),
        "alasan": "Keperluan Review"
    },
    {
        "platNo": "B1010LKX",
        "namaMobil": "Mercedes Benz G63 AMG",
        "kilometer": 901.23,
        "tersedia": "Tidak",
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
        print(tabulate(data, headers="keys", maxcolwidths=[9 for i in range(9)]))
    except Exception as e:
        print("Terjadi kesalahan saat mencetak data.")

def hapusMobil(plat):
    try:
        plat = plat.upper().replace(" ","")
        cari = False
        for item in mobil:
            if item["platNo"] == plat and item["flagan"] == True:
                cari = True
                mobil.remove(item)
                print("Data terhapus.")
                break
            elif item["platNo"] == plat and item["flagan"] == False:
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
        flag = True #kalau ditaruh di outside loop, maka dia looping forever.
        if platNo == "":
            flag = False
            print("Plat nomor mobil tidak boleh kosong !")

        for item in mobil:
            if item["platNo"] == platNo:
                flag = False
                print("Plat nomor mobil sudah tersedia. Silahkan input ulang plat nomor mobilnya.")

        if flag == True:
            print("Plat nomor berhasil di-input.")
            break
    
    while True:
        namaMobil = input("Masukkan nama mobil: ")
        flag = True
        if namaMobil == "":
            flag = False
            print("Nama mobil tidak boleh kosong !")
        
        if flag == True:
            print("Nama mobil berhasil di-input")
            break
    
    while True:
        try:
            kilometer = float(input("Masukkan kilometer mobil: "))
            flag = True
            if kilometer == "":
                flag = False
                print("Kilometer harus diisi !")

            if flag == True:
                kilometer = float(kilometer)
                print("Data berhasil di-input")
                break
        except Exception as e:
            print("Kilometer harus diisi dengan angka bulat atau angka desimal !")

    mobilBaru = {
        "platNo": platNo,
        "namaMobil": namaMobil,
        "kilometer": kilometer,
        "tersedia": "Ya",
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
        Silahkan Pilih Menu yang flag di Bawah  :
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
        elif menu ==2:
            tambahMobil()
            lanjutkan()
        elif menu == 4:
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