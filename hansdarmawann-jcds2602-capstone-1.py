from tabulate import tabulate
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
        "availability":True
    },
        {
        "platNo":"B1474PDC",
        "merk":"Land Rover",
        "nama":"Range Rover Sport",
        "trim":"Dynamic SE 3.0",
        "tipe":"SUV",
        "bahanBakar":"Hybrid",
        "statusEnergi":0.75,
        "warna":"Borasco Grey",
        "kondisi":"Mulus",
        "availability":False
    }
]

def lihatMobil(plat):
    if plat == "":
        print(tabulate(mobil, headers="keys"))
    else:
        filter = [row for row in mobil if row["platNo"] == plat]
        filtered_table = tabulate(filter, headers="keys")
        print(filtered_table)

lihatMobil("")
lihatMobil("B1474PDC")